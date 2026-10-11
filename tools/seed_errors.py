#!/usr/bin/env python3
"""Plant known errors in a copy of a chapter, and score a referee's recall on them.

`authoring/PIPELINE.md` measures referee recall at each Part pilot (target >= 0.8):
plant known errors in a copy of the chapter, run the referees on the copy, and count
how many they find. This tool (research-production §6) does the planting and the
counting, so the errors are known exactly and the run can be repeated.

**plant** copies the chapter directory to `--out/<chapter dir>/` and plants `-n`
errors, drawn in turn from the catalogue below (in an order shuffled by `--seed`).
Every error replaces **one line with one line**, so line numbers in the copy are the
line numbers of the original and no two errors share a line. The answer key (JSON:
file, line, kind, what was changed, the original and the planted line) goes to
`--key`, by default `<out>.key.json` beside, never inside, the directory the
referees get. The same chapter, `-n` and `--seed` always plant the same errors.

Catalogue (`--kinds` picks a subset; `catalogue` lists it):

* `drop-hypothesis`  -- in a theorem, lemma, proposition or corollary statement,
  delete one hypothesis: an adjective (`non-empty`, `bounded above`, `positive`, ...),
  a `with \\( ... \\)` clause, or a `Suppose ...` / `Assume ...` sentence;
* `swap-quantifiers` -- on a line with a universal phrase (`for every`, `for each`,
  `for all`, `\\forall`) followed by an existential one (`there exists`, `there is`,
  `some`, `\\exists`), exchange the two phrases' quantifier words;
* `perturb-constant` -- in an example, exercise, solution or proof, change a
  chosen constant by one: `N = 12` -> `N = 13`, `\\frac{1}{10}` -> `\\frac{1}{11}`;
* `false-meta-claim` -- append a false sentence about the section's own text to a
  prose paragraph ("This section states exactly 7 results."), made false by counting;
* `wrong-variant`    -- change an exercise's statement (`<` <-> `\\le`, `>` <-> `\\ge`,
  an integer by one) and leave its solution alone, so the solution answers a
  different variant;
* `closed-box-cite`  -- in a Fitch derivation (`nd`), make a line cite a line inside
  a box that has already closed.

**score** reads a referee's findings -- the tables of `authoring/reviews/*.md` (rows
whose Verdict is `correct` are not findings) or any list of `file:line` locations,
one finding per line -- and counts a planted error as found when a finding names its
file (by name, or by the section number `04` / `§04`) and a line within
`--tolerance` lines of it. It prints recall overall and per kind; `--json` writes it
for `tools/metrics.py` (by convention `authoring/reviews/chNN-seeded.json`).

    python3 tools/seed_errors.py plant 10 -n 10 --seed 7 --out /tmp/seed/ch10
    python3 tools/seed_errors.py score /tmp/seed/ch10.key.json referee-a.md referee-b.md
    python3 tools/seed_errors.py score KEY findings.md --json authoring/reviews/ch10-seeded.json
    python3 tools/seed_errors.py catalogue

Importable: `plant(chapter_dir, out, n, seed, kinds)`, `parse_findings(text)`, `score(key, findings)`.
"""
import argparse
import json
import random
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

SRC = Path("src")
RESULT_KINDS = ("thm", "lem", "prp", "cor")
TOLERANCE = 3

KINDS = {
    "drop-hypothesis": "a hypothesis deleted from a theorem statement",
    "swap-quantifiers": "a universal and an existential quantifier phrase exchanged",
    "perturb-constant": "a chosen constant changed by one",
    "false-meta-claim": "a false sentence about the section's own text added",
    "wrong-variant": "an exercise changed so its solution answers a different variant",
    "closed-box-cite": "a derivation line citing a line inside a closed box",
}


# ---------------------------------------------------------------------------
# Candidate sites: each is (line index, new line, description)
# ---------------------------------------------------------------------------

def _divs_of(doc, kinds=None, classes=None):
    for d in doc.divs:
        if kinds and d.id.split("-", 1)[0] in kinds and "-" in d.id:
            yield d
        elif classes and any(d.has(c) for c in classes):
            yield d


def _statement_lines(doc, div):
    """Lines of a block's own text (not of nested blocks, not code)."""
    nested = {i for c in div.children for i in range(c.start, c.end + 1)}
    for i in range(div.start + 1, div.end):
        if i not in nested and not doc.in_code[i] and doc.lines[i].strip():
            yield i


ADJ = (r"non-?empty|bounded above|bounded below|bounded|closed|open|positive|non-?negative|"
       r"non-?zero|finite|strictly increasing|increasing|decreasing|continuous|distinct|nested")
ADJ_PAIR = re.compile(rf"\b({ADJ})(\s*,\s*|\s+and\s+)(?=(?:{ADJ})\b)")
WITH_CLAUSE = re.compile(r",?\s+with\s+\\\(.*?\\\)(?=[,.;]|\s+(?:such|then|for)\b)")
WITH_AND = re.compile(r"(?<=\bwith\s)\\\(.*?\\\)\s+and\s+(?=\\\()")
HYP_SENTENCE = re.compile(r"(?:^|(?<=[.:]\s))\s*(?:Let|If|Suppose|Assume)\b[^.]*", re.S)
SUPPOSE = re.compile(r"(?:(?<=[.:]\s)|^)(?:Suppose|Assume)\b[^.]*?\.\s*")


def sites_drop_hypothesis(doc):
    out = []
    for div in _divs_of(doc, RESULT_KINDS):
        for i in _statement_lines(doc, div):
            line = doc.lines[i]
            if line.lstrip().startswith("["):
                continue
            hyp = [(h.start(), h.end()) for h in HYP_SENTENCE.finditer(line)]
            for m in ADJ_PAIR.finditer(line):
                if not any(a <= m.start() < b for a, b in hyp):
                    continue          # an adjective in the conclusion is not a hypothesis
                new = line[:m.start()] + line[m.end():]
                out.append((i, new, f"{div.id}: dropped the hypothesis '{m.group(1)}'"))
            for rx in (WITH_CLAUSE, WITH_AND):
                for m in rx.finditer(line):
                    if not any(a <= m.start() < b for a, b in hyp):
                        continue          # a "with" in the conclusion is not a hypothesis
                    new = line[:m.start()] + line[m.end():]
                    out.append((i, new, f"{div.id}: dropped the hypothesis "
                                        f"'{m.group(0).strip(', ')}'"))
            for m in SUPPOSE.finditer(line):
                new = (line[:m.start()] + line[m.end():]).rstrip()
                if new.strip():
                    out.append((i, new, f"{div.id}: dropped the sentence '{m.group(0).strip()}'"))
    return out


BEFORE_MATH = r"(?=(?:\s+[A-Za-z]+)?\s+\\\()"     # the phrase binds a variable: math follows
UNIV = re.compile(rf"\b(?:for every|for each|for all){BEFORE_MATH}|\\forall\b", re.I)
EXIST = re.compile(rf"\b(?:there exists|there exist|there is|there are|some){BEFORE_MATH}|\\exists\b",
                   re.I)


def _swap_word(word: str) -> str:
    table = {"for every": "there exists", "for each": "there exists", "for all": "there exists",
             "there exists": "for every", "there exist": "for all", "there is": "for every",
             "there are": "for all", "some": "every", "\\forall": "\\exists", "\\exists": "\\forall"}
    new = table[word.lower()]
    return new[0].upper() + new[1:] if word[0].isupper() else new


def sites_swap_quantifiers(doc):
    out = []
    for i, line in enumerate(doc.lines):
        if doc.in_code[i] or line.lstrip().startswith(("#", ":::")):
            continue
        u = UNIV.search(line)
        if not u:
            continue
        e = EXIST.search(line, u.end())
        if not e or e.start() - u.end() > 160 or re.search(r"[.;]\s", line[u.end():e.start()]):
            continue                     # both in one sentence, close together
        if (u.group(0).startswith("\\")) != (e.group(0).startswith("\\")):
            continue                     # swap words with words, symbols with symbols
        new = (line[:u.start()] + _swap_word(u.group(0)) + line[u.end():e.start()]
               + _swap_word(e.group(0)) + line[e.end():])
        out.append((i, new, f"swapped '{u.group(0)}' and '{e.group(0)}'"))
    return out


CONST = re.compile(r"((?:\\coloneqq|(?<![<>!\\])=)\s*)(\d+)(?![\w.^{(])")
FRAC = re.compile(r"(\\[dt]?frac\s*)(\{\s*\d+\s*\}|\d)(\{\s*(\d+)\s*\}|(\d))")


def sites_perturb_constant(doc):
    out = []
    targets = list(_divs_of(doc, ("exm", "exr"), ("solution", "proof")))
    lines = sorted({i for d in targets for i in _statement_lines(doc, d)})
    for i in lines:
        line = doc.lines[i]
        if "\\(" not in line and "\\[" not in line and not line.startswith(" "):
            continue
        for m in CONST.finditer(line):
            n = int(m.group(2))
            k = n + 1
            new = line[:m.start(2)] + str(k) + line[m.end(2):]
            out.append((i, new, f"constant {m.group(1).strip()} {n} changed to {k}"))
        for m in FRAC.finditer(line):
            q = int(m.group(4) or m.group(5))
            new = line[:m.start(3)] + "{" + str(q + 1) + "}" + line[m.end(3):]
            out.append((i, new, f"fraction {m.group(0)} changed to denominator {q + 1}"))
    return out


def sites_false_meta_claim(doc):
    """A counted claim about the file, made false: results, exercises, proofs citing nothing."""
    ids = [d.id for d in doc.divs if d.id]
    results = sum(1 for x in ids if x.split("-", 1)[0] in RESULT_KINDS)
    exercises = sum(1 for x in ids if x.startswith("exr-"))
    proofs = [d for d in doc.divs if d.has("proof")]
    cited = any("@" in "\n".join(doc.lines[p.start:p.end]) for p in proofs)
    claims = [f"This section states exactly {results + 1} results.",
              f"The exercises at the end of this section number {exercises + 2} in all."]
    if proofs and cited:
        claims.append("No proof in this section cites an earlier result.")
    covered = {i for d in doc.divs for i in range(d.start, d.end + 1)}
    out = []
    for i, line in enumerate(doc.lines):
        s = line.strip()
        if (i in covered or doc.in_code[i] or not s or s.startswith(("#", ":::", "|", "\\", "<!--", "-", "*", "1."))
                or not s.endswith(".") or len(s.split()) < 12):
            continue
        for c in claims:
            out.append((i, line.rstrip() + " " + c, f"false meta-claim added: '{c}'"))
    return out


VARIANT = [(re.compile(r"\\le(?![a-z])"), "<"), (re.compile(r"(?<![\\\w])<(?!=)"), r"\\le"),
           (re.compile(r"\\ge(?![a-z])"), ">"), (re.compile(r"(?<![\\\w-])>(?!=)"), r"\\ge")]


def sites_wrong_variant(doc):
    out = []
    for div in _divs_of(doc, ("exr",)):
        nxt = mdblocks.following_div(doc, div)
        if nxt is None or not nxt.has("solution"):
            continue
        for i in _statement_lines(doc, div):
            line = doc.lines[i]
            if line.lstrip().startswith("[") or "\\(" not in line:
                continue
            for rx, rep in VARIANT:
                for m in rx.finditer(line):
                    if not _in_inline_math(line, m.start()):
                        continue
                    new = line[:m.start()] + rep.replace("\\\\", "\\") + line[m.end():]
                    out.append((i, new, f"{div.id}: '{m.group(0)}' changed to "
                                        f"'{rep.replace(chr(92) * 2, chr(92))}' in the statement; "
                                        f"the solution is unchanged"))
            for m in CONST.finditer(line):
                n = int(m.group(2))
                new = line[:m.start(2)] + str(n + 1) + line[m.end(2):]
                out.append((i, new, f"{div.id}: {n} changed to {n + 1} in the statement; "
                                    f"the solution is unchanged"))
    return out


def _in_inline_math(line: str, pos: int) -> bool:
    return line.rfind("\\(", 0, pos) > line.rfind("\\)", 0, pos)


ND_CMD = re.compile(r"^\s*\\(hypo|have)\s*\{([^}]*)\}|^\s*\\(open|close)\b")
REFS = re.compile(r"\\[A-Za-z]+\{([\d,\s-]+)\}\s*$")


def sites_closed_box_cite(doc):
    out = []
    text = doc.lines
    i = 0
    while i < len(text):
        if "\\begin{nd}" in text[i] and "[schema]" not in text[i] \
                and not any("% expect-invalid" in text[j] for j in range(max(0, i - 4), i)):
            stack, closed = [[]], []
            j = i + 1
            while j < len(text) and "\\end{nd}" not in text[j]:
                m = ND_CMD.match(text[j])
                if m and m.group(3) == "open":
                    stack.append([])
                elif m and m.group(3) == "close" and len(stack) > 1:
                    box = stack.pop()
                    closed.append(box)
                    stack[-1].extend(box)
                elif m and m.group(2) and m.group(2).strip().isdigit():
                    n = int(m.group(2))
                    for s in stack:
                        s.append(n)
                    r = REFS.search(text[j])
                    if m.group(1) == "have" and r and closed:
                        refs = [x.strip() for x in r.group(1).split(",")]
                        inside = sorted({x for b in closed for x in b} - {n})
                        for k, ref in enumerate(refs):
                            if ref.isdigit() and inside:
                                bad = [x for x in inside if x < n and str(x) != ref]
                                if not bad:
                                    continue
                                new_refs = refs[:]
                                new_refs[k] = str(bad[-1])
                                new = text[j][:r.start(1)] + ",".join(new_refs) + text[j][r.end(1):]
                                out.append((j, new, f"derivation line {n} now cites line {bad[-1]}, "
                                                    f"inside a closed box (was {ref})"))
                                break
                j += 1
            i = j
        i += 1
    return out


SITES = {
    "drop-hypothesis": sites_drop_hypothesis,
    "swap-quantifiers": sites_swap_quantifiers,
    "perturb-constant": sites_perturb_constant,
    "false-meta-claim": sites_false_meta_claim,
    "wrong-variant": sites_wrong_variant,
    "closed-box-cite": sites_closed_box_cite,
}


# ---------------------------------------------------------------------------
# Plant
# ---------------------------------------------------------------------------

def candidates(chapter_dir: Path, kinds) -> dict:
    """{kind: [(file name, line index, new line, description)]}, in a fixed order."""
    out = {k: [] for k in kinds}
    for f in sorted(Path(chapter_dir).glob("[0-9]*.md")):
        doc = mdblocks.parse(f.read_text(encoding="utf-8"))
        for k in kinds:
            for i, new, desc in SITES[k](doc):
                if new != doc.lines[i] and "\n" not in new:
                    out[k].append((f.name, i, new, desc))
    return out


def plant(chapter_dir: Path, out: Path, n: int, seed: int, kinds=None, gap: int = 2) -> list:
    """Copy `chapter_dir` into `out/` and plant up to `n` errors. Returns the key entries."""
    chapter_dir, out = Path(chapter_dir), Path(out)
    kinds = list(kinds or KINDS)
    rng = random.Random(seed)
    cands = candidates(chapter_dir, kinds)
    order = kinds[:]
    rng.shuffle(order)
    for k in order:
        rng.shuffle(cands[k])
    used, chosen = {}, []
    progress = True
    while len(chosen) < n and progress:
        progress = False
        for k in order:
            if len(chosen) >= n:
                break
            while cands[k]:
                fname, i, new, desc = cands[k].pop()
                if any(abs(i - j) <= gap for j in used.get(fname, ())):
                    continue
                used.setdefault(fname, []).append(i)
                chosen.append((k, fname, i, new, desc))
                progress = True
                break
    dest = out / chapter_dir.name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(chapter_dir, dest)
    key = []
    by_file = {}
    for k, fname, i, new, desc in chosen:
        by_file.setdefault(fname, []).append((i, new))
        orig = (chapter_dir / fname).read_text(encoding="utf-8").split("\n")[i]
        key.append({"id": 0, "kind": k, "file": fname, "line": i + 1,
                    "description": desc, "original": orig, "planted": new})
    for fname, edits in by_file.items():
        lines = (dest / fname).read_text(encoding="utf-8").split("\n")
        for i, new in edits:
            lines[i] = new
        (dest / fname).write_text("\n".join(lines), encoding="utf-8")
    key.sort(key=lambda e: (e["file"], e["line"]))
    for k, e in enumerate(key, 1):
        e["id"] = k
    return key


# ---------------------------------------------------------------------------
# Score
# ---------------------------------------------------------------------------

LOC_FILE = re.compile(r"([\w.\-/]*?([\w\-]+\.md)):(\d+)(?:\s*[-–]\s*(\d+))?")
LOC_SEC = re.compile(r"(?:§\s*)?\b(\d{2}):(\d+)(?:\s*[-–]\s*(\d+))?")
LOC_SEC_LINE = re.compile(r"§\s*(\d{2})\b[^|;]{0,40}?\blines?\s+(\d+)(?:\s*[-–]\s*(\d+))?")


def _locations(text: str) -> list:
    """(file name or section number, first line, last line) for each location in `text`."""
    locs = []
    taken = []
    for m in LOC_FILE.finditer(text):
        a = int(m.group(3))
        locs.append((m.group(2), a, int(m.group(4) or a)))
        taken.append((m.start(), m.end()))
    for rx in (LOC_SEC, LOC_SEC_LINE):
        for m in rx.finditer(text):
            if any(s <= m.start() < e for s, e in taken):
                continue
            a = int(m.group(2))
            locs.append((m.group(1), a, int(m.group(3) or a)))
    return locs


def parse_findings(text: str) -> list:
    """[(source line number, [locations])]: one finding per table row or list line."""
    findings = []
    verdict_col = None
    for n, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if set(s) <= set("|-: "):
                continue
            lowered = [c.lower() for c in cells]
            if "verdict" in lowered:
                verdict_col = lowered.index("verdict")
                continue
            if verdict_col is not None and verdict_col < len(cells) \
                    and re.sub(r"[*_`]", "", cells[verdict_col]).strip().lower().startswith("correct"):
                continue
        else:
            verdict_col = None if not s else verdict_col
        locs = _locations(s)
        if locs:
            findings.append((n, locs))
    return findings


def _same_file(where: str, fname: str) -> bool:
    if where.endswith(".md"):
        return Path(where).name == fname
    return fname.startswith(where + "-") or fname.startswith(where + ".")


def score(key: list, findings: list, tolerance: int = TOLERANCE) -> dict:
    found = {}
    for e in key:
        for src_line, locs in findings:
            if any(_same_file(w, e["file"]) and a - tolerance <= e["line"] <= b + tolerance
                   for w, a, b in locs):
                found[e["id"]] = src_line
                break
    per_kind = {}
    for e in key:
        k = per_kind.setdefault(e["kind"], {"planted": 0, "found": 0})
        k["planted"] += 1
        k["found"] += e["id"] in found
    matched = set(found.values())
    return {"planted": len(key), "found": len(found),
            "recall": round(len(found) / len(key), 3) if key else None,
            "per_kind": per_kind,
            "missed": [e for e in key if e["id"] not in found],
            "unmatched_findings": [n for n, _ in findings if n not in matched]}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def chapter_dir(arg: str, src: Path = SRC) -> Path:
    p = Path(arg)
    if p.is_dir():
        return p
    if arg.isdigit():
        found = sorted(Path(src).glob(f"ch{int(arg):02d}-*"))
        if found:
            return found[0]
    sys.exit(f"no chapter {arg!r} (a number, or a chapter directory)")


def main(argv=None) -> int:
    argv = series.enter_book(argv)   # --book DIR: a volume of the series (chapter numbers are its own)
    ap = argparse.ArgumentParser(description="Plant known errors in a copy of a chapter; "
                                             "score a referee's recall on them.")
    series.add_book_arg(ap)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plant", help="copy a chapter and plant errors; write the answer key")
    p.add_argument("chapter", help="chapter number or directory")
    p.add_argument("--out", required=True, help="scratch directory; the copy goes in OUT/<chapter dir>/")
    p.add_argument("-n", type=int, default=10, help="number of errors (default 10)")
    p.add_argument("--seed", type=int, default=0, help="random seed (default 0)")
    p.add_argument("--kinds", help=f"comma-separated subset of: {', '.join(KINDS)}")
    p.add_argument("--key", help="answer key path (default: OUT.key.json, outside OUT)")
    p.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    s = sub.add_parser("score", help="score findings against an answer key")
    s.add_argument("key", help="answer key JSON written by plant")
    s.add_argument("findings", nargs="+", help="referee reports (review tables or file:line lists)")
    s.add_argument("--tolerance", type=int, default=TOLERANCE,
                   help=f"lines of slack either side (default {TOLERANCE})")
    s.add_argument("--json", help="also write the score as JSON here")
    sub.add_parser("catalogue", help="list the kinds of error")
    args = ap.parse_args(argv)

    if args.cmd == "catalogue":
        for k, v in KINDS.items():
            print(f"{k:18} {v}")
        return 0

    if args.cmd == "plant":
        kinds = [k.strip() for k in args.kinds.split(",")] if args.kinds else list(KINDS)
        bad = [k for k in kinds if k not in KINDS]
        if bad:
            sys.exit(f"unknown kind(s): {', '.join(bad)}")
        src_dir = chapter_dir(args.chapter, Path(args.src))
        out = Path(args.out)
        key_path = Path(args.key) if args.key else out.parent / f"{out.name}.key.json"
        if key_path.resolve().is_relative_to(out.resolve()):
            sys.exit("the answer key must not be inside --out, which the referees read")
        key = plant(src_dir, out, args.n, args.seed, kinds)
        key_path.parent.mkdir(parents=True, exist_ok=True)
        key_path.write_text(json.dumps({"chapter": src_dir.name, "seed": args.seed, "n": args.n,
                                        "copy": str(out / src_dir.name), "errors": key},
                                       indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Planted {len(key)} error(s) in {out / src_dir.name} (seed {args.seed}); "
              f"answer key: {key_path}")
        if len(key) < args.n:
            print(f"only {len(key)} site(s) available for {args.n} requested")
        return 0

    data = json.loads(Path(args.key).read_text(encoding="utf-8"))
    key = data["errors"] if isinstance(data, dict) else data
    findings = []
    for f in args.findings:
        findings += [(f"{f}:{n}", locs) for n, locs in parse_findings(Path(f).read_text(encoding="utf-8"))]
    result = score(key, findings, args.tolerance)
    for kind, v in sorted(result["per_kind"].items()):
        print(f"  {kind:18} {v['found']}/{v['planted']}")
    for e in result["missed"]:
        print(f"  missed #{e['id']} {e['file']}:{e['line']} [{e['kind']}] {e.get('description', '')}")
    print(f"\nRecall {result['found']}/{result['planted']}"
          f" = {result['recall'] if result['recall'] is not None else 'n/a'}; "
          f"{len(result['unmatched_findings'])} finding(s) matched no planted error.")
    if args.json:
        out = {"chapter": data.get("chapter") if isinstance(data, dict) else None,
               "seed": data.get("seed") if isinstance(data, dict) else None, **result}
        Path(args.json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
