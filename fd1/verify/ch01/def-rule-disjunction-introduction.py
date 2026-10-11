"""def-rule-disjunction-introduction and its surroundings (Ch 1, Section 1.6): the instance
lines from x > 0, the Quick check from x = 2, and the witnesses of the two warnings
(x = -1: "x >= 0 or x < 0" true, "x >= 0" false; x = 2.5: P: x > 2, Q: x > 1, R: x > 3)."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"one-way witness": -1, "too-early witness": F(5, 2), "inclusive witness": 2}

# instance lines: from x > 0, each of the three disjunctions is true
for x in grid():
    if x > 0:
        assert (x > 0 or x == 0) and (x == 0 or x > 0) and (x > 0 or x < -7)
# warning 1: the disjunction holds everywhere, its left side fails at -1
assert all(x >= 0 or x < 0 for x in grid())
x = QUOTED["one-way witness"]
assert (x >= 0 or x < 0) and not x >= 0
# warning 2 (inclusive): at x = 2 both sides of "x = 2 or x <= 5" are true
x = QUOTED["inclusive witness"]
assert x == 2 and x <= 5
# quick check: from x = 2, lines (i)-(iii) true; (iv) x >= 2 is (x > 2) or (x = 2)
assert (x == 2 or x == 3) and (x == 3 or x == 2) and (x == 2 or 1 == 0)
assert all((t >= 2) == (t > 2 or t == 2) for t in grid())
# too-early warning: premise P -> Q true everywhere; P true and R false at 2.5
assert all((not t > 2) or t > 1 for t in grid())
x = QUOTED["too-early witness"]
assert x > 2 and x > 1 and not x > 3
print("def-rule-disjunction-introduction: all quoted values check")
