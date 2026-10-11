"""exr-excluded-middle-b1 (Ch 5, Section 5.7): the derivation of |- not-not(not-not P -> P)
has 13 lines, assumptions at lines 1, 2, 3, 8, R at line 4, not-E at line 9 citing 7 and 8,
bot-E at line 10 and no RAA. Also: not-not(not-not P -> P) takes value 1 in the Goedel
three-valued algebra while not-not P -> P takes 1/2 at P = 1/2 (illustration only)."""
import pathlib
import re
from fractions import Fraction as F

QUOTED = {"lines": 13, "assumptions": [1, 2, 3, 8], "bot_e_line": 10}

src = pathlib.Path("src/ch05-from-derivations-to-prose/07-excluded-middle.md").read_text()
blk = src.split("{#exr-excluded-middle-b1}")[1].split("\\begin{nd}")[1].split("\\end{nd}")[0]
rows = re.findall(r"\\(hypo|have)\s*\{(\d+)\}\s*\{.*?\}\s*(\\[a-z]+\{[^}]*\})?\s*$", blk, re.M)
assert len(rows) == QUOTED["lines"]
assert [int(n) for kind, n, _ in rows if kind == "hypo"] == QUOTED["assumptions"]
just = {int(n): j for _, n, j in rows}
assert just[4] == "\\r{2}" and just[9] == "\\ne{7,8}" and just[QUOTED["bot_e_line"]].startswith("\\be")
assert not any(j.startswith(("\\raa", "\\nne", "\\lem")) for j in just.values())

vals = [F(0), F(1, 2), F(1)]
neg = lambda x: F(1) if x == 0 else F(0)
imp = lambda x, y: F(1) if x <= y else y
for p in vals:
    assert neg(neg(imp(neg(neg(p)), p))) == 1
assert imp(neg(neg(F(1, 2))), F(1, 2)) == F(1, 2)
print("exr-excluded-middle-b1: all quoted values check")
