"""exm-dominant-term: (2n^2 + 3n)/(n^2 - 5) -> 2; distance (3n + 10)/(n^2 - 5); bound 12/n for n >= 4.
Also the Quick check after it: n^2 - 7n >= n^2/2 iff n = 0 or n >= 14."""
from fractions import Fraction as F
import math

QUOTED = {"n0": 4, "C": 12, "qc_threshold": 14}
assert all(n * n != 5 for n in range(0, 10))
a = lambda n: F(2 * n * n + 3 * n, n * n - 5)
for n in range(3, 3000):
    assert n * n > 5
    d = a(n) - 2
    assert d == F(3 * n + 10, n * n - 5) and d > 0
for n in range(QUOTED["n0"], 3000):
    assert 3 * n + 10 <= 6 * n and n * n - 5 >= F(n * n, 2)
    assert abs(a(n) - 2) <= F(QUOTED["C"], n)
assert not (3 * 3 + 10 <= 6 * 3)                      # 3n + 10 <= 6n fails at n = 3
for eps in [F(1), F(1, 3), F(1, 50), F(7, 1000)]:
    N = max(QUOTED["n0"], math.floor(QUOTED["C"] / eps) + 1)
    assert all(abs(a(n) - 2) < eps for n in range(N, N + 2000))
# Quick check
for n in range(0, 5000):
    holds = n * n - 7 * n >= F(n * n, 2)
    assert holds == (n == 0 or n >= QUOTED["qc_threshold"]), n
assert 0 * 0 - 7 * 0 == F(0)                          # equality at n = 0
print("ok")
