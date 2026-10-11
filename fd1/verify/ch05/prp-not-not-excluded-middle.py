"""prp-not-not-excluded-middle (Ch 5, Section 5.7): the meta-claims about its derivation.
8 lines; boxes close by not-I at lines 5 and 8; or-I at 3, 6; not-E at 4, 7; no RAA, no bot-E;
lines 1-7 equal lines 1-7 of prp-excluded-middle (Ch 2) line for line, line 8 differs
(RAA there, not-I here). Also a three-valued sanity check: not-not(P or not-P) has value 1 in
the Goedel three-valued algebra (0 < 1/2 < 1, not x = 1 if x = 0 else 0) where P or not-P
has value 1/2 at P = 1/2 (an illustration of the remark, not a proof)."""
import pathlib
import re
from fractions import Fraction as F

QUOTED = {"lines": 8, "close_lines": (5, 8)}

LINE = re.compile(r"\\(hypo|have)\s*\{(\d+)\}\s*\{(.*?)\}\s*(\\[a-z]+\{[^}]*\})?\s*$", re.M)


def nd_lines(text, label):
    blk = text.split(label)[1].split("\\begin{nd}")[1].split("\\end{nd}")[0]
    return [(int(n), f.strip(), (j or "").strip()) for _, n, f, j in LINE.findall(blk)]


ch5 = pathlib.Path("src/ch05-from-derivations-to-prose/07-excluded-middle.md").read_text()
ch2 = pathlib.Path("src/ch02-negation-and-classical-logic/05-reductio-and-classical-rules.md").read_text()
mine = nd_lines(ch5, "{#prp-not-not-excluded-middle .optional}")
theirs = nd_lines(ch2, "{#prp-excluded-middle}")
assert len(mine) == QUOTED["lines"] == len(theirs)
assert mine[:7] == theirs[:7], (mine[:7], theirs[:7])
assert mine[7][2].startswith("\\ni") and theirs[7][2].startswith("\\raa")
assert [n for n, _, j in mine if j.startswith("\\ni")] == list(QUOTED["close_lines"])
assert [n for n, _, j in mine if j.startswith("\\oi")] == [3, 6]
assert [n for n, _, j in mine if j.startswith("\\ne")] == [4, 7]
assert not any(j.startswith(("\\raa", "\\be", "\\nne", "\\lem")) for _, _, j in mine)

# Goedel three-valued algebra
vals = [F(0), F(1, 2), F(1)]
neg = lambda x: F(1) if x == 0 else F(0)
for p in vals:
    assert neg(neg(max(p, neg(p)))) == 1
assert max(F(1, 2), neg(F(1, 2))) == F(1, 2)
print("prp-not-not-excluded-middle: all quoted values check")
