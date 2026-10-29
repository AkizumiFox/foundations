"""Print the table of contents of a converted reference book, from its sections' front matter.

    python blueprint/toc.py ABB            # one book: index, pdf pages, section title, headings
    python blueprint/toc.py ABB --brief    # section titles and page ranges only
    python blueprint/toc.py --all --brief  # every book in blueprint/sources.yaml

The converted library lives outside this repository (env ANALYSIS_SOURCES, default
~/math-refs/analysis/converted); each book there has sections/NNN-*.md files whose YAML front
matter records `section`, `pdf_pages` and `headings`. Only titles and page numbers are
printed -- enough to build DAG nodes and coverage lists without reading the text.
"""
import argparse
import os
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = Path(os.environ.get("ANALYSIS_SOURCES", Path.home() / "math-refs/analysis/converted"))


def books() -> dict:
    return yaml.safe_load((ROOT / "blueprint/sources.yaml").read_text())["books"]


def sections(code: str) -> list[dict]:
    """Front matter of each section file of the book `code`, in order."""
    folder = LIBRARY / books()[code]["dir"] / "sections"
    out = []
    for path in sorted(folder.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        meta = yaml.safe_load(text.split("---", 2)[1]) or {}
        meta["file"] = path.name
        meta["words"] = len(text.split())
        out.append(meta)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--brief", action="store_true")
    args = ap.parse_args()
    codes = list(books()) if args.all else args.codes
    if not codes:
        ap.error("name a book code from blueprint/sources.yaml, or --all")
    for code in codes:
        info = books()[code]
        print(f"## {code}  {Path(info['dir']).name}  [{info['role']}; Part {info['part']}]")
        for s in sections(code):
            pages = s.get("pdf_pages") or ["?", "?"]
            line = f"{s['file'][:3]}  pp.{pages[0]}-{pages[1]}  {s.get('section', '')}"
            if not args.brief:
                heads = [h for h in s.get("headings", [])[1:] if h][:8]
                if heads:
                    line += "  | " + " / ".join(heads)
            print(line)
        print()


if __name__ == "__main__":
    sys.exit(main())
