"""Tests for tools/check_structure.py, the STYLE.md section contract."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_structure.py"
spec = importlib.util.spec_from_file_location("check_structure", TOOL)
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

GOOD = """# A Section

We are here, a question is open, and this section answers it.

## First part

::: {#thm-thing}
[Thing]

A statement.
:::

::: {.idea}
Why it works.
:::

::: {.proof}
Line one.
Line two.
Line three.
Line four.
:::

::: {.warning}
A trap.
:::

::: {.check}
Is it so?
:::

::: {.solution}
Yes.
:::

## Exercises

### A. Check your understanding

::: {#exr-sec-a1}
[A1]
Do it.
:::

::: {.solution}
Done.
:::

### B. Practice

::: {#exr-sec-b1}
[B1]
Do it.
:::

::: {.solution}
Done.
:::

### C. Going deeper

::: {#exr-sec-c1}
[C1]
Do it.
:::

::: {.solution}
[Hint 1]
A tool.
:::

::: {.solution}
The real solution.
:::

<!-- dependency ledger
thm-thing (proof): 1 + 1 = 2 | inline
-->
"""


def run(text, **kw):
    fatal, advisory = cs.check_section(text, **kw)
    return [m for _, m in fatal], [m for _, m in advisory]


class SectionTests(unittest.TestCase):
    def test_good_section_has_no_fatal(self):
        fatal, advisory = run(GOOD)
        self.assertEqual(fatal, [])
        # only the word count is off in this tiny fixture
        self.assertEqual(len(advisory), 1)
        self.assertIn("words of prose on the main line", advisory[0])

    def test_missing_frame(self):
        text = GOOD.replace("We are here, a question is open, and this section answers it.\n", "")
        self.assertTrue(any("opening frame" in m for m in run(text)[0]))

    def test_check_without_sibling_solution(self):
        text = GOOD.replace("::: {.check}\nIs it so?\n:::\n\n::: {.solution}\nYes.\n:::",
                            "::: {.check}\nIs it so?\n\n::: {.solution}\nYes.\n:::\n:::")
        fatal = run(text)[0]
        self.assertTrue(any("nested inside the .check" in m for m in fatal))
        self.assertTrue(any("not followed by a sibling" in m for m in fatal))

    def test_no_warning_no_check(self):
        text = GOOD.replace("::: {.warning}\nA trap.\n:::\n", "").replace(
            "::: {.check}\nIs it so?\n:::\n\n::: {.solution}\nYes.\n:::\n", "")
        fatal = run(text)[0]
        self.assertIn("no ::: {.warning}", fatal)
        self.assertIn("no Quick check (::: {.check})", fatal)

    def test_exercise_groups(self):
        text = GOOD.replace("### B. Practice", "### B2. Practice")
        fatal, advisory = run(text)
        self.assertTrue(any("A., ### B., ### C." in m for m in fatal))
        self.assertTrue(any("unexpected ### heading" in m for m in advisory))
        self.assertTrue(any("no ## Exercises" in m for m in run(GOOD.replace("## Exercises", "## Problems"))[0]))

    def test_review_group_allowed_in_last_section_only(self):
        text = GOOD.replace("<!-- dependency", "### R. Review\n\n<!-- dependency")
        self.assertEqual(run(text, last=True)[0], [])
        self.assertTrue(any("R. Review belongs" in m for m in run(text, last=False)[1]))

    def test_exercise_needs_real_solution_not_just_hints(self):
        text = GOOD.replace("::: {.solution}\nThe real solution.\n:::\n", "")
        self.assertIn("exr-sec-c1 is not followed by a ::: {.solution} (hint rungs do not count)",
                      run(text)[0])
        text = GOOD.replace("::: {.solution}\nDone.\n:::\n\n### B.", "### B.")
        self.assertTrue(any("exr-sec-a1" in m for m in run(text)[0]))

    def test_long_proof_without_idea_is_advisory(self):
        text = GOOD.replace("::: {.idea}\nWhy it works.\n:::\n", "")
        fatal, advisory = run(text)
        self.assertEqual(fatal, [])
        self.assertTrue(any("thm-thing: proof of 4 lines" in m for m in advisory))
        self.assertFalse(any("proof of" in m for m in run(text, idea_lines=4)[1]))

    def test_dependency_ledger_is_advisory(self):
        text = GOOD.split("<!-- dependency ledger")[0]
        fatal, advisory = run(text)
        self.assertEqual(fatal, [])
        self.assertTrue(any("no dependency ledger" in m for m in advisory))
        bad = GOOD.replace("thm-thing (proof): 1 + 1 = 2 | inline", "some free text")
        self.assertTrue(any("dependency ledger line" in m for m in run(bad)[1]))

    def test_gate_section_skips_exercise_groups(self):
        gate = ("# Gate 0\n\nTwo hours, closed book.\n\n## Problems\n\n"
                "::: {#exr-gate-p1}\n[P1]\nProve it.\n:::\n\n::: {.solution}\nProof.\n:::\n")
        fatal, advisory = run(gate)
        self.assertEqual(fatal, [])
        self.assertIn("no ::: {.warning}", advisory)

    def test_colons_in_code_fences_are_ignored(self):
        text = GOOD.replace("## First part", "## First part\n\n```markdown\n::: {.check}\n```")
        self.assertEqual(run(text)[0], [])

    def test_word_count(self):
        self.assertEqual(cs.prose_words("# T\n\nOne two \\( x^2 \\) three.\n\n\\[ a = b \\]\n"), 5)


FOLD = """
::: {.second-reading title="Why it works"}
Four folded words here.

::: {.proof}
Five more folded words here.
:::
:::
"""


class SecondReadingTests(unittest.TestCase):
    """STYLE §12: folded prose is counted apart (core vs full track), folds do not nest
    and hold no heading, and the required check and warning stay on the main line."""

    def test_prose_split(self):
        text = "# T\n\nOne two three.\n" + FOLD
        self.assertEqual(cs.prose_split(text), (4, 9))        # "T" of the title counts
        self.assertEqual(cs.prose_words(text), 13)
        self.assertEqual(cs.prose_split("# T\n\nOne two.\n"), (3, 0))

    def test_budget_counts_the_main_line_only(self):
        text = GOOD.replace("## Exercises", FOLD + "\n## Exercises")
        fatal, advisory = run(text)
        self.assertEqual(fatal, [])
        words = [m for m in advisory if "words of prose" in m]
        self.assertEqual(len(words), 1)
        self.assertIn("on the main line", words[0])
        self.assertIn("9 more in second-reading folds", words[0])

    def test_reading_hours(self):
        self.assertEqual(cs.reading_hours(1600), 1.0)

    def test_nested_fold_and_heading_are_fatal(self):
        nested = FOLD.replace("Four folded words here.",
                              "::: {.second-reading}\nInner.\n:::")
        fatal = run(GOOD.replace("## Exercises", nested + "\n## Exercises"))[0]
        self.assertTrue(any("folds do not nest" in m for m in fatal))
        heading = FOLD.replace("Four folded words here.", "### A heading")
        fatal = run(GOOD.replace("## Exercises", heading + "\n## Exercises"))[0]
        self.assertTrue(any("heading inside a second-reading fold" in m for m in fatal))
        self.assertEqual(run(GOOD.replace("## Exercises", FOLD + "\n## Exercises"))[0], [])

    def test_check_and_warning_must_be_on_the_main_line(self):
        block = "::: {.warning}\nA trap.\n:::\n\n::: {.check}\nIs it so?\n:::\n\n::: {.solution}\nYes.\n:::\n"
        moved = GOOD.replace(block, "").replace(
            "## Exercises", "::: {.second-reading}\n" + block + ":::\n\n## Exercises")
        fatal = run(moved)[0]
        self.assertIn("no ::: {.warning} outside the second-reading folds", fatal)
        self.assertIn("no Quick check (::: {.check}) outside the second-reading folds", fatal)

    def test_words_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "src" / "ch01-x"
            ch.mkdir(parents=True)
            (ch / "01-a.md").write_text("# T\n\nOne two three.\n" + FOLD)
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(cs.main([str(ch), "--words"]), 0)
            self.assertIn("4 main line + 9 folded", out.getvalue())
            self.assertIn("core track", out.getvalue())


class IndexAndFilesTests(unittest.TestCase):
    INDEX = ("# Chapter\n\nStory.\n\n**What you need.** Nothing.\n\n**Time.** About 5 hours.\n\n"
             "## Roadmap\n\n- a\n\n## Named moves\n\n- b\n")

    def test_index(self):
        self.assertEqual(cs.check_index(self.INDEX), ([], []))
        fatal, _ = cs.check_index(self.INDEX.replace("## Named moves", "## Moves"))
        self.assertEqual(len(fatal), 1)
        _, advisory = cs.check_index(self.INDEX.replace("**Time.**", ""))
        self.assertEqual(len(advisory), 1)

    def test_directory_and_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "src" / "ch01-x"
            ch.mkdir(parents=True)
            (Path(tmp) / "src" / "index.md").write_text("# Preface\n")   # not a chapter: skipped
            (ch / "index.md").write_text(self.INDEX)
            (ch / "01-a.md").write_text(GOOD)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(cs.main([str(Path(tmp) / "src"), "--fatal-only"]), 0)
            (ch / "02-b.md").write_text(GOOD.replace("::: {.warning}\nA trap.\n:::\n", ""))
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(cs.main([str(Path(tmp) / "src")]), 1)
            self.assertIn("02-b.md", out.getvalue())

    def test_stub_is_advisory(self):
        self.assertTrue(cs.is_stub("# Planned Section\n\n"))
        self.assertFalse(cs.is_stub("# Planned Section\n\nOne line of prose.\n"))
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "src" / "ch05-x"
            ch.mkdir(parents=True)
            (ch / "index.md").write_text("# Planned Chapter\n")
            (ch / "01-a.md").write_text("# Planned Section\n")
            fatal, advisory = cs.find_violations(Path(tmp) / "src")
            self.assertEqual(fatal, [])
            self.assertEqual(len(advisory), 2)


if __name__ == "__main__":
    unittest.main()
