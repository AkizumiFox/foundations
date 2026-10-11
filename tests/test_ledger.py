"""Tests for tools/ledger.py: items, content hashes, verdicts and staleness.

The pure functions need no YAML and run everywhere; the command-line round trip
needs PyYAML and runs under the repo's .venv/bin/python when it exists.
"""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "ledger.py"
VENV = ROOT / ".venv" / "bin" / "python"
if not VENV.exists():               # any interpreter with PyYAML will do
    try:
        import sys
        import yaml  # noqa: F401
        VENV = Path(sys.executable)
    except ImportError:
        pass
spec = importlib.util.spec_from_file_location("ledger", TOOL)
ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger)

SECTION = """# S

Frame.

::: {#def-thing}
[Thing]
A thing is.
:::

::: {#thm-thing}
[Thing theorem]
Things exist.
:::

::: {.proof}
Because.

::: {.claim}
Inner.
:::

::: {.proof}
Nested proof, part of the outer one.
:::
:::

::: {.check}
Is it?
:::

::: {.solution}
Yes.
:::

::: {#exr-s-a1}
[A1]
Do it.
:::

::: {.solution}
Done.
:::
"""


class PureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ch = Path(self.tmp.name) / "src" / "ch03-three"
        self.ch.mkdir(parents=True)
        (self.ch / "01-s.md").write_text(SECTION)

    def tearDown(self):
        self.tmp.cleanup()

    def items(self):
        return ledger.extract_items(self.ch)

    def test_extract(self):
        got = [(i["key"], i["kind"]) for i in self.items()]
        self.assertEqual(got, [("def-thing", "def"), ("thm-thing", "thm"),
                               ("proof:thm-thing", "proof"), ("check:01-s:1", "check"),
                               ("exr-s-a1", "exr")])

    def test_solution_is_part_of_exercise_hash(self):
        before = {i["key"]: i["hash"] for i in self.items()}
        (self.ch / "01-s.md").write_text(SECTION.replace("Done.", "Done differently."))
        after = {i["key"]: i["hash"] for i in self.items()}
        self.assertNotEqual(before["exr-s-a1"], after["exr-s-a1"])
        self.assertEqual(before["thm-thing"], after["thm-thing"])

    def test_verdicts_go_stale(self):
        items = self.items()
        led, added, removed = ledger.refresh({}, items)
        self.assertEqual((len(added), removed), (5, []))
        ledger.add_verdict(led, items, "proof:thm-thing", "S5a", "correct", "refA", today="2026-01-01")
        with self.assertRaises(ValueError):
            ledger.add_verdict(led, items, "thm-thing", "S5a", "gap", "refA")   # no evidence
        with self.assertRaises(KeyError):
            ledger.add_verdict(led, items, "thm-nope", "S5a", "correct", "refA")
        self.assertEqual(ledger.stale_items(led, items), [])
        (self.ch / "01-s.md").write_text(SECTION.replace("Because.", "Because, indeed."))
        items2 = self.items()
        stale = ledger.stale_items(led, items2)
        self.assertEqual([k for k, _ in stale], ["proof:thm-thing"])
        s = ledger.summarize(led, items2)
        self.assertEqual((s["reviewed"], s["correct"], s["stale"]), (1, 1, 1))

    def test_refresh_keeps_verdicts_and_removed_items(self):
        items = self.items()
        led, _, _ = ledger.refresh({}, items)
        ledger.add_verdict(led, items, "def-thing", "S5b", "minor", "refB", evidence="01:5 wording")
        (self.ch / "01-s.md").write_text(SECTION.replace("{#def-thing}", "{#def-object}"))
        led, added, removed = ledger.refresh(led, self.items())
        self.assertEqual((added, removed), (["def-object"], ["def-thing"]))
        gone = next(e for e in led["items"] if e["key"] == "def-thing")
        self.assertTrue(gone["removed"])
        self.assertEqual(gone["verdicts"][0]["verdict"], "minor")
        self.assertIn(("def-thing", "no longer in the source"), ledger.stale_items(led, self.items()))


USAGE_SECTION = """# S

## Sets of numbers

::: {#def-naturals}
[Natural numbers]
The natural numbers are $\\mathbb{N} = \\{1, 2, 3, \\dots\\}$. A set is non-empty
if it has an element, and $n \\le m$ iff $m - n \\ge 0$. Sums, products and powers of
natural numbers are natural numbers. A map that is onto is a surjection; $P \\iff Q$.
:::

::: {#thm-order}
[Order]
Every non-empty set of natural numbers has a least element.

### Proof sketch

Take $n \\le m$, or $n > m$.
:::
"""


class UsageHashTests(unittest.TestCase):
    """content_hash ignores the English usage migration but not a mathematical edit."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ch = Path(self.tmp.name) / "src" / "ch11-numbers"
        self.ch.mkdir(parents=True)
        self.write(USAGE_SECTION)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, text):
        (self.ch / "01-s.md").write_text(text)

    def hashes(self, text=None):
        if text is not None:
            self.write(text)
        return {i["key"]: i["hash"] for i in ledger.extract_items(self.ch)}

    def assertSameHashes(self, edited):
        before = self.hashes(USAGE_SECTION)
        self.assertNotEqual(edited, USAGE_SECTION)
        self.assertEqual(self.hashes(edited), before)

    def assertChanged(self, edited, key):
        before = self.hashes(USAGE_SECTION)
        self.assertNotEqual(self.hashes(edited)[key], before[key])

    def test_nonempty(self):
        self.assertSameHashes(USAGE_SECTION.replace("non-empty", "nonempty"))

    def test_serial_comma(self):
        self.assertSameHashes(USAGE_SECTION.replace("products and powers", "products, and powers"))

    def test_iff(self):
        self.assertSameHashes(USAGE_SECTION.replace(" iff ", " if and only if "))

    def test_onto(self):
        self.assertSameHashes(USAGE_SECTION.replace("is onto", "is surjective"))

    def test_kept_heading_anchor(self):
        edited = USAGE_SECTION.replace("### Proof sketch", "### Proof sketch {#proof-sketch}")
        self.assertSameHashes(edited)

    def test_the_whole_migration_at_once(self):
        edited = (USAGE_SECTION.replace("non-empty", "nonempty")
                  .replace(" iff ", " if and only if ")
                  .replace("products and", "products, and")
                  .replace("is onto", "is surjective"))
        self.assertSameHashes(edited)

    def test_div_identifier_is_not_a_heading_anchor(self):
        self.assertIn("thm-least", self.hashes(USAGE_SECTION.replace("{#thm-order}", "{#thm-least}")))

    def test_iff_macro_is_not_the_word(self):
        self.assertChanged(USAGE_SECTION.replace("P \\iff Q", "P \\implies Q"), "def-naturals")

    def test_naturals_with_zero(self):
        edited = USAGE_SECTION.replace("\\{1, 2, 3, \\dots\\}", "\\{0, 1, 2, \\dots\\}")
        self.assertChanged(edited, "def-naturals")

    def test_inequality(self):
        self.assertChanged(USAGE_SECTION.replace("$m - n \\ge 0$", "$m - n > 0$"), "def-naturals")
        self.assertChanged(USAGE_SECTION.replace("or $n > m$", "or $n \\ge m$"), "thm-order")

    def test_rehash_carries_only_current_verdicts(self):
        items = ledger.extract_items(self.ch)
        led, _, _ = ledger.refresh({}, items)
        by_key = {it["key"]: it for it in items}
        # Verdicts as the old code recorded them: on the raw hash.
        for key in ("def-naturals", "thm-order"):
            led_entry = next(e for e in led["items"] if e["key"] == key)
            led_entry["hash"] = by_key[key]["raw_hash"]
            led_entry["verdicts"] = [{"stage": "S5a", "verdict": "correct", "by": "refA",
                                      "hash": by_key[key]["raw_hash"]}]
        # thm-order's verdict was on an earlier text: stale before, so stale after.
        stale_v = next(e for e in led["items"] if e["key"] == "thm-order")["verdicts"][0]
        stale_v["hash"] = "0123456789ab"
        self.assertNotEqual(by_key["def-naturals"]["raw_hash"], by_key["def-naturals"]["hash"])
        self.assertEqual(sorted(k for k, _ in ledger.stale_items(led, items)),
                         ["def-naturals", "thm-order"])
        self.assertEqual(ledger.rehash(led, items), 1)
        self.assertEqual([k for k, _ in ledger.stale_items(led, items)], ["thm-order"])
        self.assertEqual(stale_v["hash"], "0123456789ab")
        entry = next(e for e in led["items"] if e["key"] == "def-naturals")
        self.assertEqual(entry["hash"], by_key["def-naturals"]["hash"])
        self.assertEqual(ledger.rehash(led, items), 0)          # idempotent


@unittest.skipUnless(VENV.exists(), "needs the repo's .venv (PyYAML)")
class CliTests(unittest.TestCase):
    def run_cli(self, *args, cwd):
        return subprocess.run([str(VENV), str(TOOL), "--src", "src", "--dir", "led", *args],
                              cwd=cwd, capture_output=True, text=True)

    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "src" / "ch03-three"
            ch.mkdir(parents=True)
            (ch / "01-s.md").write_text(SECTION)
            r = self.run_cli("init", "3", cwd=tmp)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((Path(tmp) / "led" / "ch03.yaml").exists())
            r = self.run_cli("set", "3", "thm-thing", "--stage", "S5a", "--verdict", "correct",
                             "--by", "refA", cwd=tmp)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(self.run_cli("stale", "3", cwd=tmp).returncode, 0)
            (ch / "01-s.md").write_text(SECTION.replace("Things exist.", "Things exist twice."))
            r = self.run_cli("stale", "3", cwd=tmp)
            self.assertEqual(r.returncode, 1)
            self.assertIn("thm-thing", r.stdout)
            r = self.run_cli("summary", cwd=tmp)
            self.assertIn("ch03: 5 items, 1 reviewed", r.stdout)
            r = self.run_cli("set", "3", "thm-thing", "--stage", "S5a", "--verdict", "error",
                             "--by", "refA", cwd=tmp)
            self.assertNotEqual(r.returncode, 0)

    def test_rehash(self):
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "src" / "ch03-three"
            ch.mkdir(parents=True)
            text = SECTION.replace("Things exist.", "Non-empty things exist.")
            (ch / "01-s.md").write_text(text)
            self.assertEqual(self.run_cli("init", "3", cwd=tmp).returncode, 0)
            r = self.run_cli("set", "3", "thm-thing", "--stage", "S5a", "--verdict", "correct",
                             "--by", "refA", cwd=tmp)
            self.assertEqual(r.returncode, 0, r.stderr)
            # Make the ledger look as if written before normalization: the raw hash.
            item = next(it for it in ledger.extract_items(ch) if it["key"] == "thm-thing")
            self.assertNotEqual(item["raw_hash"], item["hash"])
            path = Path(tmp) / "led" / "ch03.yaml"
            path.write_text(path.read_text().replace(item["hash"], item["raw_hash"]))
            self.assertEqual(self.run_cli("stale", "3", cwd=tmp).returncode, 1)
            r = self.run_cli("rehash", cwd=tmp)               # every ledger
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("1 verdict(s) rehashed", r.stdout)
            self.assertNotIn(item["raw_hash"], path.read_text())
            self.assertEqual(self.run_cli("stale", "3", cwd=tmp).returncode, 0)
            r = self.run_cli("rehash", "3", cwd=tmp)          # one chapter; idempotent
            self.assertIn("0 verdict(s) rehashed", r.stdout)
            r = self.run_cli("rehash", "5", cwd=tmp)          # no such ledger
            self.assertIn("no ledger, skipped", r.stdout)
            (Path(tmp) / "led" / "ch07.yaml").write_text("chapter: 7\nitems: []\n")
            r = self.run_cli("rehash", "7", cwd=tmp)          # ledger without a chapter dir
            self.assertIn("not found, skipped", r.stdout)


class PointerMaskTests(unittest.TestCase):
    """Renumbering pointers or prefixing a reference with its book does not stale a verdict."""

    def test_pointer_edits_keep_the_hash(self):
        old = ("::: {#thm-x}\n[X]\nBy @thm-a, as Chapter 6 and Section 6.4 show (§02).\n:::\n")
        new = ("::: {#thm-x}\n[X]\nBy @fd1:thm-a, as Chapter 1 and *Logic and Proof*, "
               "Section 4.4 show (§02).\n:::\n")
        self.assertEqual(ledger.content_hash(old), ledger.content_hash(new))
        self.assertNotEqual(ledger.content_hash(old), ledger.content_hash(old.replace("By", "Not by")))

    def test_rehash_carries_unmasked_verdicts(self):
        with tempfile.TemporaryDirectory() as tmp:
            ch = Path(tmp) / "ch06-x"
            ch.mkdir()
            (ch / "01-s.md").write_text("# S\n\n::: {#thm-x}\n[X]\nAs Chapter 4 shows.\n:::\n")
            items = ledger.extract_items(ch)
            it = items[0]
            self.assertNotEqual(it["usage_hash"], it["hash"])
            led, _, _ = ledger.refresh({}, items)
            led["items"][0]["verdicts"] = [{"stage": "S5a", "verdict": "correct", "by": "r",
                                            "hash": it["usage_hash"]}]
            self.assertEqual(len(ledger.stale_items(led, items)), 1)
            self.assertEqual(ledger.rehash(led, items), 1)
            self.assertEqual(ledger.stale_items(led, items), [])


if __name__ == "__main__":
    unittest.main()
