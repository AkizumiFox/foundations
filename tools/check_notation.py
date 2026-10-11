#!/usr/bin/env python3
"""Notation advisories: macros missing from NOTATION.md, and symbols with two meanings.

`authoring/NOTATION.md` says every symbol the book uses has a row there and a macro
in `latex/macros.tex`, and that one symbol has one meaning. Both are easy to break
one section at a time and hard to see from inside a section, so this tool
(research-production §6) collects, per chapter:

* **macro uses**: every `\\name` in the chapter's source that is one of the book's
  own macros (defined in `latex/macros.tex` by `\\newcommand`, `\\renewcommand`,
  `\\providecommand`, `\\def` or `\\DeclareMathOperator`). A book macro that is used
  but never mentioned (as `\\name`) anywhere in NOTATION.md is reported. Standard
  LaTeX (`\\frac`, `\\sup`) is not a book macro and is never reported; nor are the
  derivation macros of `latex/fitch-book.sty`, which NOTATION.md documents as a set.
* **symbols introduced**: inside a definition block (`::: {#def-...}`), the math
  right after "write", "written", "denote(s/d) ... by" or "denoted", and the left
  side of every `\\coloneqq`; in top-level prose (outside every block), the math
  right after "we write" or "denote(d)". The symbol is that math with spaces
  removed; its **meaning** is the definition's label (or `file:line` for prose). A
  symbol introduced with two different meanings in the chapters of one Part is
  reported. Parts come from `config/config.json` (`chapters[].part`, which starts a
  Part that the following chapters belong to); chapters before the first part, or in a
  book without parts (a volume of the series), form one Part named by the book's title.

In a series split into volumes (tools/series.py), run it in a volume directory or with
`--book fd2`: NOTATION.md is the repository's (`authoring/NOTATION.md`) and the macro
file is the one the volume's config names (`"macros": "../latex/macros.tex"`).

Everything here is **advisory**: the tool prints what it finds and exits 0, unless
`--strict` is given.

    python3 tools/check_notation.py                 # advisories for all of src/
    python3 tools/check_notation.py --list          # also every symbol and macro, per chapter
    python3 tools/check_notation.py --strict        # exit 1 if anything is reported

Importable:

    from tools.check_notation import find_violations, report
    advisories = find_violations(Path("src"), Path("authoring/NOTATION.md"),
                                 Path("latex/macros.tex"), parts)
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

SRC = Path("src")
NOTATION = Path("authoring/NOTATION.md")
MACROS = Path("latex/macros.tex")
CONFIG = Path("config/config.json")

DEFINE = re.compile(
    r"\\(?:(?:re)?newcommand|providecommand|DeclareMathOperator)\*?\s*\{?\s*\\([A-Za-z]+)"
    r"|\\def\s*\\([A-Za-z]+)")
USE = re.compile(r"\\([A-Za-z]+)")
INLINE = r"\\\(\s*(.*?)\s*\\\)"
DEF_WRITE = re.compile(r"\b(?:we\s+)?(?:write|written|denoted?(?:\s+by)?)\s+" + INLINE, re.I | re.S)
DENOTE_BY = re.compile(r"\bdenotes?\b[^.]{0,80}?\bby\s+" + INLINE, re.I | re.S)
PROSE_WRITE = re.compile(r"\b(?:we\s+write|denoted?(?:\s+by)?)\s+" + INLINE, re.I | re.S)
COLONEQQ = re.compile(r"(?:\\\(|\\\[|^|,|\\quad|\\qquad|&)\s*([^()\[\],&]*?(?:\([^()]*\))?[^()\[\],&]*?)"
                      r"\s*\\coloneqq", re.S | re.M)


VARIABLE = re.compile(r"(?:[A-Za-z]|\\[A-Za-z]+(?<!\\bot))(?:_\{?[\w,]+\}?)?'*")


def chapter_of(dirname: str):
    m = re.match(r"ch(\d+)", dirname)
    return int(m.group(1)) if m else None


def book_macros(macros: Path = MACROS) -> set:
    if not Path(macros).exists():
        return set()
    text = re.sub(r"(?<!\\)%.*", "", Path(macros).read_text(encoding="utf-8"))
    return {a or b for a, b in DEFINE.findall(text)}


def notation_macros(notation: Path = NOTATION) -> set:
    if not Path(notation).exists():
        return set()
    return set(USE.findall(Path(notation).read_text(encoding="utf-8")))


def parts_from_config(config: Path = CONFIG) -> dict:
    """{chapter directory name: part name} from config.json, or {}."""
    try:
        data = json.loads(Path(config).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    part = data.get("title", "")
    out = {}
    for c in data.get("chapters", []):
        d = c.get("dir") if isinstance(c, dict) else c
        if isinstance(c, dict) and c.get("part"):
            part = c["part"]            # a chapter with a part starts it; the next ones follow
        if d:
            out[Path(d).name] = part
    return out


def macros_from_config(config: Path = CONFIG) -> Path:
    """The macro file the config names (`macros`, relative to the book), else latex/macros.tex."""
    try:
        data = json.loads(Path(config).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return MACROS
    return Path(config).resolve().parent.parent / data.get("macros", str(MACROS))


def norm(sym: str) -> str:
    sym = re.sub(r"\\[,;:! ]|\\q?quad\b", "", sym)
    return re.sub(r"\s+", "", sym).strip(".,;")


def _lineno(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def symbols_in(text: str) -> list:
    """(lineno, symbol, meaning) for the symbols one file introduces; meaning is a label or None."""
    doc = mdblocks.parse(text)
    lines = ["" if code else ln for ln, code in zip(doc.lines, doc.in_code)]
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln) + 1)
    clean = "\n".join(lines)
    out = []
    covered = [False] * len(lines)
    for div in doc.divs:
        for i in range(div.start, div.end + 1):
            covered[i] = True
        if not div.id.startswith("def-"):
            continue
        a, b = offsets[div.start], offsets[div.end + 1] if div.end + 1 < len(offsets) else len(clean)
        body = clean[a:b]
        for rx in (DEF_WRITE, DENOTE_BY):
            for m in rx.finditer(body):
                out.append((_lineno(clean, a + m.start()), norm(m.group(1)), div.id))
        for m in COLONEQQ.finditer(body):
            lhs = norm(m.group(1))
            if lhs:
                out.append((_lineno(clean, a + m.start(1)), lhs, div.id))
    prose = "\n".join("" if covered[i] else ln for i, ln in enumerate(lines))
    for m in PROSE_WRITE.finditer(prose):
        out.append((_lineno(prose, m.start()), norm(m.group(1)), None))
    seen, uniq = set(), []
    for item in out:
        if VARIABLE.fullmatch(item[1]):
            continue                    # a bare letter is a variable, not notation
        if (item[1], item[2]) not in seen and item[1]:
            seen.add((item[1], item[2]))
            uniq.append(item)
    return uniq


TIKZ = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.S)


def macro_uses(text: str, macros: set) -> dict:
    """{macro: (first lineno, count)} for the book macros a file uses (TikZ pictures skipped:
    their `\\foreach \\k` variables are not macros)."""
    text = TIKZ.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out = {}
    for m in USE.finditer(text):
        name = m.group(1)
        if name in macros:
            ln, n = out.get(name, (_lineno(text, m.start()), 0))
            out[name] = (ln, n + 1)
    return out


def collect(src: Path = SRC, macros: set = frozenset()):
    """Per chapter directory: {'symbols': [(file, line, sym, meaning)], 'macros': {name: (file, line, n)}}."""
    data = {}
    for chdir in sorted(Path(src).glob("ch[0-9]*")):
        if not chdir.is_dir():
            continue
        syms, uses = [], {}
        for f in sorted(chdir.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            for ln, sym, meaning in symbols_in(text):
                syms.append((f, ln, sym, meaning or f"{f.name}:{ln}"))
            for name, (ln, n) in macro_uses(text, macros).items():
                if name in uses:
                    uses[name] = (uses[name][0], uses[name][1], uses[name][2] + n)
                else:
                    uses[name] = (f, ln, n)
        data[chdir.name] = {"symbols": syms, "macros": uses}
    return data


def find_violations(src: Path = SRC, notation: Path = NOTATION, macros_file: Path = MACROS,
                    parts: dict | None = None) -> list:
    """Advisories as (path, lineno, message)."""
    macros = book_macros(macros_file)
    listed = notation_macros(notation)
    parts = parts if parts is not None else parts_from_config()
    data = collect(src, macros)
    out = []
    for chname, d in data.items():
        for name, (f, ln, n) in sorted(d["macros"].items()):
            if name not in listed:
                out.append((f, ln, f"macro \\{name} is used ({n}x in {chname}) but not listed "
                                   f"in {notation}"))
    by_part = defaultdict(lambda: defaultdict(list))
    for chname, d in data.items():
        part = parts.get(chname) or chname
        for f, ln, sym, meaning in d["symbols"]:
            by_part[part][sym].append((f, ln, meaning))
    for part, syms in by_part.items():
        for sym, uses in sorted(syms.items()):
            meanings = sorted({m for _, _, m in uses})
            if len(meanings) > 1:
                f, ln, _ = uses[1] if uses[1][2] != uses[0][2] else \
                    next(u for u in uses if u[2] != uses[0][2])
                where = "; ".join(f"{m} ({uf.parent.name}/{uf.name}:{ul})"
                                  for uf, ul, m in sorted({(u[0], u[1], u[2]) for u in uses},
                                                           key=lambda u: (str(u[0]), u[1])))
                out.append((f, ln, f"symbol {sym} has {len(meanings)} meanings in {part}: {where}"))
    return out


def report(items) -> str:
    return "\n".join(f"{p}:{ln}: {m}" for p, ln, m in items)


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(
        description="Notation advisories: book macros missing from NOTATION.md, and symbols "
                    "introduced with two meanings within one Part.")
    series.add_book_arg(ap)
    ap.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    ap.add_argument("--notation", default=None,
                    help="NOTATION.md path (default: authoring/NOTATION.md, the book's or the repository's)")
    ap.add_argument("--macros", default=None,
                    help="macro file (default: the config's `macros`, else latex/macros.tex)")
    ap.add_argument("--config", default=str(CONFIG), help="config with chapters[].part")
    ap.add_argument("--list", action="store_true", help="also list every symbol and macro per chapter")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything is reported")
    args = ap.parse_args(argv)
    args.notation = args.notation or str(series.shared(str(NOTATION)))
    args.macros = args.macros or str(macros_from_config(Path(args.config)))
    if args.list:
        data = collect(Path(args.src), book_macros(Path(args.macros)))
        for chname, d in data.items():
            print(f"{chname}:")
            print("  macros: " + ", ".join(f"\\{k} ({v[2]})" for k, v in sorted(d["macros"].items())))
            for f, ln, sym, meaning in d["symbols"]:
                print(f"  {f.name}:{ln}: {sym}  <- {meaning}")
        print()
    items = find_violations(Path(args.src), Path(args.notation), Path(args.macros),
                            parts_from_config(Path(args.config)))
    if items:
        print(report(items))
    print(f"\n{len(items)} notation advisory note(s).")
    return 1 if items and args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
