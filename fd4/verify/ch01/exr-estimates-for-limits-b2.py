"""exr-estimates-for-limits-b2: |(2n+1)/(n+1) - 2| = 1/(n+1); line (ii) with N > 1/eps, N >= 1."""
from fractions import Fraction as F
import math

for n in range(0, 2000):
    assert abs(F(2 * n + 1, n + 1) - 2) == F(1, n + 1)
for eps in [F(2), F(1), F(1, 7), F(1, 1000)]:
    N = max(1, math.floor(1 / eps) + 1)
    assert N > 1 / eps and F(1, N) < eps
    for n in range(N, N + 300):
        assert F(1, n + 1) < F(1, n) <= F(1, N) < eps
print("ok")
