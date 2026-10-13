"""exr-quantifier-rhetoric-c1 (Ch 5, Section 5.2): max + min = x + y; x max{x, y} >= xy for x >= 0;
x = -1, y = -2 gives x max{x, y} = 1 < 2 = xy."""
from fractions import Fraction as Fr

QUOTED = {"counter": (-1, -2), "lhs": 1, "rhs": 2}

vals = [Fr(k, 3) for k in range(-12, 13)]
for x in vals:
    for y in vals:
        assert max(x, y) + min(x, y) == x + y
        if x >= 0:
            assert x * max(x, y) >= x * y
x, y = QUOTED["counter"]
assert x * max(x, y) == QUOTED["lhs"] and x * y == QUOTED["rhs"] and not (QUOTED["lhs"] >= QUOTED["rhs"])
print("exr-quantifier-rhetoric-c1: all quoted values check")
