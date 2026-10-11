"""Tests for tools/pointers.py: renumbering prose and bookkeeping pointers, and the hash mask."""

import importlib.util
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location("pointers", TOOLS / "pointers.py")
pt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pt)

# analysis-book chapter -> (volume, local number, atlas id)
MAP = {n: ("fd1", n, f"F1.{n}") for n in range(1, 6)}
MAP.update({n: ("fd2", n - 5, f"F2.{n - 5}") for n in range(6, 9)})
MAP.update({9: ("fd3", 1, "F3.1"), 11: ("an1", 1, "AN1.1"), 12: ("an1", 2, "AN1.2")})
TITLES = {"fd1": "Logic and Proof", "fd2": "Sets, Relations, and Cardinality",
          "fd3": "Number Systems", "an1": "Analysis on the Real Line"}


def prose(text, here):
    return pt.rewrite_prose(text, MAP, here, TITLES)


class RewriteTests(unittest.TestCase):
    def test_same_volume_renumbered(self):
        self.assertEqual(prose("See Chapter 7 and Section 6.4.", "fd2"),
                         "See Chapter 2 and Section 1.4.")
        self.assertEqual(prose("Sections 7.5 and 7.6 then study", "fd2"),
                         "Sections 2.5 and 2.6 then study")

    def test_other_volume_named(self):
        self.assertEqual(prose("Chapter 11 states them as axioms.", "fd2"),
                         "*Analysis on the Real Line*, Chapter 1 states them as axioms.")
        self.assertEqual(prose("as in Section 4.7.", "an1"), "as in *Logic and Proof*, Section 4.7.")
        self.assertEqual(prose("Chapters 1 and 2", "fd2"), "*Logic and Proof*, Chapters 1 and 2")

    def test_range_across_volumes(self):
        self.assertEqual(prose("From Chapters 3–8: induction", "an1"),
                         "From *Logic and Proof*, Chapters 3–5, and "
                         "*Sets, Relations, and Cardinality*, Chapters 1–3: induction")
        # the volume's own part is named too when another volume is in the pointer
        self.assertEqual(prose("Chapters 1–6.", "fd2"),
                         "*Logic and Proof*, Chapters 1–5, and *Sets, Relations, and Cardinality*, Chapter 1.")

    def test_left_alone(self):
        for text in ("the linear-algebra companion, Chapter 0, whose", "\\( \\text{Chapter 11} \\)",
                     "`Chapter 11`", "Chapter 40 is not mapped", "```\nChapter 11\n```\n"):
            self.assertEqual(prose(text, "fd1"), text)

    def test_dependency_ledger_in_atlas_ids(self):
        text = "Text, Chapter 11.\n<!-- dependency ledger\nx (proof): y | ch07 (promised); Ch 4 Section 4.9\n-->\n"
        self.assertEqual(prose(text, "fd2"),
                         "Text, *Analysis on the Real Line*, Chapter 1.\n<!-- dependency ledger\n"
                         "x (proof): y | F2.2 (promised); F1.4 §09\n-->\n")

    def test_atlas(self):
        self.assertEqual(pt.rewrite_atlas("| Ch 6 §01, §02 | sets | Ch 11 (paid) |", MAP),
                         "| F2.1 §01, §02 | sets | AN1.1 (paid) |")
        self.assertEqual(pt.rewrite_atlas("Chapters 1–2 and Section 8.3", MAP), "F1.1–F1.2 and F2.3 §03")
        self.assertEqual(pt.rewrite_atlas("Tao, Analysis I, ch. 5; src/ch02-x", MAP),
                         "Tao, Analysis I, ch. 5; src/ch02-x")

    def test_refs(self):
        owner = {"thm-a": "fd1", "def-b": "fd2"}
        self.assertEqual(pt.rewrite_refs("By @thm-a and @def-b, not \\(@thm-a\\).", owner, "fd2"),
                         "By @fd1:thm-a and @def-b, not \\(@thm-a\\).")


class MaskTests(unittest.TestCase):
    def same(self, old, here):
        new = pt.rewrite_refs(prose(old, here), {"thm-a": "fd1"}, here)
        self.assertNotEqual(old, new)
        self.assertEqual(pt.mask(old), pt.mask(new), (old, new))

    def test_mask_survives_the_split(self):
        self.same("From Chapters 3–8: induction (@thm-a), and Section 6.4.", "an1")
        self.same("Chapter 7, then Chapters 1 and 2.", "fd2")
        self.same("<!-- dependency ledger\nx | Ch 4 Section 4.9; ch07\n-->", "fd2")

    def test_mask_still_sees_mathematics(self):
        self.assertNotEqual(pt.mask("Chapter 4 proves x < 1."), pt.mask("Chapter 4 proves x < 2."))


if __name__ == "__main__":
    unittest.main()
