"""exm-first-estimate: (n + 3)/(2n^2 - 1) -> 0, with n0 = 3, C = 2, N = max{3, N'}, N' > 2/eps."""
from fractions import Fraction as F
import math

QUOTED = {"n0": 3, "C": 2}
a = lambda n: F(n + 3, 2 * n * n - 1)
for n in range(1, 3000):
    assert 2 * n * n - 1 >= 1 and a(n) > 0          # step (1)
    assert 2 * n * n - 1 >= n * n                     # holds from n = 1 on
for n in range(QUOTED["n0"], 3000):
    assert n + 3 <= 2 * n
    assert a(n) <= F(QUOTED["C"], n)
assert not (2 + 3 <= 2 * 2)                           # n + 3 <= 2n fails at n = 2
for eps in [F(1), F(1, 2), F(1, 7), F(3, 100), F(1, 1000)]:
    Np = math.floor(QUOTED["C"] / eps) + 1            # an integer > C/eps
    N = max(QUOTED["n0"], Np)
    assert all(abs(a(n)) < eps for n in range(N, N + 2000))
print("ok")
