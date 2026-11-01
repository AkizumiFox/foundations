"""exr-estimates-for-limits-b1: (n + 5)/2^n; 2^n >= n(n-1)/2 >= n^2/4 for n >= 2; n + 5 <= 2n for n >= 5; bound 8/n."""
from fractions import Fraction as F
import math

QUOTED = {"n0": 5, "C": 8}
for n in range(2, 400):
    assert 2 ** n >= F(n * (n - 1), 2) >= F(n * n, 4)
for n in range(QUOTED["n0"], 400):
    assert n + 5 <= 2 * n
    assert F(n + 5, 2 ** n) <= F(QUOTED["C"], n)
assert not (4 + 5 <= 2 * 4)
for eps in [F(1), F(1, 9), F(1, 500)]:
    N = max(QUOTED["n0"], math.floor(QUOTED["C"] / eps) + 1)
    assert all(F(n + 5, 2 ** n) < eps for n in range(N, N + 200))
print("ok")
