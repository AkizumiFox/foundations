"""exr-cauchy-sequences-c3: counterexample to the step in Q with b_n = 1/(n+1), a_n = n+1,
eps = 1: for n = N, m = 2N + 1, |b_n - b_m| = 1/(N+1) - 1/(2N+2) = 1/(2(N+1)) = eps/(2|a_n|)."""
from fractions import Fraction as F
QUOTED = {"eps": 1, "m": "2N + 1"}
eps = F(QUOTED["eps"])
b = lambda n: F(1, n + 1)
a = lambda n: n + 1
for N in range(2000):
    n, m = N, 2 * N + 1
    assert m >= N and n >= N
    d = abs(b(n) - b(m))
    assert d == F(1, N + 1) - F(1, 2 * N + 2) == F(1, 2 * (N + 1))
    assert d == eps / (2 * abs(a(n)))
    assert not (d < eps / (2 * abs(a(n))))
print("ok")
