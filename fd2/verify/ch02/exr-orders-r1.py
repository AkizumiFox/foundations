"""exr-orders-r1: f(x) = x^2 + 4x = (x + 2)^2 - 4; f([-3,1]) = [-4,5];
f^{-1}([-3,0]) = [-4,-3] u [-1,0]; f(R) = [-4, oo); f^{-1}([-5,0]) = [-4,0] and f([-4,0]) = [-4,0]."""
from fractions import Fraction as F

QUOTED = {"image": (-4, 5), "pre": ((-4, -3), (-1, 0)), "range_min": -4, "check": (-4, 0)}

f = lambda x: x * x + 4 * x
xs = [F(k, 100) for k in range(-1000, 1001)]
assert all(f(x) == (x + 2) ** 2 - 4 for x in xs)
img = [f(x) for x in xs if -3 <= x <= 1]
assert (min(img), max(img)) == QUOTED["image"]
(a1, b1), (a2, b2) = QUOTED["pre"]
assert all((-3 <= f(x) <= 0) == (a1 <= x <= b1 or a2 <= x <= b2) for x in xs)
assert min(f(x) for x in xs) == QUOTED["range_min"]
lo, hi = QUOTED["check"]
assert all((-5 <= f(x) <= 0) == (lo <= x <= hi) for x in xs)
img2 = [f(x) for x in xs if lo <= x <= hi]
assert (min(img2), max(img2)) == (lo, hi)
print("exr-orders-r1: all quoted values check")
