"""exr-estimates-for-limits-a1: (c) n/(n^3 + 7) <= 1/n^2 for n >= 1; (d) |a_n| <= 5/n for n >= 10 gives N = max{10, N'}."""
from fractions import Fraction as F
import math

for n in range(1, 2000):
    assert F(n, n ** 3 + 7) <= F(1, n * n)
for eps in [F(1), F(1, 4), F(1, 300)]:
    N = max(10, math.floor(5 / eps) + 1)
    assert all(F(5, n) < eps for n in range(N, N + 500))
print("ok")
