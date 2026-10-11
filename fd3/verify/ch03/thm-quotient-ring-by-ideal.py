"""thm-quotient-ring-by-ideal: the warning on Z inside Q (and the non-example 1/2 not in Z)."""
from fractions import Fraction as F

QUOTED = {"x": F(1, 2), "x2": F(3, 2), "y": F(1, 2), "p1": F(1, 4), "p2": F(3, 4), "diff": F(1, 2)}
is_int = lambda q: q.denominator == 1
assert is_int(QUOTED["x2"] - QUOTED["x"])           # [1/2] = [3/2]
assert QUOTED["x"] * QUOTED["y"] == QUOTED["p1"]
assert QUOTED["x2"] * QUOTED["y"] == QUOTED["p2"]
assert QUOTED["p2"] - QUOTED["p1"] == QUOTED["diff"] and not is_int(QUOTED["diff"])
# 2m = 1 has no integer solution (1 is odd): 1 = 2*0 + 1
assert 1 == 2 * 0 + 1 and all(2 * m != 1 for m in range(-100, 101))
# the sum on Q/Z is well defined on a sample
for a in range(-6, 7):
    for b in range(1, 5):
        for k in range(-3, 4):
            x, xp = F(a, b), F(a, b) + k
            for y in (F(1, 3), F(-5, 2), F(7, 4)):
                assert is_int((x + y) - (xp + y))
print("thm-quotient-ring-by-ideal: ok")
