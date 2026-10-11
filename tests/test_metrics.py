"""Tests for tools/metrics.py: per-chapter metrics from whatever sources exist."""

import csv
import importlib.util
import io
import json
import os
import tempfile
import unittest
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "metrics.py"
spec = importlib.util.spec_from_file_location("metrics", TOOL)
mt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mt)

SECTION = r"""# One

An opening frame of a few words.

::: {#thm-one}
[One]
A statement.
:::

::: {.proof}
Short.
:::

::: {#exm-one}
[Ex]
An example.
:::

::: {.check}
Check?
:::

::: {.solution}
Yes.
:::

## Exercises

### A.

::: {#exr-one-a1}
[A1]
Do it.
:::

::: {.solution}
Done.
:::

### C.

::: {#exr-one-c1}
[C1: Exit check: everything]
Prove it.
:::

<!-- dependency ledger
thm-one (proof): a fact | ch02 (promised)
exm-one (example): another | ch01
-->
"""

REVIEW = """# S2

| # | Location | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | §01 | x | correct | fine |
| 2 | §01 | y | **gap** | 01:3 |
| 3 | §01 | z | error (copying) | 01:4 |
"""


class MetricsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.ch = self.root / "src" / "ch03-three"
        self.ch.mkdir(parents=True)
        (self.ch / "01-one.md").write_text(SECTION)
        (self.ch / "index.md").write_text("# Three\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_size(self):
        s = mt.size_metrics(self.ch)
        self.assertEqual((s["sections"], s["results"], s["proofs"], s["examples"], s["exercises"]),
                         (1, 1, 1, 1, 2))
        self.assertEqual(s["exercise_solution_pct"], 50.0)
        self.assertEqual((s["exit_checks"], s["quick_checks"]), (1, 1))
        self.assertEqual((s["ledger_lines"], s["ledger_promised"]), (2, 1))
        self.assertEqual(s["sections_outside_budget"], 1)
        self.assertEqual(s["prose_words_folded"], 0)

    def test_folded_words(self):
        text = (self.ch / "01-one.md").read_text().replace(
            "\n## ", "\n::: {.second-reading}\nThree folded words.\n:::\n\n## ", 1)
        (self.ch / "01-one.md").write_text(text)
        s = mt.size_metrics(self.ch)
        self.assertEqual(s["prose_words_folded"], 3)
        self.assertTrue(s["words_per_section"].endswith("+3"))

    def test_review_findings_and_rates(self):
        reviews = self.root / "authoring" / "reviews"
        reviews.mkdir(parents=True)
        (reviews / "ch03-S2.md").write_text(REVIEW)
        (reviews / "ch03-S9-author.md").write_text(REVIEW.replace("**gap**", "correct"))
        (reviews / "ch03-S5-B.md").write_text(REVIEW.replace("error (copying)", "correct"))
        counts = mt.review_findings(reviews, 3)
        self.assertEqual(counts, Counter({("S2", "gap"): 1, ("S2", "error"): 1, ("S9", "error"): 1,
                                          ("S5b", "gap"): 1}))
        row = mt.findings_metrics(counts, 20000)
        self.assertEqual((row["S2_gap"], row["S2_error"], row["S9_error"]), (1, 1, 1))
        self.assertEqual(row["S5b_gap"], 1)
        self.assertEqual(row["findings_per_10k"], 2.0)
        self.assertEqual(row["escape_rate"], 0.5)
        self.assertEqual(row["blueprint_defects_s2"], 2)

    def test_degrades_without_sources(self):
        with redirect_stdout(io.StringIO()):
            row = mt.chapter_metrics(self.ch, root=self.root, src=self.root / "src",
                                     manual={"agents": "4"})
        self.assertEqual(set(row), set(mt.COLUMNS))
        self.assertEqual(row["agents"], "4")
        self.assertEqual(row["prose_words"], mt.size_metrics(self.ch)["prose_words"])
        self.assertEqual(row["forward_citations"], "")
        for note in ("no findings recorded", "crossref", "no HTML build", "no ./build.py check output"):
            self.assertIn(note, row["notes"])
        self.assertIsInstance(row["structure_fatal"], int)          # the gates still ran
        self.assertIn("git", row["notes"])                          # not a repository

    def test_seeded_recall_and_check_log(self):
        reviews = self.root / "authoring" / "reviews"
        reviews.mkdir(parents=True)
        (reviews / "ch03-seeded.json").write_text(json.dumps({"recall": 0.8}))
        log = "⚠ spelling in ch03-three/01-one.md: foo\n✖ unresolved reference @x in ch03-three/01-one.md\n"
        with redirect_stdout(io.StringIO()):
            row = mt.chapter_metrics(self.ch, root=self.root, src=self.root / "src", check_output=log)
        self.assertEqual(row["seeded_recall"], 0.8)
        self.assertEqual((row["check_errors"], row["check_warnings"]), (1, 1))

    def test_append_creates_header_then_appends(self):
        out = self.root / "authoring" / "metrics.csv"
        mt.append_rows(out, [{"chapter": "a", "prose_words": 1}])
        mt.append_rows(out, [{"chapter": "b", "prose_words": 2}])
        rows = list(csv.DictReader(out.open()))
        self.assertEqual([r["chapter"] for r in rows], ["a", "b"])
        self.assertEqual(list(rows[0]), mt.COLUMNS)

    def test_main_dry_run(self):
        cwd = os.getcwd()
        os.chdir(self.root)
        try:
            with redirect_stdout(io.StringIO()) as buf:
                mt.main(["3", "--dry-run", "--set", "hours=2"])
        finally:
            os.chdir(cwd)
        self.assertIn("hours: 2", buf.getvalue())
        self.assertFalse((self.root / "authoring" / "metrics.csv").exists())


if __name__ == "__main__":
    unittest.main()
