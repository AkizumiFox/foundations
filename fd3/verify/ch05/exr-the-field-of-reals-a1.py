"""exr-the-field-of-reals-a1 (c): the split for a = 2 + 1/(n+1), a' = 2, b = x_n, b' = d_n, and the bounds 3 and 2."""
from fractions import Fraction as F
from math import isqrt

QUOTED = {"bound_a": 3, "bound_d": 2}
x = [F(2)]
for _ in range(9):
    x.append((x[-1] ** 2 + 2) / (2 * x[-1]))
for n in range(10):
    d = F(isqrt(2 * 10 ** (2 * n)), 10 ** n)
    a, a2, b, b2 = 2 + F(1, n + 1), F(2), x[n], d
    assert a * b - a2 * b2 == a * (b - b2) + F(1, n + 1) * d
    assert abs(a) <= QUOTED["bound_a"] and 1 <= d < QUOTED["bound_d"]
print("ok")
