#!/usr/bin/env python3
"""Check each section file against the section contract of `authoring/STYLE.md`.

STYLE §2, §4, §5 and §6 describe the page every section must have. Most of it is
mechanical, so it is checked here rather than left to a referee's eye. Each rule is
either **fatal** (the section is not finished without it) or **advisory** (a
reminder worth a look, printed but never failing the run).

Section files (`src/chNN-slug/MM-slug.md`):

* fatal  -- an **opening frame**: prose after the `# Title` line and before the
  first `##` heading (STYLE §2);
* fatal  -- at least one **Quick check** `::: {.check}`, and each check is followed
  directly (next block, a sibling, not nested) by a `::: {.solution}` (STYLE §5);
* fatal  -- at least one `::: {.warning}` (STYLE §3 step 10, §9);
* fatal  -- a `## Exercises` heading followed by `### A.`, `### B.`, `### C.`
  headings in that order; an optional `### R.` group is allowed (STYLE §6);
* fatal  -- every `::: {#exr-...}` is followed directly by a `::: {.solution}`;
* advisory -- a proof longer than `--idea-lines` lines (default 3; a derivation or
  display counts as one line) has a `::: {.idea}` as the block before it (STYLE §4
  step 3); proofs nested in a claim are exempt;
* advisory -- prose word count in 2,500-5,000 (STYLE §2); math, code, raw LaTeX and
  markup are not counted;
* advisory -- a `###` heading under Exercises other than A/B/C/R, and an
  `### R. Review` group outside the chapter's last section (STYLE §6, §11.5);
* advisory -- the file ends with a **dependency ledger**, an HTML comment whose
  first line is `<!-- dependency ledger` and whose lines are
  `<label> (<kind>): <fact> | <source>` or `none: ...` (STYLE §9).

Hint rungs (STYLE §6, §11.7) are `::: {.solution}` blocks whose first line is
`[Hint 1]` / `[Hint 2]`, placed between an exercise and its solution. They are
skipped when looking for the exercise's solution: an exercise followed only by
hints has no solution.

A **Gate** section (its `# Title` contains "Gate"; STYLE §2, §11.10) has no
Exercises heading of its own -- its problems are the section -- so the Exercises and
A/B/C rules do not apply to it, and its check and warning rules are advisory.

A chapter's `index.md` is exempt from the section rules, but must have (fatal) its
**What you need**, **Roadmap** and **Named moves** parts, as a heading or as a bold
lead-in (STYLE §2); a missing **Time** line is advisory.

    python3 tools/check_structure.py                          # all of src/
    python3 tools/check_structure.py src/ch11-least-upper-bound
    python3 tools/check_structure.py --fatal-only             # hide advisories

Exits 1 if any fatal problem is found. Importable:

    from tools.check_structure import find_violations, report
    fatal, advisory = find_violations(Path("src"))

As a `./build.py check` plugin (config `checks`), `run(book, labels)` reports the fatal
rules as errors and the advisories as one summary warning. In a series, run it in a
volume directory or pass `--book fd2`.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

WORDS_MIN, WORDS_MAX = 2500, 5000
IDEA_LINES = 3
GROUPS = ("A", "B", "C")
INDEX_PARTS = ("What you need", "Roadmap", "Named moves")
INDEX_ADVISORY = ("Time",)
HINT = re.compile(r"^\[Hint\s*\d+\]")
LEDGER_LINE = re.compile(r"^(none:.*|[a-z]+-[\w-]+ \((proof|idea|claim|solution|example)\): .+\|.+)$")


def is_hint(doc, div) -> bool:
    j = mdblocks.next_nonblank(doc.lines, div.start)
    return div.has("solution") and 0 <= j < div.end and bool(HINT.match(doc.lines[j].strip()))


def solution_after(doc, div):
    """The first non-hint .solution following `div` (hint rungs skipped), or None."""
    nxt = mdblocks.following_div(doc, div)
    while nxt is not None and is_hint(doc, nxt):
        nxt = mdblocks.following_div(doc, nxt)
    return nxt if nxt is not None and nxt.has("solution") else None


def check_ledger(text: str):
    """Advisory problems with the closing dependency ledger."""
    m = re.search(r"<!-- dependency ledger[ \t]*\n(.*?)-->", text, flags=re.S)
    if not m:
        return [(len(text.split("\n")), "no dependency ledger (<!-- dependency ledger ... -->) at the end")]
    out = []
    first = text.count("\n", 0, m.start()) + 1
    if text[m.end():].strip():
        out.append((first, "the dependency ledger is not the last thing in the file"))
    for k, line in enumerate(m.group(1).split("\n")):
        if line.strip() and not LEDGER_LINE.match(line.strip()):
            out.append((first + 1 + k, f"dependency ledger line not '<label> (<kind>): <fact> | <source>': {line.strip()[:60]!r}"))
    return out


def prose_words(text: str) -> int:
    """Words of prose: math, code, raw LaTeX, div fences and markup removed."""
    doc = mdblocks.parse(text)
    kept = [ln for ln, code in zip(doc.lines, doc.in_code) if not code]
    t = "\n".join(kept)
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\\\(.*?\\\)", " X ", t, flags=re.S)       # inline math counts as a word
    t = re.sub(r"^:{3,}.*$", " ", t, flags=re.M)
    t = re.sub(r"`[^`]*`", " X ", t)
    t = re.sub(r"@[\w-]+", " X ", t)
    t = re.sub(r"[#*_>\[\]{}|]", " ", t)
    return len(re.findall(r"[A-Za-z0-9][\w'’-]*", t))


def proof_length(doc, div) -> int:
    """Lines of a proof: non-blank source lines, a code fence or display counting once."""
    n = 0
    i = div.start + 1
    in_display = False
    while i < div.end:
        line = doc.lines[i].strip()
        if doc.in_code[i]:
            if line.startswith("```") or line.startswith("~~~"):
                # count the whole fenced block once
                j = i + 1
                while j < div.end and not (doc.in_code[j] and doc.lines[j].strip().startswith(line[:3])):
                    j += 1
                n += 1
                i = j + 1
                continue
        elif line.startswith("\\["):
            in_display = not line.endswith("\\]") or line == "\\["
            n += 1
        elif in_display:
            if line.endswith("\\]") or line.startswith("\\]"):
                in_display = False
        elif line and not mdblocks.CLOSE.match(line) and not mdblocks.OPEN.match(line):
            n += 1
        i += 1
    return n


def check_section(text: str, idea_lines: int = IDEA_LINES, last: bool = True):
    """(fatal, advisory) for one section file: lists of (lineno, message).

    `last` says whether this is the chapter's last section (where R. Review belongs).
    """
    fatal, advisory = [], []
    doc = mdblocks.parse(text)
    lines = doc.lines
    title_text = next((t for _, lvl, t in doc.headings if lvl == 1), "")
    gate = "gate" in title_text.lower()
    soft = advisory if gate else fatal

    # opening frame
    first_h2 = next((i for i, lvl, _ in doc.headings if lvl == 2), len(lines))
    title = next((i for i, lvl, _ in doc.headings if lvl == 1), None)
    if title is None:
        fatal.append((1, "no `# Title` line"))
    start = (title + 1) if title is not None else 0
    frame = [lines[i] for i in range(start, first_h2)
             if lines[i].strip() and not doc.in_code[i]
             and not mdblocks.OPEN.match(lines[i]) and not mdblocks.CLOSE.match(lines[i])
             and not any(d.start < i < d.end for d in doc.divs)]
    if not frame:
        fatal.append((start + 1, "no opening frame: prose paragraph before the first ## heading"))

    # checks and their solutions
    checks = [d for d in doc.divs if d.has("check")]
    if not checks:
        soft.append((1, "no Quick check (::: {.check})"))
    for d in checks:
        if any(c.has("solution") for c in d.children):
            fatal.append((d.start + 1, "a .solution is nested inside the .check; put it after the check closes"))
        nxt = mdblocks.following_div(doc, d)
        if nxt is None or not nxt.has("solution") or nxt.parent is not d.parent:
            fatal.append((d.start + 1, "Quick check not followed by a sibling ::: {.solution}"))

    if not any(d.has("warning") for d in doc.divs):
        soft.append((1, "no ::: {.warning}"))

    # exercises
    ex = next((i for i, lvl, t in doc.headings if lvl == 2 and t.strip() == "Exercises"), None)
    if ex is None:
        if not gate:
            fatal.append((1, "no ## Exercises heading"))
    else:
        after = [(i, lvl, t) for i, lvl, t in doc.headings if i > ex]
        stop = next((i for i, lvl, _ in after if lvl <= 2), len(lines))
        groups = []
        for i, lvl, t in after:
            if i >= stop or lvl != 3:
                continue
            m = re.match(r"([A-Z])\.\s", t + " ")
            if m and m.group(1) in GROUPS + ("R",):
                groups.append((i, m.group(1)))
            else:
                advisory.append((i + 1, f"unexpected ### heading under Exercises: {t!r}"))
        letters = [g for _, g in groups if g in GROUPS]
        if any(g == "R" for _, g in groups) and not last:
            advisory.append((ex + 1, "### R. Review belongs in the chapter's last section only"))
        if letters != list(GROUPS) and not gate:
            fatal.append((ex + 1, f"Exercises groups must be ### A., ### B., ### C. in order "
                                  f"(found {', '.join(letters) or 'none'})"))
    for d in doc.divs:
        if d.id.startswith("exr-"):
            if solution_after(doc, d) is None:
                fatal.append((d.start + 1, f"{d.id} is not followed by a ::: {{.solution}}"
                                           f" (hint rungs do not count)"))

    # ideas before long proofs
    for d in doc.divs:
        if not d.has("proof"):
            continue
        if d.parent is not None and (d.parent.has("claim") or d.parent.has("proof")):
            continue
        n = proof_length(doc, d)
        if n <= idea_lines:
            continue
        prev = mdblocks.previous_sibling(d, doc)
        if prev is None or not prev.has("idea"):
            owner = prev.id if prev is not None and prev.id else "proof"
            advisory.append((d.start + 1, f"{owner}: proof of {n} lines has no ::: {{.idea}} before it"))

    advisory += check_ledger(text)

    words = prose_words(text)
    if not WORDS_MIN <= words <= WORDS_MAX:
        advisory.append((1, f"{words} words of prose (aim for {WORDS_MIN:,}-{WORDS_MAX:,})"))
    return fatal, advisory


def check_index(text: str):
    fatal = []
    for part in INDEX_PARTS:
        pat = rf"^(#{{2,3}}\s+{part}\b|\*\*{part}\b)"
        if not re.search(pat, text, flags=re.M | re.I):
            fatal.append((1, f"index.md has no '{part}' part (a ## heading or a **bold** lead-in)"))
    advisory = []
    for part in INDEX_ADVISORY:
        if not re.search(rf"^(#{{2,3}}\s+{part}\b|\*\*{part}\b)", text, flags=re.M | re.I):
            advisory.append((1, f"index.md has no '{part}' line"))
    return fatal, advisory


def find_violations(root: Path, idea_lines: int = IDEA_LINES):
    """Check every chapter file under `root` (a file, a chapter or src/).

    Returns (fatal, advisory): lists of (path, lineno, message). The book's
    top-level `src/index.md` (the preface) is not a chapter and is skipped.
    """
    root = Path(root)
    files = [root] if root.is_file() else sorted(root.rglob("*.md"))
    fatal, advisory = [], []
    for f in files:
        if not re.match(r"ch\w+", f.parent.name):
            continue
        text = f.read_text(encoding="utf-8")
        sections = sorted(p.name for p in f.parent.glob("[0-9]*.md"))
        last = not sections or f.name == sections[-1]
        fa, ad = check_index(text) if f.name == "index.md" else check_section(text, idea_lines, last)
        fatal += [(f, ln, m) for ln, m in fa]
        advisory += [(f, ln, m) for ln, m in ad]
    return fatal, advisory


def report(items) -> str:
    return "\n".join(f"{p}:{ln}: {m}" for p, ln, m in items)


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(
        description="Check section files against the STYLE.md section contract.")
    series.add_book_arg(ap)
    ap.add_argument("paths", nargs="*", default=["src"], help="files or directories (default: src)")
    ap.add_argument("--fatal-only", action="store_true", help="do not print advisories")
    ap.add_argument("--idea-lines", type=int, default=IDEA_LINES,
                    help=f"proofs longer than this need an Idea (default {IDEA_LINES})")
    args = ap.parse_args(argv)
    fatal, advisory = [], []
    for p in args.paths:
        fa, ad = find_violations(Path(p), args.idea_lines)
        fatal += fa
        advisory += ad
    if advisory and not args.fatal_only:
        print("Advisory:")
        print(report(advisory))
        print()
    if fatal:
        print("Fatal:")
        print(report(fatal))
    print(f"\n{len(fatal)} fatal, {len(advisory)} advisory.")
    return 1 if fatal else 0


def run(book, labels):
    """The engine's check plugin protocol (build/plugins.py): (errors, warnings)."""
    fatal, advisory = find_violations(book.src_dir)
    root = Path(book.root)
    errors = report([(Path(p).resolve().relative_to(root.resolve()), n, m)
                     for p, n, m in fatal]).splitlines()
    warnings = ([f"{len(advisory)} section-structure advisory note(s); run "
                 f"`python3 tools/check_structure.py --book {root.name}` to list them"]
                if advisory else [])
    return errors, warnings

if __name__ == "__main__":
    sys.exit(main())
