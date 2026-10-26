"""exr-ordering-the-reals-b4: (b) b = (-1, 1, 1, ...) ~ (1)_n, b_0 = -1; (d) with a margin delta for a,
b_n >= a_n - 1/(n + 1) >= delta/2 beyond max{N, K}, K with 1/m < delta/2 for m >= K; (e) a = b = (1)_n."""
from fractions import Fraction as F
import math

QUOTED = {"b0": -1, "e_diff": 0}

b = lambda n: F(-1) if n == 0 else F(1)
assert b(0) == QUOTED["b0"] and all(b(n) == 1 for n in range(1, 100))

# (d): numeric check on several (a, delta, N) choices, b at the worst case b_n = a_n - 1/(n+1)
cases = [
    (lambda n: F(1), F(1), 0),
    (lambda n: 1 - F(2, n + 1), F(1, 2), 3),
    (lambda n: F(1, 10) + F(1, n + 1), F(1, 10), 0),
    (lambda n: F(3, 100) - F(1, (n + 1) ** 2) if n < 5 else F(3, 100), F(3, 100), 5),
]
for a, d, N in cases:
    assert all(a(n) >= d for n in range(N, N + 500))
    K = math.floor(2 / d) + 1          # 1/K < d/2
    assert F(1, K) < d / 2 and all(F(1, m) < d / 2 for m in range(K, K + 500))
    bw = lambda n: a(n) - F(1, n + 1)
    M = max(N, K)
    assert all(bw(n) >= d / 2 for n in range(M, M + 2000))

# (e)
assert F(1) - F(1) == QUOTED["e_diff"]
print("ok")
