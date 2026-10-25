"""Tests for tools/renumber.py: one simultaneous renumbering map, applied once."""

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location("renumber", TOOLS / "renumber.py")
renumber = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renumber)

SERIES = {"repo": "foundations", "volumes": [
    {"prefix": "fd1", "id": "F1", "title": "Logic and Proof", "repo": "foundations", "dir": "fd1"},
    {"prefix": "fd2", "id": "F2", "title": "Sets and Functions", "repo": "foundations",
     "dir": "fd2"},
]}
MAP = {"fd1": {
    "chapters": {"5": "6"},
    "sections": {"3.5": "3.6", "3.6": "3.7", "3.7": "3.8", "4.11": "?", "4.12": "5.5"},
    "moves": {"src/ch05-prose": "src/ch06-prose",
              "src/ch04-predicates/12-soundness.md": "src/ch05-models/05-soundness.md"},
}}


class RenumberCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "foundations"
        (self.repo / "authoring").mkdir(parents=True)
        (self.repo / "authoring" / "series.json").write_text(json.dumps(SERIES))
        for vol in ("fd1", "fd2"):
            for sub in ("src", "authoring", "config"):
                (self.repo / vol / sub).mkdir(parents=True)
        (self.repo / "fd1" / "src" / "ch05-prose").mkdir()
        (self.repo / "fd1" / "src" / "ch04-predicates").mkdir()
        (self.repo / "fd1" / "src" / "ch04-predicates" / "12-soundness.md").write_text("# Soundness\n")
        self.map = Path(self.tmp.name) / "map.json"
        self.map.write_text(json.dumps(MAP))

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def run_map(self, dry_run=False):
        logged = []
        hits, changed, diff = renumber.run(self.map, dry_run=dry_run,
                                           series_path=self.repo / "authoring" / "series.json",
                                           out=logged.append)
        return hits, changed, diff, logged

    def read(self, rel):
        return (self.repo / rel).read_text()


class PointerTests(RenumberCase):
    def test_simultaneous_never_chained(self):
        self.write("fd1/src/ch03-a/01.md", "See Section 3.5, then Section 3.6 and Section 3.7.\n")
        self.run_map()
        self.assertEqual(self.read("fd1/src/ch03-a/01.md"),
                         "See Section 3.6, then Section 3.7 and Section 3.8.\n")

    def test_chapter_map_carries_its_sections_and_lists(self):
        self.write("fd1/src/ch01-a/01.md",
                   "Chapter 5 and Section 5.3; Chapters 1–5; Sections 5.2 and 5.7; Sections 3.5, 3.6 "
                   "and 4.12; Chapter 4 stays; Section 4.1 stays; Chapter 50 stays.\n")
        self.run_map()
        self.assertEqual(self.read("fd1/src/ch01-a/01.md"),
                         "Chapter 6 and Section 6.3; Chapters 1–6; Sections 6.2 and 6.7; Sections 3.6, 3.7 "
                         "and 5.5; Chapter 4 stays; Section 4.1 stays; Chapter 50 stays.\n")

    def test_singular_takes_one_number(self):
        self.write("fd1/src/ch01-a/01.md", "In Chapter 5, 3 examples; Section 3.5, 3.6 apples; Chapter 4.2.\n")
        self.run_map()
        self.assertEqual(self.read("fd1/src/ch01-a/01.md"),
                         "In Chapter 6, 3 examples; Section 3.6, 3.6 apples; Chapter 4.2.\n")

    def test_other_volumes_need_the_title(self):
        self.write("fd2/src/ch01-a/01.md",
                   "From *Logic and Proof*, Section 3.5 and from Logic and Proof, Chapter 5. "
                   "Our own Section 3.5 and Chapter 5 stay.\n")
        hits, _, _, _ = self.run_map()
        self.assertEqual(self.read("fd2/src/ch01-a/01.md"),
                         "From *Logic and Proof*, Section 3.6 and from Logic and Proof, Chapter 6. "
                         "Our own Section 3.5 and Chapter 5 stay.\n")
        # the plain pointers share a line with the title: flagged, not changed
        reviews = [h for h in hits if not h.new]
        self.assertEqual([h.old for h in reviews], ["Section 3.5", "Chapter 5"])
        self.assertIn("naming Logic and Proof", reviews[0].note)

    def test_a_pointer_into_an_unmapped_volume_is_not_local(self):
        self.write("fd1/src/ch01-a/01.md", "*Sets and Functions*, Chapter 5 stays; Chapter 5 moves.\n")
        self.run_map()
        self.assertEqual(self.read("fd1/src/ch01-a/01.md"),
                         "*Sets and Functions*, Chapter 5 stays; Chapter 6 moves.\n")

    def test_question_mark_is_reported_and_kept(self):
        self.write("fd1/src/ch04-a/01.md", "As Section 4.11 shows.\n")
        self.write("fd2/src/ch01-a/01.md", "See *Logic and Proof*, Section 4.11.\n")
        hits, changed, _, _ = self.run_map()
        self.assertEqual(changed, [])
        self.assertEqual(len(hits), 2)
        self.assertTrue(all(not h.new and "'?'" in h.note for h in hits))

    def test_hand_written_result_numbers_are_reported(self):
        self.write("fd1/src/ch03-a/01.md", "By Theorem 3.5.2 and Lemma 2.1.1.\n")
        self.write("fd2/src/ch01-a/01.md", "By *Logic and Proof*, Theorem 3.6.1.\n")
        hits, changed, _, _ = self.run_map()
        self.assertEqual(changed, [])
        self.assertEqual(sorted(h.old for h in hits), ["Theorem 3.5.2", "Theorem 3.6.1"])

    def test_root_authoring_and_yaml(self):
        self.write("authoring/STATUS.md", "fd1: *Logic and Proof*, Section 3.7; plain Section 3.7 stays.\n")
        self.write("fd1/authoring/ledger/ch03.yaml", "- where: Section 3.6\n")
        self.run_map()
        self.assertEqual(self.read("authoring/STATUS.md"),
                         "fd1: *Logic and Proof*, Section 3.8; plain Section 3.7 stays.\n")
        self.assertEqual(self.read("fd1/authoring/ledger/ch03.yaml"), "- where: Section 3.7\n")


class MoveAndModeTests(RenumberCase):
    def test_moves_and_paths(self):
        self.write("fd1/config/config.json", '{"chapters": ["src/ch05-prose"]}\n')
        self.write("fd2/src/ch01-a/01.md", "[soundness](../../fd1/ch04-predicates/12-soundness.html) "
                                           "and ch05-prose/01-x.md; ch05-prosed stays.\n")
        hits, _, _, logged = self.run_map()
        self.assertTrue((self.repo / "fd1/src/ch06-prose").is_dir())
        self.assertFalse((self.repo / "fd1/src/ch05-prose").exists())
        self.assertTrue((self.repo / "fd1/src/ch05-models/05-soundness.md").is_file())
        self.assertEqual(self.read("fd1/config/config.json"), '{"chapters": ["src/ch06-prose"]}\n')
        self.assertEqual(self.read("fd2/src/ch01-a/01.md"),
                         "[soundness](../../fd1/ch05-models/05-soundness.html) "
                         "and ch06-prose/01-x.md; ch05-prosed stays.\n")
        self.assertEqual(len(logged), 2)

    def test_dry_run_writes_nothing(self):
        path = self.write("fd1/src/ch03-a/01.md", "Section 3.5.\n")
        hits, changed, diff, logged = self.run_map(dry_run=True)
        self.assertEqual(path.read_text(), "Section 3.5.\n")
        self.assertTrue((self.repo / "fd1/src/ch05-prose").is_dir())
        self.assertEqual(changed, [path])
        self.assertIn("-Section 3.5.", diff)
        self.assertIn("+Section 3.6.", diff)
        self.assertEqual([str(h).split(": ", 1)[1] for h in hits], ["'Section 3.5' -> 'Section 3.6'"])

    def test_cli_check_and_report(self):
        self.write("fd1/src/ch03-a/01.md", "Section 3.5.\n")
        out = io.StringIO()
        argv = [str(self.map), "--check", "--series", str(self.repo / "authoring" / "series.json")]
        with redirect_stdout(out):
            self.assertEqual(renumber.main(argv), 1)
        self.assertIn("1 pointer(s) to rewrite in 1 file(s)", out.getvalue())
        self.assertEqual(self.read("fd1/src/ch03-a/01.md"), "Section 3.5.\n")

    def test_bad_map(self):
        self.map.write_text(json.dumps({"fd9": {}}))
        with self.assertRaises(SystemExit):
            self.run_map(dry_run=True)


if __name__ == "__main__":
    unittest.main()
