"""exr-roots-and-rational-powers-r3 (05): (n + sqrt n)/(n^2 + 1) <= 2/n for n >= 1; N > 2/eps works."""
import math
from fractions import Fraction as F

QUOTED = {"C": 2}
for n in range(1, 5000):
    assert n <= n * n  # so sqrt n <= n
    assert F(2 * n, n * n + 1) <= F(QUOTED["C"], n)
for eps in [F(1), F(1, 10), F(3, 1000)]:
    N = math.floor(2 / eps) + 1
    assert N >= 1 and all(F(2, n) < eps for n in range(N, N + 300))
print("ok")
