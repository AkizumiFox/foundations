#!/usr/bin/env python3
"""Check the reader-facing prose of each section against STYLE §13 ("Writing for a beginner").

Read-only. Advisory by default: it prints what it finds and exits 0; `--strict` makes any
finding fail the run (exit 1). The mechanical half of §13; Referee C (PIPELINE S5) reads for
the rest. Per section file (`src/chNN-slug/MM-slug.md`) it flags, as `path:line: [kind] ...`:

* `refs`      -- a sentence with more than one inline `@ref` outside a Uses line (B1). A
  Uses line is a `::: {.uses}` div (or, in a draft, a paragraph opening with `*Uses:*`);
  references there are not counted. A sentence comparing two results may keep two (B1):
  the tool cannot tell, so read the flag before acting on it;
* `long`      -- a sentence of more than `--max-words` words (default 35; displays not
  counted, inline math and an `@ref` count one word each) (B6);
* `nested`    -- a parenthesis inside a parenthesis, math removed first; a reference's
  clause tags, "(@thm-x (a))", do not count (B6);
* `semicolons`-- more than two semicolons in one sentence (B6);
* `term`      -- an authoring term printed for the reader (B4): in prose, headings, list
  items, table cells and box titles (`title="..."`, a `[Title]` line). The default list is
  TERMS below; `--terms FILE` replaces it (one term per line, `#` comments; a term is
  matched case-insensitively as whole words);
* `code`      -- a clause or rule code, such as (Eq3) or (O3), used alone after "by",
  "from", "using", "and" or "via", with no words saying what it is (B7). A heuristic:
  "transitivity, (Eq3)" passes, "by (Eq3)" is flagged.

Per chapter `index.md` (B4, B8):

* `time-line` -- the old Time-line template ("on the core track (all of A, ...)");
* `index-part`-- a Named moves / Proof methods, Summary or Terms part in the index: §13
  moves them to the Chapter review page (`review.md` in the chapter directory);
* `need`      -- a "What you need" part with more than five links.

Not checked: prose inside code fences and raw LaTeX (a block opening with `\\begin{...}`
at the start of a line, to its `\\end{...}`), displays `\\[ ... \\]`, HTML comments
(the dependency ledger), and the attributes of a div fence other than `title`.

    python3 tools/check_beginner.py --book fd1                 # all of fd1/src
    python3 tools/check_beginner.py --book fd3 src/ch02-integers/02-well-defined-operations.md
    python3 tools/check_beginner.py --book fd2 --summary       # counts only, per chapter
    python3 tools/check_beginner.py --book fd1 --only refs,long
    python3 tools/check_beginner.py --book fd1 --strict        # exit 1 on any finding

Importable:

    from check_beginner import check_text, check_index, find_findings, KINDS
    findings = check_text(text)           # [(lineno, kind, message)]
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

MAX_WORDS = 35
MAX_SEMICOLONS = 2
MAX_NEED_LINKS = 5
KINDS = ("refs", "long", "nested", "semicolons", "term", "code", "time-line", "index-part", "need")

# STYLE §13 B4: authoring vocabulary that never reaches the page. Matched as whole words,
# case-insensitively; a plural "s" is allowed after the last word.
TERMS = (
    "core track", "exit check", "named move", "method box", "fold", "hook", "payoff",
    "prompt", "self-explain", "template", "usual failure", "non-example by minimal change",
    "degenerate", "givens", "citing rule", "ledger", "legal source", "legal target",
    "fatal error", "second reading",
)

REF = re.compile(r"(?<![\w.@])@(?:[a-z][a-z0-9]*:)?[a-z]+-[\w-]*[\w]")
# A reference with its clause tags, "@thm-x (a), (c)": one citation, not a nested parenthesis
CLAUSE = r"\((?:[a-z]{1,4}|[A-Z][A-Za-z]{0,3}\d+[a-z]?)\)"
REF_CLAUSES = re.compile(REF.pattern + r"(?:\s*" + CLAUSE + r"(?:\s*(?:,|and|or)\s*" + CLAUSE + r")*)?")
CODE_ALONE = re.compile(r"\b(?:by|from|using|and|via|or)\s+\(([A-Z][A-Za-z]{0,3}\d+[a-z]?)\)")
TITLE_ATTR = re.compile(r'title="([^"]*)"')
USES_PARA = re.compile(r"^\s*\*Uses:?\*")
ABBREV = re.compile(r"\b(e\.g|i\.e|cf|etc|vs|Fig|Ch|Sec|resp|approx)\.$", re.I)
SENTENCE_END = re.compile(r"(?<=[.?!])[)\"”’*_]*\s+(?=[\"“(*_\[]*[A-Z0-9@\\]|\*?\((?:[ivx]+|[a-z])\))")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
INDEX_MOVED = ("Named moves", "Proof methods", "Summary", "Terms")
TIME_TEMPLATE = re.compile(r"core track|\(all of A, one B and one C per section", re.I)


def term_patterns(terms):
    out = []
    for t in terms:
        words = [re.escape(w) for w in t.split()]
        out.append((t, re.compile(r"(?<![\w-])" + r"[\s/-]+".join(words) + r"(?:s|es)?(?![\w-])", re.I)))
    return out


DEFAULT_TERMS = term_patterns(TERMS)


def load_terms(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return term_patterns([ln.split("#", 1)[0].strip() for ln in lines if ln.split("#", 1)[0].strip()])


def _strip_math(text: str) -> str:
    text = re.sub(r"\\\[.*?\\\]", " X ", text, flags=re.S)
    return re.sub(r"\\\(.*?\\\)", " X ", text, flags=re.S)


def words(sentence: str) -> int:
    t = REF.sub(" X ", sentence)
    t = re.sub(r"`[^`]*`", " X ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)      # [text](url)
    t = re.sub(r"[#*_>\[\]{}|]", " ", t)
    return len(re.findall(r"[A-Za-z0-9][\w'’-]*", t))


def nested_parens(sentence: str) -> bool:
    """A parenthesis inside a parenthesis. A reference's clause tags, "(@thm-x (a))", do
    not count: B1 moves such a citation to the Uses line, and `refs` reports it there."""
    depth = 0
    for ch in REF_CLAUSES.sub("X", sentence):
        if ch == "(":
            depth += 1
            if depth >= 2:
                return True
        elif ch == ")":
            depth = max(depth - 1, 0)
    return False


def sentences(text: str):
    """Split a paragraph (math already replaced) into sentences: (offset, sentence)."""
    out, start = [], 0
    for m in SENTENCE_END.finditer(text):
        piece = text[start:m.start()]
        if ABBREV.search(piece.rstrip(")\"”’*_")):
            continue
        out.append((start, piece))
        start = m.end()
    if text[start:].strip():
        out.append((start, text[start:]))
    return out


def paragraphs(text: str):
    """Reader-facing prose units of a Markdown file: (first line no., text, kind, in_uses).

    kind is "prose", "heading", "item", "cell" or "title". Code, raw LaTeX, displays,
    HTML comments and fence lines (except their title attribute) are left out.
    """
    doc = mdblocks.parse(text)
    lines = doc.lines
    uses_lines = set()
    for d in doc.divs:
        if d.has("uses"):
            uses_lines.update(range(d.start, d.end + 1))
    units, buf, buf_start, buf_uses = [], [], 0, False
    in_comment = in_display = False
    raw_env = None          # a raw LaTeX block (a derivation, a tikzpicture) outside a code fence

    def flush():
        nonlocal buf
        if buf:
            joined = " ".join(buf)
            units.append((buf_start + 1, joined, "prose", buf_uses or bool(USES_PARA.match(joined))))
        buf = []

    for i, line in enumerate(lines):
        s = line.strip()
        if doc.in_code[i]:
            flush()
            continue
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            flush()
            if "-->" not in s:
                in_comment = True
            continue
        if raw_env:
            if f"\\end{{{raw_env}}}" in s:
                raw_env = None
            continue
        m = re.match(r"^\\begin\{([^}]+)\}", s)
        if m and not in_display:
            flush()
            if f"\\end{{{m.group(1)}}}" not in s:
                raw_env = m.group(1)
            continue
        if in_display:
            if "\\]" in s:
                in_display = False
                rest = s.split("\\]", 1)[1]
                rest = re.sub(r"^\{#eq-[^}]*\}", "", rest).strip()
                if rest:
                    buf.append(rest)
            continue
        if s.startswith("\\[") and "\\]" not in s:
            buf.append(" X ")
            in_display = True
            continue
        if mdblocks.OPEN.match(line) or mdblocks.CLOSE.match(line):
            flush()
            m = TITLE_ATTR.search(line)
            if m:
                units.append((i + 1, m.group(1), "title", False))
            continue
        if not s:
            flush()
            continue
        m = mdblocks.HEADING.match(line)
        if m:
            flush()
            units.append((i + 1, m.group(2), "heading", False))
            continue
        if s.startswith("|"):
            flush()
            if re.match(r"^\|[\s:|-]+\|?$", s):
                continue
            for cell in s.strip("|").split("|"):
                if cell.strip():
                    units.append((i + 1, cell.strip(), "cell", i in uses_lines))
            continue
        if re.match(r"^\[[^\]]+\]$", s):          # a box's [Title] line
            flush()
            units.append((i + 1, s[1:-1], "title", False))
            continue
        if LIST_ITEM.match(line):
            flush()
            buf_start, buf_uses = i, i in uses_lines
            buf.append(LIST_ITEM.sub("", line))
            continue
        if not buf:
            buf_start, buf_uses = i, i in uses_lines
        buf.append(s)
    flush()
    return units


def check_text(text: str, terms=None, max_words: int = MAX_WORDS):
    """Findings for one section file: [(lineno, kind, message)]."""
    terms = DEFAULT_TERMS if terms is None else terms
    out = []
    for lineno, unit, kind, in_uses in paragraphs(text):
        plain = _strip_math(unit)
        for term, pat in terms:
            m = pat.search(REF.sub(" ", plain))
            if m:
                out.append((lineno, "term", f"authoring term {m.group(0)!r} ({kind})"))
        if kind in ("heading", "title"):
            continue
        for _, sent in sentences(plain):
            snippet = " ".join(sent.split())[:70]
            if not in_uses:
                n = len(REF.findall(sent))
                if n > 1:
                    out.append((lineno, "refs", f"{n} inline references in one sentence: {snippet!r}"))
            n = words(sent)
            if n > max_words:
                out.append((lineno, "long", f"{n} words in one sentence: {snippet!r}"))
            if nested_parens(sent):
                out.append((lineno, "nested", f"a parenthesis inside a parenthesis: {snippet!r}"))
            if sent.count(";") > MAX_SEMICOLONS:
                out.append((lineno, "semicolons", f"{sent.count(';')} semicolons: {snippet!r}"))
            m = CODE_ALONE.search(sent)
            if m and not in_uses:
                out.append((lineno, "code", f"code ({m.group(1)}) used alone: {snippet!r}"))
    return out


def check_index(text: str, terms=None):
    """Findings for a chapter index.md: the section rules on its prose, plus B4/B8's parts."""
    out = [f for f in check_text(text, terms) if f[1] in ("term", "long", "nested", "refs")]
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^\*\*Time\.?\*\*", line.strip()) and TIME_TEMPLATE.search(line):
            out.append((i + 1, "time-line", "the old Time-line template (core track, exit checks): "
                                            "use STYLE §2's wording"))
        for part in INDEX_MOVED:
            if re.match(rf"^(#{{2,3}}\s+{part}\b|\*\*{part}\b)", line.strip(), flags=re.I):
                out.append((i + 1, "index-part", f"'{part}' belongs on the Chapter review page "
                                                 f"(review.md), not the chapter opening"))
    m = re.search(r"^(?:#{2,3}\s+What you need\b|\*\*What you need\b)(.*?)(?=^#{1,3}\s|^\*\*[A-Z][^*]*\*\*|\Z)",
                  text, flags=re.M | re.S | re.I)
    if m:
        n = len(REF.findall(m.group(0))) + len(re.findall(r"\]\([^)]*\)", m.group(0)))
        if n > MAX_NEED_LINKS:
            first = text.count("\n", 0, m.start()) + 1
            out.append((first, "need", f"What you need has {n} links (at most {MAX_NEED_LINKS})"))
    return sorted(out)


def chapter_files(root: Path):
    root = Path(root)
    files = [root] if root.is_file() else sorted(root.rglob("*.md"))
    return [f for f in files if re.match(r"ch\w+", f.parent.name)]


def find_findings(root: Path, terms=None, max_words: int = MAX_WORDS):
    """[(path, lineno, kind, message)] for every chapter file under `root`."""
    out = []
    for f in chapter_files(root):
        text = f.read_text(encoding="utf-8")
        if f.name == "index.md":
            found = check_index(text, terms)
        elif f.name == "review.md":
            found = [x for x in check_text(text, terms, max_words) if x[1] != "refs"]
        else:
            found = check_text(text, terms, max_words)
        out += [(f, ln, k, m) for ln, k, m in found]
    return out


def summary(findings, root: Path) -> str:
    """Counts per chapter directory and kind, and a total row."""
    by_chapter = {}
    for p, _, k, _ in findings:
        chap = Path(p).parent.name
        by_chapter.setdefault(chap, Counter())[k] += 1
    kinds = [k for k in KINDS if any(c[k] for c in by_chapter.values())] or list(KINDS[:3])
    rows = ["| chapter | " + " | ".join(kinds) + " | all |",
            "|---|" + "---:|" * (len(kinds) + 1)]
    total = Counter()
    for chap in sorted(by_chapter):
        c = by_chapter[chap]
        total.update(c)
        rows.append(f"| {chap} | " + " | ".join(str(c[k]) for k in kinds) + f" | {sum(c.values())} |")
    rows.append("| **total** | " + " | ".join(str(total[k]) for k in kinds) + f" | {sum(total.values())} |")
    return "\n".join(rows)


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(description="Check reader-facing prose against STYLE §13 "
                                             "(advisory; --strict to fail).")
    series.add_book_arg(ap)
    ap.add_argument("paths", nargs="*", default=["src"], help="files or directories (default: src)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything is found")
    ap.add_argument("--summary", action="store_true", help="print a count table only")
    ap.add_argument("--only", help="comma-separated kinds to report (" + ", ".join(KINDS) + ")")
    ap.add_argument("--terms", help="a file of authoring terms, one per line, replacing the default list")
    ap.add_argument("--max-words", type=int, default=MAX_WORDS,
                    help=f"longest sentence allowed (default {MAX_WORDS})")
    args = ap.parse_args(argv)
    terms = load_terms(args.terms) if args.terms else None
    findings = []
    for p in args.paths:
        findings += find_findings(Path(p), terms, args.max_words)
    if args.only:
        keep = {k.strip() for k in args.only.split(",")}
        unknown = keep - set(KINDS)
        if unknown:
            ap.error(f"unknown kind(s): {', '.join(sorted(unknown))}")
        findings = [f for f in findings if f[2] in keep]
    if args.summary:
        print(summary(findings, Path(args.paths[0])))
    else:
        for p, ln, k, m in findings:
            print(f"{p}:{ln}: [{k}] {m}")
        counts = Counter(k for _, _, k, _ in findings)
        print(f"\n{len(findings)} finding(s)" + (": " + ", ".join(f"{counts[k]} {k}" for k in KINDS if counts[k])
                                                if findings else "."))
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
