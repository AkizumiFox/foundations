#!/usr/bin/env python3
"""Renumber chapters and sections: one simultaneous map, applied once to every prose pointer.

When a volume's chapters or sections move (a chapter inserted, sections renumbered), the
hand-written pointers into it must follow: "Chapter 5" in its own text, "*Logic and Proof*,
Section 4.11" in another volume's. Applying old -> new replacements one after another chains
them (5 -> 6, then 6 -> 7, ...), so this tool reads the whole map first and rewrites each
pointer exactly once, from the original text.

The map is JSON, one entry per volume prefix (authoring/series.json):

    {"fd1": {
        "chapters": {"5": "6"},
        "sections": {"3.5": "3.6", "3.6": "3.7", "4.11": "?", "4.12": "5.5"},
        "moves": {"src/ch05-from-derivations-to-prose": "src/ch06-from-derivations-to-prose",
                  "src/ch04-predicate-logic/12-first-order-soundness.md":
                      "src/ch05-models-and-theories/05-first-order-soundness.md"}}}

* `chapters`: "Chapter N" -> "Chapter M". A section of a mapped chapter follows it ("Section
  5.3" -> "Section 6.3") unless `sections` names it.
* `sections`: "Section N.M" -> "Section P.Q".
* "?" as a new number: the pointer needs reading by hand (old 4.11 became 5.1 or 5.2,
  depending on what it names). It is reported and left as it is.
* `moves`: files and directories of the volume to move (paths relative to the volume),
  with `git mv` when the volume is in a git work tree. Every mention of a moved path is
  rewritten in the same pass: a directory's name (`ch05-from-derivations-to-prose`) and a
  file's directory/stem (`ch04-predicate-logic/12-first-order-soundness`, so `.md` and
  `.html` links both follow).

What is rewritten, in the `src/` (.md), `authoring/` (.md, .yaml, .yml) and
`config/config.json` of every volume of authoring/series.json that is checked out, and in
each repository's root `authoring/`:

* a pointer inside the volume's own files: "Chapter N", "Chapters N–M", "Section N.M",
  "Sections N.M and P.Q" (lists joined by ",", "and", "or", "to", "–", "-");
* a pointer from anywhere into a mapped volume, prefixed by its title, italic or not:
  "*Logic and Proof*, Chapter N", "Logic and Proof, Sections 4.9–4.10";
* moved paths, as above.

Reported but never changed (each with "review"):

* a "?" entry;
* a plain pointer in another volume's file on a line that also names a mapped volume's
  title ("*Logic and Proof*, Section 4.11 and Section 4.12": the second may be fd1's);
* a hand-written numbered result ("Theorem 4.11.2") whose section is mapped.

    python3 tools/renumber.py MAP.json --dry-run     # the diff and the report; writes nothing
    python3 tools/renumber.py MAP.json               # rewrite, move, report
    python3 tools/renumber.py MAP.json --exclude 'authoring/pilot-archive/*'

Exits 0; with --check, exits 1 if anything would change (a gate after the sweep).
"""
import argparse
import difflib
import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import series as series_mod  # noqa: E402

REVIEW = "?"
NUM = r"\d+(?:\.\d+)?(?![.\d]*\d)"
SEP = r"\s*(?:,\s*(?:and\s+|or\s+)?|–|—|-|\s(?:and|or|to)\s)\s*"
LIST = rf"{NUM}(?:{SEP}{NUM})*"
KIND = r"(?:Chapter|Section)s?"
RESULT = (r"\b(?:Theorem|Lemma|Proposition|Corollary|Definition|Example|Exercise|Axiom|Remark|"
          r"Rule)\s+(\d+)\.(\d+)\.\d+\b")
SCAN = {"src": ("*.md",), "authoring": ("*.md", "*.yaml", "*.yml"), "config": ("config.json",)}


@dataclass
class VolumeMap:
    prefix: str
    title: str
    root: Path | None
    chapters: dict = field(default_factory=dict)
    sections: dict = field(default_factory=dict)
    moves: dict = field(default_factory=dict)

    def chapter(self, n: str) -> str:
        return self.chapters.get(n, n)

    def section(self, s: str) -> str:
        if s in self.sections:
            return self.sections[s]
        c, m = s.split(".")
        new = self.chapters.get(c)
        if new is None:
            return s
        return REVIEW if new == REVIEW else f"{new}.{m}"

    def maps_section(self, s: str) -> bool:
        return self.section(s) != s


@dataclass
class Hit:
    path: Path
    line: int
    old: str
    new: str            # "" for a review hit
    note: str = ""

    def __str__(self):
        if self.new:
            return f"{self.path}:{self.line}: {self.old!r} -> {self.new!r}{f' ({self.note})' if self.note else ''}"
        return f"{self.path}:{self.line}: review {self.old!r}: {self.note}"


def load_map(path: Path, series) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    maps = {}
    for prefix, entry in data.items():
        if prefix.startswith("_"):
            continue
        vol = series.by_prefix.get(prefix)
        if vol is None:
            raise SystemExit(f"renumber: {prefix} is not a volume of {series.repo / 'authoring/series.json'}")
        maps[prefix] = VolumeMap(prefix, vol.title, series.volume_dir(prefix),
                                 {str(k): str(v) for k, v in entry.get("chapters", {}).items()},
                                 {str(k): str(v) for k, v in entry.get("sections", {}).items()},
                                 dict(entry.get("moves", {})))
        for key in maps[prefix].sections:
            if not re.fullmatch(r"\d+\.\d+", key):
                raise SystemExit(f"renumber: {prefix} section {key!r} is not N.M")
    return maps


def title_pattern(title: str) -> str:
    """The title as the prose writes it: italic or not, any run of spaces."""
    words = [re.escape(w) for w in title.split()]
    return r"\*?" + r"\s+".join(words) + r"\*?"


def path_tokens(maps: dict) -> dict:
    """old token -> new token for the moved paths (file tokens before directory ones)."""
    files, dirs = {}, {}
    for vm in maps.values():
        for old, new in vm.moves.items():
            o, n = Path(old), Path(new)
            if o.suffix:
                files[f"{o.parent.name}/{o.stem}"] = f"{n.parent.name}/{n.stem}"
            elif o.name != n.name:
                dirs[o.name] = n.name
    return {**files, **dirs}


class Renumberer:
    def __init__(self, maps: dict, volumes: dict):
        """`maps`: prefix -> VolumeMap; `volumes`: prefix -> (title, root) for every volume."""
        self.maps = maps
        self.volumes = volumes
        self.tokens = path_tokens(maps)
        # every volume's title: a pointer into an unmapped volume must not be read as local
        self.titles = {p: t for p, (t, _) in volumes.items()}
        for p, vm in maps.items():
            self.titles.setdefault(p, vm.title)
        titled = "|".join(f"(?P<t_{p}>{title_pattern(t)})"
                          for p, t in sorted(self.titles.items(), key=lambda x: -len(x[1])))
        parts = []
        if titled:
            parts.append(rf"(?P<titled>(?:{titled})(?:\]\([^)]*\))?,?\s+(?P<tkind>{KIND})\s+(?P<tlist>{LIST}))")
        parts.append(rf"(?P<plain>\b(?P<kind>{KIND})\s+(?P<list>{LIST}))")
        if self.tokens:
            alts = "|".join(re.escape(t) for t in sorted(self.tokens, key=len, reverse=True))
            parts.append(rf"(?P<path>(?<![\w-])(?:{alts})(?![\w-]))")
        parts.append(rf"(?P<result>{RESULT})")
        self.pattern = re.compile("|".join(parts))
        self.title_res = {p: re.compile(title_pattern(vm.title)) for p, vm in maps.items()}

    def map_list(self, vm: VolumeMap, kind: str, text: str):
        """(new text, [review items]) for the list after "Chapter(s)"/"Section(s)"; the list
        stops at the first item of the wrong shape (a chapter with a dot, a section without),
        which is left as written."""
        pieces = re.split(rf"({SEP})", text)
        section = kind.startswith("Section")
        plural = kind.endswith("s")
        out, review, rest = [], [], ""
        for i in range(0, len(pieces), 2):
            item = pieces[i]
            # a singular kind takes one item or a range ("Chapter 4, 3 examples": just 4)
            bad_sep = i and not plural and pieces[i - 1].strip() not in ("–", "—", "-")
            if ("." in item) != section or bad_sep:
                rest = "".join(pieces[i - 1 if i else 0:])
                if i:
                    out.pop()
                break
            new = vm.section(item) if section else vm.chapter(item)
            if new == REVIEW:
                review.append(item)
                new = item
            out.append(new)
            if i + 1 < len(pieces):
                out.append(pieces[i + 1])
        return "".join(out) + rest, review

    def rewrite(self, text: str, path: Path, own: str | None):
        """(new text, hits) for one file of volume `own` (None: a repository's root files)."""
        hits = []
        line_starts = [0] + [m.end() for m in re.finditer("\n", text)]

        def lineno(pos):
            lo, hi = 0, len(line_starts)
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                lo, hi = (mid, hi) if line_starts[mid] <= pos else (lo, mid)
            return lo + 1

        def line_text(pos):
            n = lineno(pos)
            end = line_starts[n] if n < len(line_starts) else len(text)
            return text[line_starts[n - 1]:end]

        def sub(m):
            old = m.group(0)
            titled = m.groupdict().get("titled")
            if titled or m.group("plain") is not None:
                if titled:
                    prefix = next(p for p in self.titles if m.group(f"t_{p}"))
                    if prefix not in self.maps:
                        return old
                    kind, lst = m.group("tkind"), m.group("tlist")
                    head = old[:m.start("tlist") - m.start()]
                else:
                    prefix = own
                    kind, lst = m.group("kind"), m.group("list")
                    head = old[:m.start("list") - m.start()]
                    for p, rx in self.title_res.items():   # a pointer that may belong to p
                        if p == own:
                            continue
                        vm = self.maps[p]
                        items = re.findall(NUM, lst)
                        if any((vm.section(x) if "." in x else vm.chapter(x)) != x for x in items) \
                                and rx.search(line_text(m.start())):
                            hits.append(Hit(path, lineno(m.start()), old, "",
                                            f"a plain pointer on a line naming {vm.title}; "
                                            f"if it points into {p}, rewrite it by hand"))
                    if own not in self.maps:
                        return old
                vm = self.maps[prefix]
                new_list, review = self.map_list(vm, kind, lst)
                for item in review:
                    hits.append(Hit(path, lineno(m.start()), old, "",
                                    f"{prefix} {kind.rstrip('s').lower()} {item} is mapped to '?': read it"))
                new = head + new_list
                if new != old:
                    hits.append(Hit(path, lineno(m.start()), old, new, prefix if prefix != own else ""))
                return new
            if m.groupdict().get("path") is not None:
                new = self.tokens[old]
                hits.append(Hit(path, lineno(m.start()), old, new, "moved path"))
                return new
            if m.group("result") is not None:
                c, s = re.search(r"(\d+)\.(\d+)\.\d+", old).groups()
                pre = text[max(0, m.start() - 60):m.start()]
                for p, vm in self.maps.items():
                    if (p == own or self.title_res[p].search(pre)) and vm.maps_section(f"{c}.{s}"):
                        hits.append(Hit(path, lineno(m.start()), old, "",
                                        f"a hand-written number in {p} section {c}.{s}, which moves; "
                                        f"use a label reference"))
                        break
            return old

        return self.pattern.sub(sub, text), hits


def files_of(root: Path, exclude=()):
    for sub, globs in SCAN.items():
        base = root / sub
        if not base.is_dir():
            continue
        for g in globs:
            for f in sorted(base.rglob(g)):
                rel = f.relative_to(root).as_posix()
                if not any(fnmatch.fnmatch(rel, x) for x in exclude):
                    yield f


def targets(series, exclude=()):
    """[(file, own prefix or None)] for every volume that is checked out and every
    repository's root authoring/."""
    out, roots = [], set()
    for v in series.volumes:
        vdir = series.volume_dir(v.prefix)
        if vdir is None:
            continue
        out += [(f, v.prefix) for f in files_of(vdir, exclude)]
        roots.add(vdir.parent)
    for repo in sorted(roots):
        base = repo / "authoring"
        if base.is_dir():
            out += [(f, None) for g in SCAN["authoring"] for f in sorted(base.rglob(g))
                    if not any(fnmatch.fnmatch(f.relative_to(repo).as_posix(), x) for x in exclude)]
    return out


def in_git(path: Path) -> bool:
    return subprocess.run(["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
                          capture_output=True, text=True).returncode == 0


def apply_moves(maps: dict, dry_run: bool, log=print):
    """Move every file and directory of the maps at once: first each to a temporary name,
    then to its target, so a target may be another move's source."""
    plan = []
    for vm in maps.values():
        for old, new in vm.moves.items():
            src, dst = vm.root / old, vm.root / new
            if not src.exists():
                raise SystemExit(f"renumber: {vm.prefix}: {old} does not exist")
            plan.append((src, dst))
    for src, dst in plan:
        log(f"move {src} -> {dst}")
    if dry_run or not plan:
        return
    staged = []
    for n, (src, dst) in enumerate(plan):
        tmp = src.with_name(f".renumber-{n}-{src.name}")
        _move(src, tmp)
        staged.append((tmp, dst))
    for tmp, dst in staged:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            raise SystemExit(f"renumber: {dst} exists")
        _move(tmp, dst)


def _move(src: Path, dst: Path):
    if in_git(src.parent):
        r = subprocess.run(["git", "-C", str(src.parent), "mv", str(src), str(dst)],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return
    os.rename(src, dst)


def run(map_path, dry_run=False, series_path=None, exclude=(), out=print):
    """Apply the map; return (hits, changed files, diff text)."""
    series = series_mod.Series.load(series_path)
    maps = load_map(map_path, series)
    volumes = {v.prefix: (v.title, series.volume_dir(v.prefix)) for v in series.volumes}
    r = Renumberer(maps, volumes)
    hits, changed, diff = [], [], []
    for f, own in targets(series, exclude):
        text = f.read_text(encoding="utf-8")
        new, h = r.rewrite(text, f, own)
        hits += h
        if new != text:
            changed.append(f)
            diff += difflib.unified_diff(text.splitlines(True), new.splitlines(True),
                                         str(f), str(f) + " (renumbered)")
            if not dry_run:
                f.write_text(new, encoding="utf-8")
    apply_moves(maps, dry_run, log=out)
    return hits, changed, "".join(diff)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Apply a simultaneous chapter/section renumbering "
                                             "map to every prose pointer, once.")
    ap.add_argument("map", help="the JSON map (see the module docstring)")
    ap.add_argument("--dry-run", action="store_true", help="print the diff and the report; write nothing")
    ap.add_argument("--check", action="store_true", help="like --dry-run, and exit 1 if anything would change")
    ap.add_argument("--series", help="authoring/series.json to read (default: this repository's)")
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                    help="skip files whose path (relative to the volume or repository) matches")
    args = ap.parse_args(argv)
    dry = args.dry_run or args.check
    hits, changed, diff = run(args.map, dry_run=dry, series_path=args.series, exclude=args.exclude)
    if dry and diff:
        print(diff)
    for h in hits:
        print(h)
    rewrites = sum(1 for h in hits if h.new)
    reviews = len(hits) - rewrites
    print(f"\n{rewrites} pointer(s) {'to rewrite' if dry else 'rewritten'} in {len(changed)} file(s); "
          f"{reviews} to review by hand.")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
