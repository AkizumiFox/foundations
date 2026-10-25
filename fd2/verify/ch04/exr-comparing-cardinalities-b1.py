"""exr-comparing-cardinalities-b1: x/4 on (0,1) u (2,3); the injection j: Z -> N."""
from fractions import Fraction as F

QUOTED = {"images": ((F(0), F(1, 4)), (F(1, 2), F(3, 4)))}

(a0, b0), (a1, b1) = QUOTED["images"]
for k in range(1, 1000):
    x = F(k, 1000)
    assert a0 < x / 4 < b0 and a1 < (2 + x) / 4 < b1
assert b0 <= a1 and b1 <= 1  # the two image pieces are disjoint and inside (0, 1)


def j(k):
    return 2 * k if k >= 0 else -2 * k - 1


vals = [j(k) for k in range(-2000, 2001)]
assert all(v >= 0 for v in vals) and len(set(vals)) == len(vals)
assert set(vals) == set(range(4001))
print("ok")
