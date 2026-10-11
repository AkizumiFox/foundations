"""The series' macro file parses as the engine reads it (the engine's own parser tests are in
engine/tests/test_macros.py)."""

import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINE = Path(os.environ.get("BOOK_ENGINE") or ROOT / "engine").expanduser().resolve()
sys.path.insert(0, str(ENGINE))


class TestBookMacros(unittest.TestCase):
    def test_project_macro_file_parses(self):
        if not (ENGINE / "build" / "macros.py").is_file():
            self.skipTest("no engine (git submodule update --init, or set BOOK_ENGINE)")
        from build.macros import mathjax_macros
        macros_file = ROOT / "latex" / "macros.tex"
        if not macros_file.exists():
            self.skipTest("no latex/macros.tex")
        macros = mathjax_macros(macros_file)
        self.assertEqual(macros["v"], r"\mathbf{v}")
        self.assertEqual(macros["nQ"], r"\mathbb{Q}")
        self.assertEqual(macros["norm"][1], 1)


if __name__ == "__main__":
    unittest.main()
