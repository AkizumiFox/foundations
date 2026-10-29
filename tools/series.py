#!/usr/bin/env python3
"""Where a book sits in its series: its volume, its chapters' atlas ids, and the other volumes.

The series is split into volumes, one book each (math-atlas spec/06, "系列與冊"). A volume is a
directory of this repository with its own `config/config.json`, `src/`, `verify/` and
`authoring/` (ledger, blueprints, reviews); the book tools in `tools/` and the shared documents
in `authoring/` sit at the repository root. Chapters are numbered from 1 within a volume, so a
chapter number alone no longer names a chapter. Two names do:

* the **atlas id** (`F1.4`, `F2.1`, `AN1.1`), math-atlas's stable chapter id
  (`registry/chapters.yaml`), used in the bookkeeping: STATUS.md, NOTATION.md, blueprints,
  dependency ledgers, and everything these tools print;
* the **local number** inside a volume (`fd2` chapter 1 = `src/ch01-*`), used in the prose: a
  pointer into the same volume is "Chapter 1" / "Section 1.4", a pointer into another volume
  carries its title the way the engine prints a reference into another book
  ("*Logic and Proof*, Chapter 4", like "Logic and Proof, Theorem 4.2.1").

`authoring/series.json` (repository root) holds the map: every volume of the series this
repository belongs to and of its sibling series, in reading order, with its prefix (the
`@prefix:label` of cross-book references), title, repository, directory and chapters. It is
generated from math-atlas's registry:

    python3 tools/series.py refresh ../../registry   # rewrite authoring/series.json
    python3 tools/series.py show                             # the map, one chapter a line
    python3 tools/series.py where                            # the volume of the current directory

Importable:

    from series import Series, book_root
    s = Series.load(); vol = s.volume_at(Path("fd2"))
    s.atlas_id("fd2", 1)  -> "F2.1";   s.locate("F2.1") -> ("fd2", 1)
"""
import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
SERIES_JSON = REPO / "authoring" / "series.json"
# the repositories (math-atlas `book` values) whose volumes this repository's tools must know
SERIES_REPOS = ("foundations", "analysis")
# the directory a repository is checked out in, next to this one (default: its name); the
# analysis repository is checked out as analysis-series, beside the author's corpus `analysis`
CHECKOUTS = {"foundations": "foundations", "analysis": "analysis-series"}
ATLAS_ID = re.compile(r"\b([A-Z]+\d*\.\d+[ab]?)\b")


@dataclass
class Volume:
    prefix: str
    id: str
    title: str
    repo: str
    dir: str
    chapters: list = field(default_factory=list)   # [{"n", "id", "title", "ab"}]
    order: int = 0
    checkout: str = ""      # the repository's checkout directory, a sibling of this one

    def chapter(self, n: int):
        return next((c for c in self.chapters if c["n"] == n), None)


class Series:
    def __init__(self, data: dict, repo: Path = REPO):
        self.repo = Path(repo)
        self.name = data.get("repo", "")
        self.volumes = []
        for i, v in enumerate(data.get("volumes", [])):
            self.volumes.append(Volume(v["prefix"], v["id"], v["title"], v.get("repo", ""),
                                       v.get("dir", v["prefix"]), v.get("chapters", []), i,
                                       v.get("checkout") or v.get("repo", "")))
        self.by_prefix = {v.prefix: v for v in self.volumes}
        self._ids = {c["id"]: (v.prefix, c["n"]) for v in self.volumes for c in v.chapters}

    @classmethod
    def load(cls, path: Path | None = None):
        """The series map, or an empty one (a plain book: every tool then works as before)."""
        path = Path(path) if path else SERIES_JSON
        if not path.exists():
            return cls({}, path.parent.parent)
        return cls(json.loads(path.read_text(encoding="utf-8")), path.parent.parent)

    def __bool__(self):
        return bool(self.volumes)

    # -- lookups ---------------------------------------------------------------------------
    def volume_at(self, book: Path):
        """The volume whose directory is `book` (a volume directory of this repository)."""
        book = Path(book).resolve()
        for v in self.volumes:
            if v.repo == self.name and (self.repo / v.dir).resolve() == book:
                return v
        return None

    def volume_by_title(self, title: str):
        t = _plain(title)
        return next((v for v in self.volumes if _plain(v.title) == t), None)

    def atlas_id(self, prefix: str, n: int):
        v = self.by_prefix.get(prefix)
        c = v.chapter(n) if v else None
        return c["id"] if c else None

    def locate(self, atlas_id: str):
        """(prefix, local number) of an atlas id, or None."""
        return self._ids.get(atlas_id)

    def order_key(self, atlas_id: str):
        """Reading order: volumes in registry order, chapters by local number."""
        loc = self.locate(atlas_id)
        if loc is None:
            return (10 ** 6, 0)
        return (self.by_prefix[loc[0]].order, loc[1])

    def volume_dir(self, prefix: str):
        """The directory of a volume: in this repository, or in a sibling checkout of its own
        repository (../<checkout>/<dir>, e.g. ../analysis-series/an1), or None."""
        v = self.by_prefix.get(prefix)
        if v is None:
            return None
        here = self.repo / v.dir if v.repo == self.name else self.repo.parent / v.checkout / v.dir
        return here if here.is_dir() else None

    def chapter_dir(self, atlas_id: str):
        """src/chNN-* of an atlas id, if that volume's sources are reachable."""
        loc = self.locate(atlas_id)
        vdir = self.volume_dir(loc[0]) if loc else None
        if vdir is None:
            return None
        found = sorted((vdir / "src").glob(f"ch{loc[1]:02d}-*"))
        return found[0] if found else None

    def describe(self, atlas_id: str) -> str:
        """`F2.1 (fd2 Ch 1)`: the id and where it is."""
        loc = self.locate(atlas_id)
        return f"{atlas_id} ({loc[0]} Ch {loc[1]})" if loc else atlas_id


def _plain(title: str) -> str:
    """A title compared without its math (prose_lines blanks math) and markup."""
    title = re.sub(r"\\\(.*?\\\)", " ", title)
    return re.sub(r"[\s*_]+", " ", title).strip().lower()


def book_root(arg: str | None = None) -> Path:
    """The book (volume) directory: --book, else the current directory."""
    return Path(arg).resolve() if arg else Path.cwd()


def enter_book(argv: list | None):
    """Strip `--book DIR` from argv and chdir into DIR, so a tool's relative defaults (src,
    verify, authoring/ledger, config/config.json) are that volume's. Returns the new argv."""
    argv = list(sys.argv[1:] if argv is None else argv)
    for i, a in enumerate(argv):
        if a == "--book" and i + 1 < len(argv):
            os.chdir(argv[i + 1])
            return argv[:i] + argv[i + 2:]
        if a.startswith("--book="):
            os.chdir(a.split("=", 1)[1])
            return argv[:i] + argv[i + 1:]
    return argv


def add_book_arg(ap):
    """Document --book in a tool's help (enter_book has already consumed it)."""
    ap.add_argument("--book", metavar="DIR",
                    help="the volume (book) directory to work on (default: the current directory)")


def shared(relative: str, book: Path | None = None) -> Path:
    """A shared file (authoring/STATUS.md, authoring/NOTATION.md, ...): the book's own copy if it
    has one (a plain book), else the repository root's."""
    book = Path(book) if book else Path.cwd()
    own = book / relative
    return own if own.exists() else REPO / relative


# ---------------------------------------------------------------------------
# Generating series.json from math-atlas's registry
# ---------------------------------------------------------------------------

def generate(registry: Path, repo_name: str, repos=SERIES_REPOS, checkouts=CHECKOUTS) -> dict:
    import yaml
    registry = Path(registry)
    vols = yaml.safe_load((registry / "volumes.yaml").read_text(encoding="utf-8"))
    chapters = yaml.safe_load((registry / "chapters.yaml").read_text(encoding="utf-8"))
    out = []
    for v in vols:
        if v.get("book") not in repos:
            continue
        chs = []
        for i, c in enumerate(chapters.get(v["id"], []) or [], 1):
            srcs = c.get("src")
            srcs = srcs if isinstance(srcs, list) else [srcs]
            ab = [int(s[3:]) for s in srcs if isinstance(s, str) and s.startswith("ab:")]
            entry = {"n": i, "id": c["id"], "title": c["title"]}
            if ab:
                entry["ab"] = ab[0]
            if c.get("opt"):
                entry["optional"] = True
            chs.append(entry)
        out.append({"prefix": v["prefix"], "id": v["id"], "title": v["title"],
                    "repo": v["book"], "checkout": checkouts.get(v["book"], v["book"]),
                    "dir": v["prefix"], "chapters": chs})
    return {
        "_README": ["The volumes of the series, in reading order (math-atlas registry/volumes.yaml",
                    "and chapters.yaml). Chapters are numbered from 1 in each volume; `id` is the",
                    "atlas chapter id, `ab` the analysis-book chapter it came from; `checkout` is",
                    "the directory, next to this repository's, where a volume's repository is",
                    "checked out (cross-repository lookups read ../<checkout>/<dir>). Regenerate",
                    "with python3 tools/series.py refresh <math-atlas>/registry; do not edit by hand."],
        "repo": repo_name,
        "volumes": out,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The series map (authoring/series.json).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("refresh", help="regenerate authoring/series.json from math-atlas's registry")
    p.add_argument("registry", help="math-atlas registry directory")
    sub.add_parser("show", help="every volume and chapter")
    sub.add_parser("where", help="the volume of the current directory")
    args = ap.parse_args(argv)
    if args.cmd == "refresh":
        old = json.loads(SERIES_JSON.read_text(encoding="utf-8")) if SERIES_JSON.exists() else {}
        data = generate(Path(args.registry), old.get("repo") or REPO.name)
        SERIES_JSON.parent.mkdir(parents=True, exist_ok=True)
        SERIES_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {SERIES_JSON}: {len(data['volumes'])} volume(s)")
        return 0
    s = Series.load()
    if not s:
        sys.exit(f"no {SERIES_JSON}")
    if args.cmd == "where":
        v = s.volume_at(Path.cwd())
        print(f"{v.prefix} ({v.id}) {v.title}" if v else "not a volume directory")
        return 0 if v else 1
    for v in s.volumes:
        here = "" if v.repo == s.name else f"  [{v.repo}]"
        print(f"{v.prefix} {v.id}: {v.title}{here}")
        for c in v.chapters:
            ab = f"  (ab ch{c['ab']})" if c.get("ab") else ""
            print(f"  Ch {c['n']:>2}  {c['id']:<7} {c['title']}{ab}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
