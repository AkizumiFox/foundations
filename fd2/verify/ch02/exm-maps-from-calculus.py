"""exm-maps-from-calculus (a)-(c), prp-strictly-monotone-injective's use,
and the n^2 Quick check (F2.6 §02)."""
import math
from fractions import Fraction as F

QUOTED = {"floor(0)": 0, "floor(1/2)": 0, "D(0,0,0)": (0, 0), "D(1,0,0)": (0, 0)}

# (a) identities and positivity for x < y
pts = [F(k, 4) for k in range(-24, 25)]
for x in pts:
    for y in pts:
        assert y ** 3 - x ** 3 == (y - x) * (x * x + x * y + y * y)
        assert x * x + x * y + y * y == (x + y / 2) ** 2 + F(3, 4) * y * y
        if x < y:
            assert x * x + x * y + y * y > 0 and x ** 3 < y ** 3
# cube roots (numeric)
for k in range(-50, 51):
    y = k / 7
    r = math.copysign(abs(y) ** (1 / 3), y)
    assert abs(r ** 3 - y) < 1e-9
# (b) floor
assert math.floor(0) == QUOTED["floor(0)"] and math.floor(0.5) == QUOTED["floor(1/2)"]
assert all(math.floor(n) == n for n in range(-50, 51))
# (c) D(a, b, c) = (b, 2c) matches the derivative of a + b x + c x^2
# the symmetric difference quotient is exact for quadratics, so it gives the derivative
for (a0, b0, c0) in [(1, 2, 3), (F(1, 2), -4, 7), (0, 0, -5)]:
    poly = lambda t: a0 + b0 * t + c0 * t * t
    for x0 in pts[::6]:
        hh = F(1, 3)
        assert (poly(x0 + hh) - poly(x0 - hh)) / (2 * hh) == b0 + 2 * c0 * x0
D = lambda a, b, c: (b, 2 * c)
assert D(0, 0, 0) == QUOTED["D(0,0,0)"] and D(1, 0, 0) == QUOTED["D(1,0,0)"]
for u in pts[:10]:
    for v in pts[:10]:
        assert D(0, u, v / 2) == (u, v)
# Quick check: n^2 strictly increasing on N, not injective on Z, 2 not a square
assert all(n * n < m * m for n in range(60) for m in range(n + 1, 60))
assert (-1) ** 2 == 1 ** 2
assert all(n * n != 2 for n in range(-100, 101))
assert all((n * n <= 1) if abs(n) <= 1 else (n * n >= 4) for n in range(-100, 101))
print("exm-maps-from-calculus: all quoted values check")
