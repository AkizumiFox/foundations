#!/usr/bin/env python3
"""Find the book's forward promises and reconcile them with authoring/STATUS.md.

A forward promise is a prose pointer to a later part of the series with no `@ref`
behind it: "Chapter 9 turns this into the definition of a limit", "Section 1.5
separates the two", "*Analysis on the Real Line*, Chapter 1 states them as axioms",
"the rules of §04". STYLE §7 says every one must be paid off and recorded in
STATUS.md's "Forward promises" table; this tool finds them so the table can be
checked rather than remembered.

Chapters are named by their **atlas id** (`F1.4`, `F2.1`, `AN1.1`; tools/series.py),
because chapter numbers restart in every volume. In the prose:

* `Chapter N`, `Chapters N–M` (each chapter in the range), `Chapters N and M`,
  `Section N.M` (chapter N, section M) are chapters of the volume the file is in;
* `*Title*, Chapter N` / `*Title*, Section N.M` are chapters of the volume with that
  title (the engine prints a reference into another book the same way);
* `§NN` / `§NN–§MM` is a section of the *current* chapter;
* only pointers **forward** of the file they are in count: a later chapter in the
  series' reading order (volumes in math-atlas order, then chapter numbers), or a later
  section of the same chapter; a pointer back is a recall, not a promise;
* not the linear-algebra companion's chapters, and not math, code or raw LaTeX;
* a pointer whose sentence also carries an `@ref` (or `@prefix:ref`) to a label defined
  in the target chapter counts as linked, not as a promise. Labels of another volume
  are read from its sources when they are reachable (this repository, or a sibling
  checkout of the other repository); otherwise any `@prefix:` reference into that
  volume counts.

STATUS.md (shared by the volumes of a repository, at its root) names chapters by atlas
id: a row's From cell is `F1.1 §01, §02, index`, its Target cell names the target
chapters (`F1.3 (paid: ...)`).

    python3 tools/promises.py --book fd1                # every promise of a volume, by target
    cd fd2 && python3 ../tools/promises.py --for 3      # what fd2's Chapter 3 (F2.3) must pay
    python3 tools/promises.py --for AN1.1               # what AN1.1 must pay, from every volume here
    python3 tools/promises.py --reconcile               # every volume of the repository; exit 1 if any

Run in a volume directory (or with --book), the tool reads that volume; at the
repository root it reads every volume that has sources. Without authoring/series.json
(a plain book) chapters are named by their numbers, as before the split.

Importable:

    from tools.promises import find_promises, parse_status, reconcile
"""
import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series as series_mod  # noqa: E402

SRC = Path("src")
STATUS = Path("authoring/STATUS.md")

DASH = r"\s*(?:–|—|-|to)\s*"
TITLE = r"(?:\*(?P<title>[^*\n]{1,160}?)\*,\s+)?"
CHAPTERS = re.compile(
    rf"{TITLE}\bChapters?\s+(\d+)((?:(?:{DASH}|\s*,\s*|\s+and\s+|\s+or\s+)\d+(?!\.\d))*)")
SECTION = re.compile(rf"{TITLE}\bSections?\s+(\d+)\.(\d+)")
PARA = re.compile(rf"§\s*(\d+)(?:{DASH}§?\s*(\d+))?")
ATLAS_SEC = re.compile(rf"\b([A-Z]{{1,3}}\d?\.\d+[ab]?)\b(?:\s*(§\s*(\d+)(?:{DASH}§?\s*(\d+))?))?")
LABEL_DEF = re.compile(r"\{#([a-z]+-[\w-]+)")
REF = re.compile(r"@(?:([a-z][a-z0-9]*):)?([a-z]+-[\w-]+)")
STATUS_CH = re.compile(r"\bCh\s*(\d+)")


@dataclass(frozen=True)
class Promise:
    file: str          # e.g. fd2/ch01-sets-and-functions/03-products.md
    line: int
    chapter: str       # chapter the pointer is written in (atlas id; a number without a series)
    section: str       # "03", or "index"
    target: str        # target chapter
    target_section: int | None
    text: str          # the pointer as written, with a little context


class Context:
    """The series map and how to name and order chapters (atlas ids, or plain numbers)."""

    def __init__(self, series=None):
        self.series = series if series is not None else series_mod.Series.load()
        self._labels = {}

    def chapter_id(self, volume, n: int):
        if self.series and volume is not None:
            return self.series.atlas_id(volume.prefix, n)
        return str(n)

    def order(self, cid: str):
        if self.series:
            return self.series.order_key(cid)
        return (0, int(cid)) if cid.isdigit() else (10 ** 6, 0)

    def describe(self, cid: str) -> str:
        return self.series.describe(cid) if self.series else f"Ch {cid}"

    def labels(self, cid: str, local_src: Path, volume):
        """Labels defined in chapter `cid`, or None if its sources are not reachable."""
        if cid in self._labels:
            return self._labels[cid]
        found = None
        if self.series:
            d = self.series.chapter_dir(cid)
            if d is None and volume is not None:
                loc = self.series.locate(cid)
                if loc and loc[0] == volume.prefix:
                    hits = sorted(Path(local_src).glob(f"ch{loc[1]:02d}-*"))
                    d = hits[0] if hits else None
        else:
            hits = sorted(Path(local_src).glob(f"ch{int(cid):02d}-*")) if cid.isdigit() else []
            d = hits[0] if hits else None
        if d is not None:
            found = set()
            for f in d.rglob("*.md"):
                found |= set(LABEL_DEF.findall(f.read_text(encoding="utf-8")))
        self._labels[cid] = found
        return found


def chapter_of(dirname: str):
    m = re.match(r"ch(\d+)", dirname)
    return int(m.group(1)) if m else None


def section_of(path: Path) -> str:
    m = re.match(r"(\d+)", path.name)
    return m.group(1) if m else "index"


def expand(first: str, rest: str) -> list:
    nums = [int(first)]
    for m in re.finditer(rf"({DASH}|\s*,\s*|\s+and\s+|\s+or\s+)(\d+)", rest):
        n = int(m.group(2))
        if re.fullmatch(DASH, m.group(1)) and n > nums[-1]:
            nums += list(range(nums[-1] + 1, n + 1))
        else:
            nums.append(n)
    return nums


def prose_lines(text: str):
    """(lineno, line) for prose lines, with math and code blanked out."""
    doc = mdblocks.parse(text)
    joined = "\n".join("" if code else ln for ln, code in zip(doc.lines, doc.in_code))
    joined = re.sub(r"\\\[.*?\\\]", lambda m: "\n" * m.group(0).count("\n"), joined, flags=re.S)
    joined = re.sub(r"\\\(.*?\\\)", lambda m: " " + "\n" * m.group(0).count("\n"), joined, flags=re.S)
    joined = re.sub(r"`[^`\n]*`", " ", joined)
    return list(enumerate(joined.split("\n"), 1))


def sentence_around(line: str, pos: int) -> str:
    start = max(line.rfind(". ", 0, pos), line.rfind("; ", 0, pos))
    end_candidates = [i for i in (line.find(". ", pos), line.find("; ", pos)) if i >= 0]
    end = min(end_candidates) if end_candidates else len(line)
    return line[start + 1 if start >= 0 else 0:end + 1]


def _volume_named(ctx, title, here):
    """The volume a pointer names: its title, or the volume the file is in."""
    if title is None:
        return here, True
    if not ctx.series:
        return None, False
    v = ctx.series.volume_by_title(title)
    return v, v is not None


def find_promises(src: Path = SRC, ctx: Context | None = None, volume=None, label: str = "") -> list:
    """The forward promises of one volume's sources. `volume` is its series.Volume (None for a
    plain book); `label` prefixes the file names (e.g. "fd2/")."""
    src = Path(src)
    ctx = ctx or Context(series_mod.Series({}))
    promises = []
    for f in sorted(src.rglob("*.md")):
        n = chapter_of(f.parent.name)
        if n is None:
            continue
        ch = ctx.chapter_id(volume, n)
        if ch is None:
            continue
        sec = section_of(f)
        cur = int(sec) if sec.isdigit() else 0
        rel = f"{label}{f.parent.name}/{f.name}"
        for lineno, line in prose_lines(f.read_text(encoding="utf-8")):
            hits = []
            for m in CHAPTERS.finditer(line):
                if "companion" in line[max(0, m.start() - 40):m.start()]:
                    continue
                vol, ok = _volume_named(ctx, m.group("title"), volume)
                if not ok:
                    continue
                for k in expand(m.group(2), m.group(3) or ""):
                    t = ctx.chapter_id(vol, k)
                    if t is not None:
                        hits.append((m, t, None))
            for m in SECTION.finditer(line):
                vol, ok = _volume_named(ctx, m.group("title"), volume)
                if not ok:
                    continue
                t = ctx.chapter_id(vol, int(m.group(2)))
                if t is not None:
                    hits.append((m, t, int(m.group(3))))
            # bookkeeping (dependency ledgers): "F1.4 §10" is a section of F1.4, not of this
            # chapter (as "Section 4.10" was before the split; a bare atlas id is not a promise)
            owned = set()
            if ctx.series:
                for m in ATLAS_SEC.finditer(line):
                    if m.group(2) and ctx.series.locate(m.group(1)) is not None:
                        owned.add(m.start(2))
                        lo = int(m.group(3))
                        hi = int(m.group(4)) if m.group(4) else lo
                        for s_ in range(lo, hi + 1):
                            hits.append((m, m.group(1), s_))
            for m in PARA.finditer(line):
                if m.start() in owned:
                    continue
                lo = int(m.group(1))
                hi = int(m.group(2)) if m.group(2) else lo
                for s in range(lo, hi + 1):
                    hits.append((m, ch, s))
            seen = set()
            for m, target, tsec in hits:
                if target == ch:
                    forward = tsec is not None and tsec > cur
                else:
                    forward = ctx.order(target) > ctx.order(ch)
                if not forward or (target, tsec) in seen:
                    continue
                seen.add((target, tsec))
                sentence = sentence_around(line, m.start())
                if _linked(ctx, sentence, target, src, volume):
                    continue
                context = line[max(0, m.start() - 50):m.end() + 50].strip()
                promises.append(Promise(rel, lineno, ch, sec, target, tsec, context))
    return promises


def _linked(ctx, sentence, target, src, volume) -> bool:
    refs = REF.findall(sentence)
    if not refs:
        return False
    labels = ctx.labels(target, src, volume)
    if labels is not None:
        return any(lab in labels for _, lab in refs)
    loc = ctx.series.locate(target) if ctx.series else None
    return bool(loc) and any(p == loc[0] for p, _ in refs)


def volume_sources(ctx: Context, here: Path = Path(".")):
    """[(src, volume, label)] to scan: the volume `here` is, else every volume of the
    repository that has sources, else `here/src` as a plain book."""
    here = Path(here).resolve()
    s = ctx.series
    if s:
        v = s.volume_at(here)
        if v is not None:
            return [(here / "src", v, f"{v.prefix}/")]
        if here == s.repo.resolve():
            return [(s.repo / x.dir / "src", x, f"{x.prefix}/") for x in s.volumes
                    if x.repo == s.name and (s.repo / x.dir / "src").is_dir()]
    return [(here / "src", None, "")]


# ---------------------------------------------------------------------------
# STATUS.md
# ---------------------------------------------------------------------------

@dataclass
class Row:
    line: int
    source: str
    chapter: str | None
    sections: set          # {"01", "index", ...}; empty = whole chapter
    promise: str
    targets: set
    paid: bool


def _ids(cell: str) -> list:
    ids = series_mod.ATLAS_ID.findall(cell)
    return ids if ids else STATUS_CH.findall(cell)


def parse_status(path: Path = STATUS) -> list:
    rows = []
    text = Path(path).read_text(encoding="utf-8")
    in_table = False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            in_table = line.strip() == "## Forward promises"
            continue
        if not in_table or not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] == "From":
            continue
        frm, promise, target = cells[0], cells[1], cells[2]
        first = _ids(frm)
        sections = set(re.findall(r"§(\d+)", frm))
        if re.search(r"\bindex\b", frm):
            sections.add("index")
        rows.append(Row(n, line, first[0] if first else None, sections, promise,
                        set(_ids(target)), "paid" in target.lower()))
    return rows


def existing_sections(src: Path = SRC, ctx: Context | None = None, volume=None) -> set:
    """{(chapter id, section number)} for every section file in src."""
    ctx = ctx or Context(series_mod.Series({}))
    out = set()
    for f in Path(src).rglob("*.md"):
        n, sec = chapter_of(f.parent.name), section_of(f)
        if n is not None and sec.isdigit():
            out.add((ctx.chapter_id(volume, n), int(sec)))
    return out


def reconcile(promises: list, rows: list, sections: set = frozenset(), ctx: Context | None = None):
    """Promises with no STATUS row: (promise, reason) pairs.

    A row covers a promise when it has the same source chapter and target chapter,
    and lists the promise's section (or lists no section at all). A pointer to a
    later section of the *same* chapter needs no row: it is paid when that section
    exists (`sections`, from `existing_sections`), and reported when it does not.
    """
    name = (ctx.describe if ctx else (lambda c: f"Ch {c}"))
    missing = []
    for p in promises:
        if p.target == p.chapter:
            if (p.target, p.target_section) not in sections:
                missing.append((p, f"points at §{p.target_section:02d}, which does not exist"))
            continue
        candidates = [r for r in rows if r.chapter == p.chapter and p.target in r.targets]
        if not candidates:
            missing.append((p, f"no row {name(p.chapter)} → {name(p.target)}"))
        elif not any(not r.sections or p.section in r.sections for r in candidates):
            missing.append((p, f"row(s) {name(p.chapter)} → {name(p.target)} exist but do not list "
                               f"{'§' + p.section if p.section != 'index' else 'index'}"))
    return missing


def fmt(p: Promise, ctx: Context | None = None) -> str:
    name = ctx.describe(p.target) if ctx else f"Ch {p.target}"
    tgt = name + (f" §{p.target_section:02d}" if p.target_section else "")
    return f"{p.file}:{p.line}: → {tgt}: …{p.text}…"


def _target_id(ctx, arg: str, sources):
    """--for: an atlas id, or a chapter number of the (one) volume being read."""
    if not arg.isdigit():
        return arg
    vols = [v for _, v, _ in sources if v is not None]
    if len(vols) == 1:
        return ctx.chapter_id(vols[0], int(arg))
    if ctx.series:
        sys.exit("--for N needs a volume (--book DIR); at the root give an atlas id (--for F2.1)")
    return arg


def main(argv=None) -> int:
    argv = series_mod.enter_book(argv)
    ap = argparse.ArgumentParser(description="List forward promises (prose pointers without "
                                             "@ref) and reconcile them with STATUS.md.")
    series_mod.add_book_arg(ap)
    ap.add_argument("--src", help="source directory of a plain book (default: the volume's src, "
                                  "or every volume's at the repository root)")
    ap.add_argument("--status", help="STATUS.md path (default: authoring/STATUS.md, the "
                                     "volume's or the repository's)")
    ap.add_argument("--for", dest="target", metavar="CH",
                    help="only the promises chapter CH must pay (atlas id, or a chapter number "
                         "of this volume)")
    ap.add_argument("--reconcile", action="store_true",
                    help="list promises with no STATUS row; exit 1 if any")
    args = ap.parse_args(argv)

    ctx = Context()
    if args.src:
        here = Path(args.src).resolve().parent
        v = ctx.series.volume_at(here) if ctx.series else None
        if v is None:
            ctx = Context(series_mod.Series({}))      # a plain book: chapters by number
        sources = [(Path(args.src), v, f"{v.prefix}/" if v else "")]
    else:
        sources = volume_sources(ctx)
        if all(v is None for _, v, _ in sources):
            ctx = Context(series_mod.Series({}))
    status = Path(args.status) if args.status else series_mod.shared(str(STATUS))

    promises, sections = [], set()
    for src, vol, label in sources:
        promises += find_promises(src, ctx, vol, label)
        sections |= existing_sections(src, ctx, vol)
    rows = parse_status(status) if status.exists() else []

    if args.target is not None:
        tid = _target_id(ctx, args.target, sources)
        mine = [p for p in promises if p.target == tid]
        print(f"{ctx.describe(tid)} must pay {len(mine)} prose promise(s):")
        for p in mine:
            print("  " + fmt(p, ctx))
        status_rows = [r for r in rows if tid in r.targets]
        print(f"\nSTATUS.md rows targeting {tid}: {len(status_rows)}")
        for r in status_rows:
            print(f"  {'[paid] ' if r.paid else ''}{r.source}")
        return 0

    if args.reconcile:
        missing = reconcile(promises, rows, sections, ctx)
        for p, why in missing:
            print(f"{fmt(p, ctx)}\n    {why}")
        print(f"\n{len(promises)} promise(s) in the prose, {len(rows)} STATUS row(s), "
              f"{len(missing)} promise(s) not recorded.")
        return 1 if missing else 0

    by_target = defaultdict(list)
    for p in promises:
        by_target[p.target].append(p)
    for t in sorted(by_target, key=ctx.order):
        print(f"{ctx.describe(t)} ({len(by_target[t])}):")
        for p in by_target[t]:
            print("  " + fmt(p, ctx))
    print(f"\n{len(promises)} forward promise(s) to {len(by_target)} chapter(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
