"""exr-checking-proofs-b2 (Ch 5, Section 5.6): x = 1, y = -1 gives |x| + |y| = 2, |x + y| = 0,
and satisfies neither case; the two cases are correct where they apply; triangle inequality."""
from fractions import Fraction as F
QUOTED = {"x": 1, "y": -1, "lhs": 2, "rhs": 0}
x, y = QUOTED["x"], QUOTED["y"]
assert abs(x) + abs(y) == QUOTED["lhs"] and abs(x + y) == QUOTED["rhs"]
assert not ((x >= 0 and y >= 0) or (x < 0 and y < 0))
pts = [F(k, 7) for k in range(-40, 41)]
for x in pts:
    for y in pts:
        if (x >= 0 and y >= 0) or (x < 0 and y < 0):
            assert abs(x) + abs(y) == abs(x + y)
        assert abs(x + y) <= abs(x) + abs(y)
print("exr-checking-proofs-b2: all quoted values check")
