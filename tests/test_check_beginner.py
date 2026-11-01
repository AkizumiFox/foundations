"""tools/check_beginner.py: the mechanical half of STYLE §13."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check_beginner as cb  # noqa: E402


def kinds(findings):
    return sorted(k for _, k, _ in findings)


class TestSentences(unittest.TestCase):

    def test_two_refs_flagged_uses_line_exempt(self):
        text = ("By @thm-a and @lem-b, the claim holds.\n\n"
                "::: {.proof}\nIt follows.\n\n::: {.uses}\n@thm-a; @lem-b; @def-c.\n:::\n:::\n")
        self.assertEqual(kinds(cb.check_text(text)), ["refs"])

    def test_draft_uses_paragraph_exempt(self):
        self.assertEqual(cb.check_text("*Uses:* @thm-a (one); @lem-b (two).\n"), [])

    def test_one_ref_per_sentence_passes(self):
        self.assertEqual(cb.check_text("By @thm-a, x holds. By @lem-b, y holds.\n"), [])

    def test_long_sentence_and_displays(self):
        long = " ".join(["word"] * 36) + "."
        self.assertEqual(kinds(cb.check_text(long + "\n")), ["long"])
        short = "Then\n\\[\n" + " + ".join(["a"] * 50) + "\n\\]\nholds.\n"
        self.assertEqual(cb.check_text(short), [])

    def test_inline_math_is_one_word(self):
        # "Let" + 15 formulas + 14 "and" + "be given" = 32 words, however long the formulas
        text = "Let " + " and ".join([r"\( x_{%d} + y + z \)" % i for i in range(15)]) + " be given.\n"
        self.assertEqual(cb.check_text(text), [])

    def test_nested_parentheses(self):
        self.assertEqual(kinds(cb.check_text("This (as before (see above)) holds.\n")), ["nested"])
        self.assertEqual(cb.check_text(r"This (\( f(x) \)) holds." + "\n"), [])
        self.assertEqual(cb.check_text("Commutativity (@thm-laws (b), (c)) gives it.\n"), [])

    def test_terms(self):
        found = cb.check_text("## Named moves\n\nThe fold below has the proof.\n")
        self.assertEqual(kinds(found), ["term", "term"])
        self.assertEqual(cb.check_text("A twofold claim.\n"), [])
        self.assertEqual(kinds(cb.check_text('::: {.second-reading title="The usual failure"}\nx.\n:::\n')),
                         ["term"])

    def test_custom_terms(self):
        terms = cb.term_patterns(["widget"])
        self.assertEqual(kinds(cb.check_text("The fold. A widget.\n", terms)), ["term"])

    def test_code_alone(self):
        self.assertEqual(kinds(cb.check_text("So x ~ z by (Eq3).\n")), ["code"])
        self.assertEqual(cb.check_text("So x ~ z by transitivity, (Eq3).\n"), [])

    def test_code_fences_comments_and_raw_latex_skipped(self):
        text = ("```python\nx = 1; y = 2; z = 3; w = 4\n```\n\n"
                "<!-- dependency ledger\nthm-a (proof): fold, ledger | x\n-->\n\n"
                "\\begin{center}\n" + " ".join(["w"] * 50) + "\n\\end{center}\n")
        self.assertEqual(cb.check_text(text), [])

    def test_abbreviations_and_roman_items(self):
        text = "Take e.g. the set A. (i) It is finite. (ii) It is small.\n"
        self.assertEqual(len(cb.sentences(text)), 3)


class TestIndex(unittest.TestCase):

    def test_index_parts_and_time_line(self):
        text = ("# Chapter\n\nStory.\n\n**What you need.** @a-1, @b-2, @c-3, @d-4, @e-5, @f-6.\n\n"
                "**Time.** About 40 hours on the core track (all of A, one B and one C per section, "
                "the exit checks); about 60 hours for everything.\n\n"
                "## Named moves\n\n- x\n\n## Summary\n\nDone.\n\n## Terms\n\n- y\n")
        k = kinds(cb.check_index(text))
        for want in ("time-line", "need", "index-part"):
            self.assertIn(want, k)
        self.assertEqual(k.count("index-part"), 3)

    def test_clean_index(self):
        text = ("# Chapter\n\nStory.\n\n**What you need.** Chapter 1 (@thm-a).\n\n"
                "**Time.** About 40 hours if you read the main text and do every A exercise and one B "
                "and one C exercise per section; about 60 hours for everything.\n")
        self.assertEqual(cb.check_index(text), [])


class TestFiles(unittest.TestCase):

    def test_find_and_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            chapter = Path(tmp) / "src" / "ch01-x"
            chapter.mkdir(parents=True)
            (chapter / "01-a.md").write_text("# A\n\nBy @thm-a and @thm-b, done.\n")
            (chapter / "review.md").write_text("# Chapter Review\n\n## Terms\n\n- **x**: @def-x, @def-y.\n")
            found = cb.find_findings(Path(tmp) / "src")
            self.assertEqual([(Path(p).name, k) for p, _, k, _ in found], [("01-a.md", "refs")])
            self.assertIn("| ch01-x | 1 | 1 |", cb.summary(found, Path(tmp)))

    def test_strict_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            chapter = Path(tmp) / "src" / "ch01-x"
            chapter.mkdir(parents=True)
            (chapter / "01-a.md").write_text("# A\n\nBy @thm-a and @thm-b, done.\n")
            src = str(Path(tmp) / "src")
            self.assertEqual(cb.main([src, "--summary"]), 0)
            self.assertEqual(cb.main([src, "--strict", "--summary"]), 1)


if __name__ == "__main__":
    unittest.main()
