"""Tests for tools/promises.py: forward pointers in prose, reconciled with STATUS.md.

PromiseTests: a plain book (no series map), chapters named by number as before the split.
SeriesPromiseTests: two volumes of a series, chapters named by atlas id, pointers into
another volume written "*Title*, Chapter N".
"""

import importlib.util
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent / "tools"


def load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pr = load("promises")
series = load("series")

STATUS = """# Status

## Forward promises

| From | Promise | Target |
|---|---|---|
| Ch 3 §01 | quantifiers | Ch 4 |
| Ch 3 index | limits | Ch 9, Ch 10 (paid) |

## Other
"""


class PromiseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.src = root / "src"
        ch3 = self.src / "ch03-three"
        ch4 = self.src / "ch04-four"
        ch3.mkdir(parents=True)
        ch4.mkdir(parents=True)
        (ch3 / "index.md").write_text("# Three\n\nChapters 9–10 do limits.\n")
        (ch3 / "01-a.md").write_text(
            "# A\n\n"
            "Chapter 4 proves this. Chapter 2 did that.\n"                  # 4 forward, 2 back
            "The linear-algebra companion, Chapter 7, has it.\n"          # companion: ignored
            "Section 3.2 does more, and §01 is here, and §03 is missing.\n"  # 3.2 fwd, §03 fwd
            "Chapter 4 proves it (@thm-four).\n"                           # linked: not a promise
            "Math \\( \\text{Chapter 12} \\) is ignored.\n"
            "```\nChapter 11 in code\n```\n")
        (ch3 / "02-b.md").write_text("# B\n\nChapter 5 and Chapter 6, see Chapter 5.\n")
        (ch4 / "01-x.md").write_text("# X\n\n::: {#thm-four}\n[Four]\nS.\n:::\n")
        self.status = root / "STATUS.md"
        self.status.write_text(STATUS)
        self.ctx = pr.Context(series.Series({}))

    def tearDown(self):
        self.tmp.cleanup()

    def found(self):
        return sorted((p.file.split("/")[1], p.line, p.target, p.target_section)
                      for p in pr.find_promises(self.src, self.ctx))

    def test_find(self):
        self.assertEqual(self.found(), [
            ("01-a.md", 3, "4", None),
            ("01-a.md", 5, "3", 2),
            ("01-a.md", 5, "3", 3),
            ("02-b.md", 3, "5", None),
            ("02-b.md", 3, "6", None),
            ("index.md", 3, "10", None),
            ("index.md", 3, "9", None),
        ])

    def test_expand_ranges(self):
        self.assertEqual(pr.expand("2", "–5"), [2, 3, 4, 5])
        self.assertEqual(pr.expand("2", " and 4"), [2, 4])

    def test_parse_status(self):
        rows = pr.parse_status(self.status)
        self.assertEqual(len(rows), 2)
        self.assertEqual((rows[0].chapter, rows[0].sections, rows[0].targets), ("3", {"01"}, {"4"}))
        self.assertEqual((rows[1].sections, rows[1].targets, rows[1].paid), ({"index"}, {"9", "10"}, True))

    def test_reconcile(self):
        missing = pr.reconcile(pr.find_promises(self.src, self.ctx), pr.parse_status(self.status),
                               pr.existing_sections(self.src, self.ctx))
        got = sorted((p.file.split("/")[1], p.target, p.target_section) for p, _ in missing)
        # §02 of ch03 exists (paid in-chapter); §03 does not; Ch 5 and 6 have no rows
        self.assertEqual(got, [("01-a.md", "3", 3), ("02-b.md", "5", None), ("02-b.md", "6", None)])

    def test_cli(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(pr.main(["--src", str(self.src), "--status", str(self.status), "--for", "4"]), 0)
        self.assertIn("must pay 1 prose promise", out.getvalue())
        self.assertIn("| Ch 3 §01 |", out.getvalue())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(pr.main(["--src", str(self.src), "--status", str(self.status),
                                      "--reconcile"]), 1)


SERIES = {
    "repo": "demo",
    "volumes": [
        {"prefix": "fd1", "id": "F1", "title": "Logic and Proof", "repo": "demo", "dir": "fd1",
         "chapters": [{"n": 1, "id": "F1.1", "title": "A"}, {"n": 2, "id": "F1.2", "title": "B"}]},
        {"prefix": "fd2", "id": "F2", "title": "Sets, Relations, and Cardinality", "repo": "demo",
         "dir": "fd2", "chapters": [{"n": 1, "id": "F2.1", "title": "C"}, {"n": 2, "id": "F2.2", "title": "D"}]},
        {"prefix": "an1", "id": "AN1", "title": "Analysis on the Real Line", "repo": "other", "dir": "an1",
         "chapters": [{"n": 1, "id": "AN1.1", "title": "E"}]},
    ],
}

SERIES_STATUS = """# Status

## Forward promises

| From | Promise | Target |
|---|---|---|
| F1.1 §01 | sets | F2.1 |
| F1.2 | the axioms | AN1.1 (paid) |
"""


class SeriesPromiseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = root = Path(self.tmp.name) / "demo"
        (root / "authoring").mkdir(parents=True)
        (root / "authoring" / "series.json").write_text(json.dumps(SERIES))
        (root / "authoring" / "STATUS.md").write_text(SERIES_STATUS)
        self.s = series.Series.load(root / "authoring" / "series.json")
        f1 = root / "fd1" / "src" / "ch01-a"
        f12 = root / "fd1" / "src" / "ch02-b"
        f2 = root / "fd2" / "src" / "ch01-c"
        for d in (f1, f12, f2):
            d.mkdir(parents=True)
        (f1 / "01-x.md").write_text(
            "# X\n\n"
            "*Sets, Relations, and Cardinality*, Chapter 1 defines sets.\n"   # forward, other volume
            "Chapter 2 comes next, and Section 2.1 too.\n"                    # forward, this volume
            "*Analysis on the Real Line*, Chapter 1 has the axioms.\n"        # forward, other repo
            "*Analysis on the Real Line*, Chapter 1 again (@an1:ax-lub).\n"   # linked by prefix
            "*Some Other Book*, Chapter 3 is not ours.\n")                    # unknown title: ignored
        (f12 / "01-y.md").write_text("# Y\n\n*Analysis on the Real Line*, Chapter 1 states them.\n")
        (f2 / "01-z.md").write_text(
            "# Z\n\n"
            "*Logic and Proof*, Chapter 2 did that.\n"                        # back: a recall
            "*Logic and Proof*, Chapters 1–2 and Chapter 2 follow.\n")        # back, and forward F2.2
        self.ctx = pr.Context(self.s)
        self.cwd = os.getcwd()

    def tearDown(self):
        os.chdir(self.cwd)
        self.tmp.cleanup()

    def promises(self, prefix):
        v = self.s.by_prefix[prefix]
        return pr.find_promises(self.root / prefix / "src", self.ctx, v, f"{prefix}/")

    def test_ids_and_order(self):
        self.assertEqual(self.s.atlas_id("fd2", 1), "F2.1")
        self.assertEqual(self.s.locate("AN1.1"), ("an1", 1))
        self.assertLess(self.s.order_key("F1.2"), self.s.order_key("F2.1"))
        self.assertEqual(self.s.volume_by_title("*Logic and Proof*").prefix, "fd1")
        self.assertEqual(self.s.volume_at(self.root / "fd2").prefix, "fd2")

    def test_volume_dir_in_a_sibling_checkout(self):
        """Another repository's volume is found in its checkout directory beside this one."""
        self.assertIsNone(self.s.volume_dir("an1"))             # ../other/an1 is absent
        data = json.loads(json.dumps(SERIES))
        data["volumes"][2]["checkout"] = "other-series"
        s = series.Series(data, self.root)
        (self.root.parent / "other" / "an1").mkdir(parents=True)  # the wrong directory
        self.assertIsNone(s.volume_dir("an1"))
        (self.root.parent / "other-series" / "an1" / "src" / "ch01-e").mkdir(parents=True)
        self.assertEqual(s.volume_dir("an1"), self.root.parent / "other-series" / "an1")
        self.assertEqual(s.chapter_dir("AN1.1").name, "ch01-e")
        self.assertEqual(s.volume_dir("fd2"), self.root / "fd2")
        gen = series.generate.__defaults__[-1]
        self.assertEqual(gen["analysis"], "analysis-series")

    def test_find_across_volumes(self):
        got = sorted(((p.file, p.chapter, p.target, p.target_section) for p in self.promises("fd1")),
                     key=lambda t: (t[0], t[2], t[3] or 0))
        self.assertEqual(got, [
            ("fd1/ch01-a/01-x.md", "F1.1", "AN1.1", None),
            ("fd1/ch01-a/01-x.md", "F1.1", "F1.2", None),
            ("fd1/ch01-a/01-x.md", "F1.1", "F1.2", 1),
            ("fd1/ch01-a/01-x.md", "F1.1", "F2.1", None),
            ("fd1/ch02-b/01-y.md", "F1.2", "AN1.1", None),
        ])
        got = [(p.chapter, p.target) for p in self.promises("fd2")]
        self.assertEqual(got, [("F2.1", "F2.2")])

    def test_status_and_reconcile(self):
        rows = pr.parse_status(self.root / "authoring" / "STATUS.md")
        self.assertEqual([(r.chapter, r.targets, r.paid) for r in rows],
                         [("F1.1", {"F2.1"}, False), ("F1.2", {"AN1.1"}, True)])
        missing = pr.reconcile(self.promises("fd1"), rows, set(), self.ctx)
        self.assertEqual(sorted((p.target, why.split(" ")[0]) for p, why in missing),
                         [("AN1.1", "no"), ("F1.2", "no"), ("F1.2", "no")])

    def test_cli_in_a_volume(self):
        os.chdir(self.root)
        tools_series = series.SERIES_JSON
        try:
            series.SERIES_JSON = self.root / "authoring" / "series.json"
            pr.series_mod.SERIES_JSON = series.SERIES_JSON
            pr.series_mod.REPO = self.root
            out = io.StringIO()
            with redirect_stdout(out):
                pr.main(["--book", "fd2", "--for", "2", "--status", "../authoring/STATUS.md"])
            self.assertIn("F2.2 (fd2 Ch 2) must pay 1 prose promise", out.getvalue())
        finally:
            series.SERIES_JSON = tools_series
            pr.series_mod.SERIES_JSON = tools_series
            pr.series_mod.REPO = tools_series.parent.parent


if __name__ == "__main__":
    unittest.main()
