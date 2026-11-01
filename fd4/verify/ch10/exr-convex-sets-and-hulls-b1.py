"""exr-convex-sets-and-hulls-b1: (1-t)a^2 + t c^2 - ((1-t)a + t c)^2 = t(1-t)(a-c)^2; (1-t) - (1-t)^2 = t(1-t).
A polynomial identity of degree <= 2 in each of a, c, t, checked exactly on a 5x5x5 grid of rationals (enough points)."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"identity": "t(1-t)(a-c)^2"}
pts = [F(k, 3) for k in range(-2, 3)]
for a, c, t in product(pts, pts, pts):
    assert (1 - t) * a**2 + t * c**2 - ((1 - t) * a + t * c)**2 == t * (1 - t) * (a - c)**2
    assert (1 - t) - (1 - t)**2 == t * (1 - t) == t - t**2
# A1 (b): (1,1), (-1,1) satisfy y <= x^2, midpoint (0,1) does not
assert 1 <= 1**2 and 1 <= (-1)**2 and not (1 <= 0**2)
print("ok")
