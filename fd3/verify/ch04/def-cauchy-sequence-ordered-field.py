"""def-cauchy-sequence-ordered-field: for a_n = 1/(n+1) in Q and eps = 1/100, N = 101 works
(1/N < eps and |a_m - a_n| < 1/N for m, n >= N); the non-example 1,0,1,0,... fails at eps = 1."""
from fractions import Fraction as F
QUOTED = {"eps": F(1, 100), "N": 101}
eps, N = QUOTED["eps"], QUOTED["N"]
assert F(1, N) < eps
a = lambda n: F(1, n + 1)
for m in range(N, N + 300):
    for n in range(N, N + 300, 7):
        assert abs(a(m) - a(n)) < F(1, N) < eps
# the bound of the argument is uniform: sup over m, n >= N of |a_m - a_n| is 1/(N+1) < 1/N
assert F(1, N + 1) < F(1, N)
b = lambda n: 1 if n % 2 == 0 else 0
for N0 in range(50):
    assert abs(b(N0) - b(N0 + 1)) == 1   # not < 1
print("ok")
