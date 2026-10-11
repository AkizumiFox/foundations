"""exm-pair-equations and the quick check after it (Ch 6 Section 6.3)."""
from fractions import Fraction as F

QUOTED = {"x": 2, "y": 1, "2x": 4, "2y": 2, "t for the pair equation": -1}

# (x + y, x - y) = (3, 1): solve over a grid of rationals, and exactly
sols = [(x, y) for x in range(-10, 11) for y in range(-10, 11) if (x + y, x - y) == (3, 1)]
assert sols == [(QUOTED["x"], QUOTED["y"])]
assert 2 * QUOTED["x"] == QUOTED["2x"] == 3 + 1 and 2 * QUOTED["y"] == QUOTED["2y"] == 3 - 1
assert (1, 2) != (2, 1) and (1, 1) == (1, 1)
# quick check: (t^2, t) = (1, -1) only at t = -1; {t^2, t} = {1, -1} only at t = -1
ts = [F(k, 4) for k in range(-40, 41)]
assert [t for t in ts if (t * t, t) == (1, -1)] == [QUOTED["t for the pair equation"]]
assert [t for t in ts if {t * t, t} == {1, -1}] == [-1]
# (t, 1) = (1, t) only at t = 1, while {t, 1} = {1, t} always
assert [t for t in ts if (t, 1) == (1, t)] == [1]
assert all({t, 1} == {1, t} for t in ts)
print("exm-pair-equations: all quoted values check")
