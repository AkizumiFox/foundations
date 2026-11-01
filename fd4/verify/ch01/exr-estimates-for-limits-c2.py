"""exr-estimates-for-limits-c2: r^n >= C(n,3) h^3 = n(n-1)(n-2)/6 h^3; n-1 >= 3n/4, n-2 >= n/2 for n >= 4;
r^n >= n^3 h^3/16; n^2/r^n <= 16/(n h^3)."""
from fractions import Fraction as F
from math import comb
import math

QUOTED = {"n0": 4, "den": 16}
for n in range(3, 300):
    assert comb(n, 3) * 6 == n * (n - 1) * (n - 2)
for n in range(0, 300):
    assert (n - 1 >= F(3 * n, 4)) == (n >= 4)
    assert (n - 2 >= F(n, 2)) == (n >= 4)
for n in range(QUOTED["n0"], 300):
    assert n * (n - 1) * (n - 2) >= F(3 * n ** 3, 8)
    assert F(3 * n ** 3, 8 * 6) == F(n ** 3, QUOTED["den"])
for r in [F(11, 10), F(3, 2), F(2), F(5)]:
    h = r - 1
    for n in range(QUOTED["n0"], 300):
        assert r ** n >= F(n * (n - 1) * (n - 2), 6) * h ** 3 >= F(n ** 3, 16) * h ** 3
        assert F(n * n) / r ** n <= F(16) / (n * h ** 3)
    for eps in [F(1), F(1, 100)]:
        N = max(4, math.floor(16 / (h ** 3 * eps)) + 1)
        assert all(F(n * n) / r ** n < eps for n in range(N, N + 100))
print("ok")
