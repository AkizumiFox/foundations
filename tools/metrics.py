#!/usr/bin/env python3
"""Per-chapter process metrics (research-production §7.1), appended to authoring/metrics.csv.

`authoring/PIPELINE.md` records, for every chapter, its size, its findings by stage
and severity, the escape rate, referee recall on seeded errors, its dependency
bookkeeping, its hygiene counts and its cost. This tool computes each of those from
whatever exists, and appends one row per chapter to `authoring/metrics.csv`
(created, with its header, on first use). Every source is optional; a missing one
leaves its columns blank and is named in the row's `notes` column:

* **the source** (`src/chNN-*/`): prose words per section against the 2,500-5,000
  budget (`tools/check_structure.py`'s count), results, proofs, examples,
  exercises, % of exercises followed by a solution, exit checks
  (`[C…: Exit check: …]`), Quick checks, dependency-ledger lines and those whose
  source is `(promised)`;
* **the claim ledger** (`authoring/ledger/chNN.yaml`, via `tools/ledger.py`; needs
  PyYAML, so run this tool with `.venv/bin/python` to get these columns): every
  verdict by stage and severity, and stale verdicts;
* **review reports** (`authoring/reviews/chNN-S<stage>*.md`): each table row's
  Verdict, counted under the stage in the file name (used for a stage the ledger
  has no verdicts for);
* findings per 10k prose words; the **escape rate** (errors found at S8, S9 or
  later, over all errors); **blueprint defects** (non-`correct` S2 findings);
* **seeded recall** (`authoring/reviews/chNN-seeded*.json`, from
  `tools/seed_errors.py score --json`);
* **the gates**: `tools/check_structure.py`, `check_fitch.py`, `check_numbers.py`
  (sidecars are not run; `--run-sidecars` runs them), `check_notation.py`,
  `promises.py` (opened by this chapter, owed to it, and STATUS rows paid);
* **the build**: `_build/crossref_labels.json` (forward citations from proofs,
  results citing an exercise), `_build/html/chNN-*/` (`check_rendered.py` hits),
  LaTeX logs naming the chapter (overfull boxes), and `./build.py check` output --
  from a saved log with `--check-log FILE`, or run with `--run-check` (it writes
  `_build/`, so never while another agent builds in this tree);
* **git**: commits touching the chapter directory, first and last commit dates;
* **cost** (agents, tokens, hours) cannot be read from anywhere: give it with
  `--set agents=21 --set tokens=7.2M --set hours=8`.

In a series split into volumes (tools/series.py) the tool works on one volume: run it in
the volume directory or pass `--book fd2`; chapter numbers are the volume's own, the
ledger and reviews are the volume's (`fd2/authoring/`), STATUS.md, NOTATION.md and
metrics.csv the repository's (`authoring/`), and the `chapter` column reads
`fd2/ch01-sets-and-functions`.

    python3 tools/metrics.py --book fd2 1          # append a row for fd2's Chapter 1 (F2.1)
    python3 tools/metrics.py 10                    # append a row for Chapter 10
    .venv/bin/python tools/metrics.py              # every chapter, with ledger columns
    python3 tools/metrics.py 10 --dry-run          # print the row, write nothing
    python3 tools/metrics.py 10 --set agents=19 --check-log /tmp/check.txt

Importable: `chapter_metrics(chapter_dir, ...) -> dict`, `COLUMNS`.
"""
import argparse
import csv
import datetime
import importlib.util
import io
import json
import re
import subprocess
import sys
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

TOOLS = Path(__file__).resolve().parent
SRC = Path("src")
CSV = Path("authoring/metrics.csv")
WORDS_MIN, WORDS_MAX = 2500, 5000
SEVERITIES = ("minor", "gap", "error")
STAGES = ("S2", "S5a", "S5b", "S5", "S6", "S8", "S9")
LATE_STAGES = ("S8", "S9", "S10", "later")
RESULT_KINDS = ("thm", "lem", "cor", "prp", "ax")
EXIT_CHECK = re.compile(r"^\[C\d*:\s*Exit check", re.I)
PROMISED = re.compile(r"\(promised\)")

COLUMNS = [
    "date", "commit", "chapter",
    # size
    "sections", "prose_words", "words_per_section", "sections_outside_budget",
    "results", "proofs", "examples", "exercises", "exercise_solution_pct", "exit_checks",
    "quick_checks",
    # findings
    *[f"{st}_{sev}" for st in STAGES for sev in SEVERITIES],
    "findings_total", "errors_total", "findings_per_10k", "errors_per_10k",
    "escape_rate", "blueprint_defects_s2", "seeded_recall",
    # dependencies
    "forward_citations", "results_citing_exercises", "ledger_lines", "ledger_promised",
    "promises_opened", "promises_owed", "promises_paid",
    # hygiene
    "structure_fatal", "structure_advisory", "fitch_errors", "numbers_fatal",
    "numbers_advisory", "notation_advisories", "rendered_hits", "overfull_boxes",
    "stale_verdicts", "check_errors", "check_warnings",
    # git and cost
    "commits", "first_commit", "last_commit", "agents", "tokens", "hours",
    "notes",
]


def _tool(name):
    """A book tool (tools/), else an engine tool ($BOOK_ENGINE/tools or the submodule's)."""
    path = TOOLS / f"{name}.py"
    if not path.exists():
        import os
        engine = Path(os.environ.get("BOOK_ENGINE") or TOOLS.parent / "engine").expanduser()
        path = engine / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def chapter_number(chdir: Path):
    m = re.match(r"ch(\d+)", Path(chdir).name)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------

def size_metrics(chdir: Path) -> dict:
    cs = _tool("check_structure")
    words, outside, per = 0, 0, []
    counts = Counter()
    ex_with_solution = 0
    ledger_lines = promised = 0
    sections = sorted(Path(chdir).glob("[0-9]*.md"))
    for f in sections:
        text = f.read_text(encoding="utf-8")
        w = cs.prose_words(text)
        words += w
        per.append(f"{f.name[:2]}:{w}")
        outside += not (WORDS_MIN <= w <= WORDS_MAX)
        doc = mdblocks.parse(text)
        for d in doc.divs:
            kind = d.id.split("-", 1)[0] if d.id and "-" in d.id else ""
            if kind in RESULT_KINDS:
                counts["results"] += 1
            elif kind == "exm":
                counts["examples"] += 1
            elif kind == "exr":
                counts["exercises"] += 1
                ex_with_solution += cs.solution_after(doc, d) is not None
                j = mdblocks.next_nonblank(doc.lines, d.start)
                if 0 <= j < d.end and EXIT_CHECK.match(doc.lines[j].strip()):
                    counts["exit_checks"] += 1
            if d.has("proof"):
                counts["proofs"] += 1
            if d.has("check"):
                counts["quick_checks"] += 1
        m = re.search(r"<!-- dependency ledger[ \t]*\n(.*?)-->", text, flags=re.S)
        if m:
            lines = [ln for ln in m.group(1).split("\n") if ln.strip()]
            ledger_lines += sum(1 for ln in lines if not ln.strip().startswith("none:"))
            promised += sum(1 for ln in lines if PROMISED.search(ln))
    ex = counts["exercises"]
    return {"sections": len(sections), "prose_words": words, "words_per_section": " ".join(per),
            "sections_outside_budget": outside, "results": counts["results"],
            "proofs": counts["proofs"], "examples": counts["examples"], "exercises": ex,
            "exercise_solution_pct": round(100 * ex_with_solution / ex, 1) if ex else "",
            "exit_checks": counts["exit_checks"], "quick_checks": counts["quick_checks"],
            "ledger_lines": ledger_lines, "ledger_promised": promised}


def _severity(text: str):
    t = re.sub(r"[*_`]", "", text).strip().lower()
    for v in ("correct",) + SEVERITIES:
        if t.startswith(v):
            return v
    return None


def review_findings(reviews: Path, ch: int) -> Counter:
    """Counter{(stage, severity)} from the tables of authoring/reviews/chNN-S*.md."""
    out = Counter()
    for f in sorted(Path(reviews).glob(f"ch{ch:02d}-S*.md")):
        m = re.match(rf"ch{ch:02d}-(S\d+)(?:-?([AaBb])(?![a-z]))?", f.name)   # S5a, S5-A, S5B
        stage = m.group(1) + (m.group(2) or "").lower()
        col = None
        for line in f.read_text(encoding="utf-8").split("\n"):
            s = line.strip()
            if not s.startswith("|"):
                col = None
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            lowered = [c.lower() for c in cells]
            if "verdict" in lowered:
                col = lowered.index("verdict")
                continue
            if col is not None and col < len(cells):
                sev = _severity(cells[col])
                if sev in SEVERITIES:
                    out[(stage, sev)] += 1
    return out


def ledger_findings(ledger_dir: Path, ch: int, chdir: Path):
    """(Counter{(stage, severity)}, stale count), or raises if unavailable."""
    path = Path(ledger_dir) / f"ch{ch:02d}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"no {path}")
    import yaml  # noqa: F401  (ImportError is reported by the caller)
    lg = _tool("ledger")
    data = lg.load(path)
    out = Counter()
    for e in data.get("items", []):
        for v in e.get("verdicts", []) or []:
            if v.get("verdict") in SEVERITIES:
                out[(str(v.get("stage", "?")), v["verdict"])] += 1
    stale = len(lg.stale_items(data, lg.extract_items(chdir)))
    return out, stale


def _stage_key(stage: str) -> str:
    s = stage.upper().replace("S5A", "S5a").replace("S5B", "S5b")
    s = re.sub(r"^S2[AB]$", "S2", s)
    return s if s in STAGES else ("S9" if s.startswith(("S9", "S10")) else s)


def findings_metrics(counts: Counter, words: int) -> dict:
    row = {f"{st}_{sev}": 0 for st in STAGES for sev in SEVERITIES}
    for (stage, sev), n in counts.items():
        key = f"{_stage_key(stage)}_{sev}"
        if key in row:
            row[key] += n
    total = sum(counts.values())
    errors = sum(n for (st, sev), n in counts.items() if sev == "error")
    late = sum(n for (st, sev), n in counts.items()
               if sev == "error" and _stage_key(st) in LATE_STAGES)
    row.update({
        "findings_total": total, "errors_total": errors,
        "findings_per_10k": round(total * 10000 / words, 2) if words else "",
        "errors_per_10k": round(errors * 10000 / words, 2) if words else "",
        "escape_rate": round(late / errors, 3) if errors else "",
        "blueprint_defects_s2": sum(n for (st, sev), n in counts.items() if _stage_key(st) == "S2"),
    })
    return row


def seeded_recall(reviews: Path, ch: int):
    files = sorted(Path(reviews).glob(f"ch{ch:02d}-seed*.json"))
    if not files:
        raise FileNotFoundError("no seeded-error score")
    data = json.loads(files[-1].read_text(encoding="utf-8"))
    return data.get("recall", "")


def labels_metrics(crossref: Path, chdir: Path) -> dict:
    data = json.loads(Path(crossref).read_text(encoding="utf-8"))
    labels = data.get("crossref_labels", data)
    fd = _tool("check_forward_deps")
    name = Path(chdir).name + "/"
    fwd = [v for v in fd.find_violations(labels) if (v[1] or "").startswith(name)]
    rce = sum(1 for lab, rec in labels.items()
              if (rec.get("file") or "").startswith(name)
              and rec.get("type") in fd.RESULT_TYPES
              and any(c.startswith("exr-") for c in rec.get("uses") or ()))
    return {"forward_citations": len(fwd), "results_citing_exercises": rce}


def promise_metrics(src: Path, status: Path, ch: int, root: Path = Path(".")) -> dict:
    """Promises opened by chapter `ch` of the book at `root`, owed to it (by this volume's
    prose), and STATUS rows paid to it. Chapters are compared by atlas id in a series."""
    pr = _tool("promises")
    ctx = pr.Context()
    vol = ctx.series.volume_at(Path(root)) if ctx.series else None
    cid = ctx.chapter_id(vol, ch)
    ps = pr.find_promises(src, ctx, vol)
    rows = pr.parse_status(status) if Path(status).exists() else []
    return {"promises_opened": sum(1 for p in ps if p.chapter == cid and p.target != cid),
            "promises_owed": sum(1 for p in ps if p.target == cid and p.chapter != cid),
            "promises_paid": sum(1 for r in rows if cid in r.targets and r.paid)}


def gate_metrics(chdir: Path, src: Path, root: Path, run_sidecars: bool) -> tuple:
    row, notes = {}, []
    ch = chapter_number(chdir)
    try:
        fa, ad = _tool("check_structure").find_violations(chdir)
        row.update(structure_fatal=len(fa), structure_advisory=len(ad))
    except Exception as e:  # noqa: BLE001 -- a broken tool must not stop the row
        notes.append(f"check_structure: {e}")
    try:
        errs, _, _ = _tool("check_fitch").find_violations(chdir)
        row["fitch_errors"] = len(errs)
    except Exception as e:  # noqa: BLE001
        notes.append(f"check_fitch: {e}")
    try:
        verify = root / "verify"
        if (verify / f"ch{ch:02d}").is_dir() or run_sidecars:
            fa, ad = _tool("check_numbers").find_violations(verify, src, {ch}, run=run_sidecars,
                                                            root=root)
            row.update(numbers_fatal=len(fa), numbers_advisory=len(ad))
        else:
            fa, ad = _tool("check_numbers").find_violations(verify, src, {ch}, run=False, root=root)
            row.update(numbers_fatal=len(fa), numbers_advisory=len(ad))
            notes.append("no verify/ dir")
    except Exception as e:  # noqa: BLE001
        notes.append(f"check_numbers: {e}")
    try:
        cn = _tool("check_notation")
        config = root / "config/config.json"
        items = cn.find_violations(src, series.shared("authoring/NOTATION.md", root),
                                   cn.macros_from_config(config), cn.parts_from_config(config))
        row["notation_advisories"] = sum(1 for p, _, _ in items if Path(p).parent.name == chdir.name)
    except Exception as e:  # noqa: BLE001
        notes.append(f"check_notation: {e}")
    return row, notes


def build_metrics(chdir: Path, root: Path) -> tuple:
    row, notes = {}, []
    html = root / "_build" / "html" / chdir.name
    if html.is_dir():
        cr = _tool("check_rendered")
        row["rendered_hits"] = sum(len(cr.lint_html(p.read_text(encoding="utf-8")))
                                   for p in sorted(html.glob("*.html")))
    else:
        notes.append("no HTML build")
    logs = [p for p in (root / "_build" / "tmp").rglob("*.log") if chdir.name in str(p)] \
        if (root / "_build" / "tmp").is_dir() else []
    if logs:
        cr = _tool("check_rendered")
        row["overfull_boxes"] = sum(len(cr.scan_log(p.read_text(encoding="latin-1"))[1]) for p in logs)
    else:
        notes.append("no LaTeX logs")
    return row, notes


def check_output_metrics(text: str, chdir: Path) -> dict:
    lines = [ln for ln in text.split("\n") if chdir.name in ln]
    return {"check_errors": sum(1 for ln in lines if "✖" in ln or "error" in ln.lower()[:12]),
            "check_warnings": sum(1 for ln in lines if "⚠" in ln or "warning" in ln.lower()[:12])}


def git_metrics(chdir: Path, root: Path) -> dict:
    r = subprocess.run(["git", "log", "--format=%cs", "--", str(chdir)], cwd=root,
                       capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise RuntimeError("git log failed")
    dates = r.stdout.split()
    return {"commits": len(dates), "first_commit": dates[-1] if dates else "",
            "last_commit": dates[0] if dates else ""}


def head_commit(root: Path) -> str:
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True,
                           text=True, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


# ---------------------------------------------------------------------------
# One row
# ---------------------------------------------------------------------------

def chapter_metrics(chdir: Path, root: Path = Path("."), src: Path = SRC, check_output: str | None = None,
                    run_sidecars: bool = False, manual: dict | None = None) -> dict:
    """The metrics row for one chapter directory; columns it cannot fill are ''."""
    root, chdir, src = Path(root), Path(chdir), Path(src)
    ch = chapter_number(chdir)
    row = {c: "" for c in COLUMNS}
    notes = []
    s = series.Series.load()
    vol = s.volume_at(root) if s else None
    row.update(date=datetime.date.today().isoformat(), commit=head_commit(root),
               chapter=f"{vol.prefix}/{chdir.name}" if vol else chdir.name)
    row.update(size_metrics(chdir))

    counts = Counter()
    ledger_stages = set()
    try:
        lc, stale = ledger_findings(root / "authoring" / "ledger", ch, chdir)
        counts.update(lc)
        ledger_stages = {_stage_key(st) for st, _ in lc}
        row["stale_verdicts"] = stale
    except ImportError:
        notes.append("ledger needs PyYAML (.venv/bin/python)")
    except Exception as e:  # noqa: BLE001
        notes.append(f"ledger: {e}")
    reviews = root / "authoring" / "reviews"
    rc = review_findings(reviews, ch) if reviews.is_dir() else Counter()
    for (st, sev), n in rc.items():
        if _stage_key(st) not in ledger_stages:
            counts[(st, sev)] += n
    if not counts and not rc:
        notes.append("no findings recorded")
    row.update(findings_metrics(counts, row["prose_words"]))
    try:
        row["seeded_recall"] = seeded_recall(reviews, ch)
    except Exception as e:  # noqa: BLE001
        notes.append(f"seeded recall: {e}")

    crossref = root / "_build" / "crossref_labels.json"
    try:
        row.update(labels_metrics(crossref, chdir))
    except Exception as e:  # noqa: BLE001
        notes.append(f"crossref: {e.__class__.__name__}")
    try:
        row.update(promise_metrics(src, series.shared("authoring/STATUS.md", root), ch, root))
    except Exception as e:  # noqa: BLE001
        notes.append(f"promises: {e}")
    g, n = gate_metrics(chdir, src, root, run_sidecars)
    row.update(g)
    notes += n
    b, n = build_metrics(chdir, root)
    row.update(b)
    notes += n
    if check_output is not None:
        row.update(check_output_metrics(check_output, chdir))
    else:
        notes.append("no ./build.py check output")
    try:
        row.update(git_metrics(chdir, root))
    except Exception as e:  # noqa: BLE001
        notes.append(f"git: {e}")
    for k, v in (manual or {}).items():
        row[k] = v
    row["notes"] = "; ".join(notes)
    return row


def append_rows(path: Path, rows: list):
    """Append rows to the CSV, creating it with the header. An existing file keeps its header."""
    path = Path(path)
    header = COLUMNS
    if path.exists() and path.stat().st_size:
        with path.open(newline="", encoding="utf-8") as fh:
            header = next(csv.reader(fh), COLUMNS)
        new = True
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        new = False
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=header, extrasaction="ignore")
        if not new:
            w.writeheader()
        for r in rows:
            w.writerow(r)
    return [c for c in COLUMNS if c not in header]


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(description="Compute per-chapter process metrics and append them "
                                             "to authoring/metrics.csv.")
    series.add_book_arg(ap)
    ap.add_argument("chapters", nargs="*", type=int, help="chapter numbers (default: every chapter in src)")
    ap.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    ap.add_argument("--csv", default=None,
                    help="output CSV (default: authoring/metrics.csv, the book's or the repository's)")
    ap.add_argument("--dry-run", action="store_true", help="print the rows; write nothing")
    ap.add_argument("--check-log", help="saved output of ./build.py check")
    ap.add_argument("--run-check", action="store_true",
                    help="run ./build.py check (writes _build/: not while others build here)")
    ap.add_argument("--run-sidecars", action="store_true", help="run the verify/ sidecars too")
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE",
                    help="a manual column, e.g. agents=21, tokens=7.2M, hours=8 (repeatable)")
    args = ap.parse_args(argv)
    root = Path(".")
    src = Path(args.src)
    args.csv = args.csv or str(series.shared(str(CSV), root))
    manual = {}
    for kv in args.set:
        k, _, v = kv.partition("=")
        if k not in COLUMNS:
            sys.exit(f"unknown column {k!r}")
        manual[k] = v
    check_output = None
    if args.check_log:
        check_output = Path(args.check_log).read_text(encoding="utf-8", errors="replace")
    elif args.run_check:
        r = subprocess.run([sys.executable, "build.py", "check"], capture_output=True, text=True)
        check_output = r.stdout + r.stderr
    dirs = [d for d in sorted(src.glob("ch[0-9]*")) if d.is_dir()
            and (not args.chapters or chapter_number(d) in args.chapters)]
    if not dirs:
        sys.exit("no chapter directories found")
    rows = []
    for d in dirs:
        with redirect_stdout(io.StringIO()):
            rows.append(chapter_metrics(d, root, src, check_output, args.run_sidecars, manual))
    for r in rows:
        print(f"{r['chapter']}:")
        for c in COLUMNS:
            if r[c] not in ("", 0) or c in ("prose_words", "findings_total"):
                print(f"  {c}: {r[c]}")
    if not args.dry_run:
        missing = append_rows(Path(args.csv), rows)
        print(f"\nAppended {len(rows)} row(s) to {args.csv}.")
        if missing:
            print(f"Its header predates columns {', '.join(missing)}; they were not written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
