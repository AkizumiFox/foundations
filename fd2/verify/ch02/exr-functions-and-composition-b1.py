"""exr-functions-and-composition-b1 (Section 2.1): composites, the points where they agree, and h with h o g = f."""
import math
from fractions import Fraction as F

QUOTED = {"discriminant": 56, "roots": (3, 14), "h numerator": (1, 6, 13), "h denominator": 4}

f = lambda x: x * x + 1
g = lambda x: 2 * x - 3
xs = [F(k, 5) for k in range(-100, 101)]
assert all(g(f(x)) == 2 * x * x - 1 for x in xs)
assert all(f(g(x)) == 4 * x * x - 12 * x + 10 for x in xs)
assert all((g(f(x)) - f(g(x))) == -(2 * x * x - 12 * x + 11) for x in xs)
assert 12 ** 2 - 4 * 2 * 11 == QUOTED["discriminant"] == 4 * 14
for sign in (1, -1):
    r = 3 + sign * math.sqrt(14) / 2
    assert abs(2 * r * r - 12 * r + 11) < 1e-12
    assert abs(g(f(r)) - f(g(r))) < 1e-9
a, b, c = QUOTED["h numerator"]
h = lambda y: (a * y * y + b * y + c) / F(QUOTED["h denominator"])
assert all(h(y) == ((y + 3) / 2) ** 2 + 1 for y in xs)
assert all(h(g(x)) == f(x) for x in xs)
print("exr-functions-and-composition-b1: ok")
