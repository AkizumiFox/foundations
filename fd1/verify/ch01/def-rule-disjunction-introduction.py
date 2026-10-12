"""def-rule-disjunction-introduction and its surroundings (Ch 1, Section 1.5): the instance
lines from x > 0, the Quick check from x = 2, and the witnesses of the two warnings
(x = -1: "x >= 0 or x < 0" true, "x >= 0" false; x = 2.5: P: x > 2, Q: x > 1, R: x > 3)."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"one-way witness": -1, "too-early witness": F(5, 2), "inclusive witness": 2,
          "side-choice witness": 2, "quick-check witness": F(1, 2),
          "derive-or-break witness": 1}

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
# side choice: premise x > 1, goal (x > 3) or (x > 0); x > 1 implies x > 0; x = 2 breaks x > 1 -> x > 3
assert all((not t > 1) or t > 0 for t in grid())
x = QUOTED["side-choice witness"]
assert x > 1 and not x > 3
# Quick check: premise 0 < x < 1, goal (x < 0) or (x < 2); x < 1 implies x < 2; x = 1/2 breaks the left side
assert all((not (0 < t < 1)) or t < 2 for t in grid())
x = QUOTED["quick-check witness"]
assert 0 < x < 1 and not x < 0
# "Derive it or break it": P and (Q or R) |- Q breaks at x = 1 with x > 0, x > 2, x < 3;
# P or Q |- Q or P cannot be broken (valid by truth table)
from _s06s07_logic import V, And, Or, classically_valid
x = QUOTED["derive-or-break witness"]
assert (x > 0 and (x > 2 or x < 3)) and not x > 2
_P, _Q, _R = V("P"), V("Q"), V("R")
assert not classically_valid([And(_P, Or(_Q, _R))], _Q)
assert classically_valid([Or(_P, _Q)], Or(_Q, _P))
print("def-rule-disjunction-introduction: all quoted values check")
