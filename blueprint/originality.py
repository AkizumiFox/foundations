"""Flag word sequences shared between a written chapter (src/chNN-*/*.md) and its source chapters.

    python blueprint/originality.py 7 [--n 8] [--extra PMA.2 SPI.5] [--src fd1/src]

Sources are the DAG nodes listed for the chapter in book.yaml (plus --extra nodes). Their
text is read from the converted library (env ANALYSIS_SOURCES, default
~/math-refs/analysis/converted): the section files named by the node's `files` range in
dag.json. Shared n-grams made only of mathematical boilerplate are ignored. A clean chapter
reports a handful of stock phrases at most; any run of prose is a copying defect.
"""
import argparse
import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = Path(os.environ.get("ANALYSIS_SOURCES", Path.home() / "math-refs/analysis/converted"))
COMMON = {"the", "of", "a", "is", "and", "to", "in", "that", "for", "be", "by", "with", "if", "then",
          "on", "as", "an", "are", "this", "it", "we", "let", "there", "exists", "every", "all", "such"}


# The vocabulary every analysis text shares: an n-gram made only of these words, the common
# words above and "math" (a formula) is stock phrasing ("math is not an upper bound of math",
# "every non-empty subset that is bounded above has a least upper bound") and is not reported.
# A flagged n-gram has at least three words outside this list: that is prose, not vocabulary.
STOCK = {"upper", "lower", "bound", "bounds", "bounded", "above", "below", "least", "greatest",
         "non", "empty", "subset", "set", "element", "property", "hence", "since", "so", "which",
         "has", "have", "not", "cannot", "prove", "show", "suppose", "assume", "then", "therefore",
         "thus", "even", "odd", "integer", "integers", "number", "real", "rational", "if", "only",
         "or", "at", "from", "both", "sides", "gives", "some", "any", "each", "is", "are", "no",
         "sequence", "function", "continuous", "converges", "limit", "point", "interval"}


def words(text: str):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())


def md_to_text(md: str) -> str:
    """Prose only: math, code, fences, labels and link targets removed (book and sources alike)."""
    md = re.sub(r"^---\n.*?\n---\n", " ", md, flags=re.S)
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    md = re.sub(r"\\\(.*?\\\)", " MATH ", md, flags=re.S)
    md = re.sub(r"\\\[.*?\\\](\{#[^}]*\})?", " ", md, flags=re.S)
    md = re.sub(r"\$\$.*?\$\$", " ", md, flags=re.S)
    md = re.sub(r"\$[^$\n]*\$", " MATH ", md)
    md = re.sub(r"^:::.*$", " ", md, flags=re.M)
    md = re.sub(r"@[a-z]+-[A-Za-z0-9-]+", " ", md)
    md = re.sub(r"\]\([^)]*\)", "]", md)
    return md


def ngrams(ws, n):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def source_files(node: dict, books: dict) -> list[Path]:
    folder = LIBRARY / books[node["book"]]["dir"] / "sections"
    ranges = [node.get("files")] + list(node.get("files_alt", []))
    picked = set()
    for r in filter(None, ranges):
        lo, _, hi = str(r).partition("-")
        lo, hi = int(lo), int(hi or lo)
        picked |= {p for p in folder.glob("*.md") if p.name[:3].isdigit() and lo <= int(p.name[:3]) <= hi}
    return sorted(picked)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--extra", nargs="*", default=[])
    ap.add_argument("--src", type=Path, default=ROOT / "src",
                    help="the volume's source folder (e.g. fd1/src); default ROOT/src")
    a = ap.parse_args()
    book = yaml.safe_load((ROOT / "blueprint/book.yaml").read_text())
    dag = json.loads((ROOT / "blueprint/dag.json").read_text())
    books = yaml.safe_load((ROOT / "blueprint/sources.yaml").read_text())["books"]
    ch = next(c for c in book["chapters"] if c["num"] == int(a.chapter))
    files = sorted(a.src.glob(f"ch{int(a.chapter):02d}-*/*.md"))
    mine = words(md_to_text("\n".join(f.read_text() for f in files)))
    mine_ng = ngrams(mine, a.n)
    print(f"chapter {a.chapter}: {len(mine)} words of prose checked, n = {a.n}")
    total = 0
    for nid in [s[0] for s in ch["sources"]] + a.extra:
        paths = source_files(dag["nodes"][nid], books)
        src = words(md_to_text("\n".join(p.read_text(errors="replace") for p in paths)))
        if len(src) < 200:
            print(f"  {nid}: UNCHECKED ({len(paths)} files, {len(src)} words)")
            continue
        shared = [g for g in mine_ng & ngrams(src, a.n)
                  if sum(w not in COMMON and w not in STOCK and w != "math" for w in g) >= 3]
        total += len(shared)
        print(f"  {nid}: {len(src)} source words, {len(shared)} shared {a.n}-grams")
        for g in sorted(shared)[:40]:
            print("     · " + " ".join(g))
    print(f"total shared: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
