"""exr-the-field-of-reals-b2 (a): |max(x, y) - max(x', y')| <= |x - x'| + |y - y'| on a grid of rationals."""
from fractions import Fraction as F
import itertools

QUOTED = {"max_inequality_holds": True}
vals = [F(k, 3) for k in range(-6, 7)]
for x, y, x2, y2 in itertools.product(vals, repeat=4):
    assert abs(max(x, y) - max(x2, y2)) <= abs(x - x2) + abs(y - y2)
print("ok")
