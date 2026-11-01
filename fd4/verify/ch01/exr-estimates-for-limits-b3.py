"""exr-estimates-for-limits-b3, and the warning before the exercises (eps = 1, N = n = 1, 1/n^2 = 1)."""
from fractions import Fraction as F
import math

for n in range(1, 2000):                                       # (a)
    assert n * n + 1 <= 2 * n * n and F(n * n + 1, n ** 3) <= F(2, n)
for n in range(1, 2000):                                       # (b)
    assert F(n, n + 1) >= F(1, 2)
for N in range(0, 200):
    n = max(N, 1)
    assert n >= N and abs(F(n, n + 1)) >= F(1, 2)
for n in range(1, 500):                                        # (c)
    assert abs(F((-1) ** n, n)) == F(1, n)
eps, n = F(1), 1                                               # (d) and the warning
assert n >= 1 / eps and F(1, n * n) == 1 and not (F(1, n * n) < eps)
for n in range(3, 120):                                        # (e)
    tail = F(1)
    for k in range(3, n):
        assert 0 < F(2, k) <= 1
        tail *= F(2, k)
    assert 0 < tail <= 1
    val = F(2, 1) * F(2, 2) * tail * F(2, n)
    assert val == F(2 ** n, math.factorial(n)) and val <= F(4, n)
assert F(2 ** 3, math.factorial(3)) == F(4, 3)                  # equality at n = 3
for eps in [F(1), F(1, 10), F(1, 1000)]:
    N = max(3, math.floor(4 / eps) + 1)
    assert all(F(2 ** n, math.factorial(n)) < eps for n in range(N, N + 100))
print("ok")
