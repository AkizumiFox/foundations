"""exr-estimates-for-limits-c1: |(3n^2 - n)/(n^2 + 4) - 3| = (n + 12)/(n^2 + 4) <= 13/n for n >= 1."""
from fractions import Fraction as F
import math

QUOTED = {"C": 13, "n0": 1}
for n in range(0, 3000):
    d = F(3 * n * n - n, n * n + 4) - 3
    assert d == F(-(n + 12), n * n + 4)
for n in range(QUOTED["n0"], 3000):
    assert n + 12 <= 13 * n
    assert F(n + 12, n * n + 4) <= F(QUOTED["C"], n)
for eps in [F(1), F(1, 13), F(1, 1000)]:
    N = math.floor(QUOTED["C"] / eps) + 1
    assert N >= 1 and all(abs(F(3 * n * n - n, n * n + 4) - 3) < eps for n in range(N, N + 500))
print("ok")
