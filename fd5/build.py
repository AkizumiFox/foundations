#!/usr/bin/env python3
"""Build this volume: ./build.py html | pdf | book | all | serve | check | doctor | deploy | clean

The engine is the repository's git submodule engine/ (after a clone or in a new worktree:
`git submodule update --init`), or the directory $BOOK_ENGINE names -- a working copy of
the engine, to try an engine change on this book before pinning it.
"""
import os
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent
ENGINE = os.environ.get("BOOK_ENGINE")
if ENGINE:
    ENGINE = Path(ENGINE).expanduser().resolve()
else:   # the volume's own engine/, else the repository's (one submodule for every volume)
    ENGINE = next((d / "engine" for d in (BOOK, BOOK.parent) if (d / "engine" / "build" / "cli.py").is_file()),
                  BOOK.parent / "engine")
if not (ENGINE / "build" / "cli.py").is_file():
    sys.exit(f"No book engine in {ENGINE}.\nRun: git submodule update --init   (or set BOOK_ENGINE)")
sys.path.insert(0, str(ENGINE))
from build.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(default_book=BOOK) or 0)
