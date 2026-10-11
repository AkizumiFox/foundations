# Foundations

The `foundations` series of the math-atlas textbooks: one book per volume. Split from
analysis-book on 2026-10-12 with its full history (math-atlas spec/06,
"系列與冊").

| Directory | Atlas | Volume | State |
|---|---|---|---|
| `fd1/` | F1 | Logic and Proof | book |
| `fd2/` | F2 | Sets, Relations, and Cardinality | book |
| `fd3/` | F3 | Number Systems: From \(\nN\) to \(\nR\) | book |
| `fd4/` | F4 | Algebraic Preliminaries | planned |
| `st/` | ST | Axiomatic Set Theory | planned |

A volume with sources is a book: `config/config.json`, `src/`, `verify/` (numeric sidecars),
`authoring/` (ledger, blueprints, reviews), `tests/`, and `build.py`. Chapters are numbered
from 1 within each volume; `authoring/series.json` maps them to math-atlas's chapter ids
(`python3 tools/series.py show`).

Shared at the root: `engine/` (the book engine, a git submodule), `tools/` (the book tools),
`authoring/` (STYLE, PIPELINE, NOTATION, DRAFTING, STATUS, design notes), `latex/macros.tex`,
`spelling.txt`, `tests/` (the book tools' tests).

| Task | Command |
|---|---|
| After a clone or in a new worktree | `git submodule update --init` |
| Build a volume | `cd fd1 && ./build.py html` (`all`, `check`, `serve`, ...) |
| Against a working copy of the engine | `BOOK_ENGINE=~/coding/book-engine ./build.py html` |
| A book tool on a volume | `python3 tools/ledger.py --book fd2 stale 1`, or `cd fd2 && python3 ../tools/ledger.py stale 1` |
| Promises of the whole repository | `python3 tools/promises.py --reconcile` |
| Book tool tests | `python3 -m unittest discover -s tests` |
| A volume's own tests (after `./build.py html`) | `cd fd1 && python3 -m unittest discover -s tests` |
| Several books in one site | `./build.py library <manifest>` (engine BUILD.md, "A library") |

The two repositories of the series are checked out side by side, as `foundations/` and
`analysis-series/` (the directory names in `tools/series.py`'s `CHECKOUTS`): a volume's
`external-books` read the other repository's built labels there, e.g.
`../../analysis-series/an1/_build/crossref_labels.json`, and the linear-algebra companion's
from `../../linear-algebra/`. Clone with `git clone --recurse-submodules`.

References into another volume are `@fd1:label` (the label never changes); a prose
pointer into another volume names it: "*Logic and Proof*, Chapter 4". Bookkeeping names
chapters by atlas id (`F1.4`, `F2.1 §04`).
