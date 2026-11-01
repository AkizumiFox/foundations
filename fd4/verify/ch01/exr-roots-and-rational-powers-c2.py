"""exr-roots-and-rational-powers-c2 (05): binom(n,k)/n^k <= 1/k! <= 1/2^(k-1); (1 + 1/n)^n <= 3 - 2/2^n < 3."""
from fractions import Fraction as F
from math import comb, factorial, prod

QUOTED = {}
for n in range(1, 80):
    for k in range(1, n + 1):
        t = F(comb(n, k), n ** k)
        assert t == F(1, factorial(k)) * prod((F(n - j, n) for j in range(k)), start=F(1))
        assert t <= F(1, factorial(k)) <= F(1, 2 ** (k - 1))
    assert sum(F(1, 2 ** (k - 1)) for k in range(1, n + 1)) == 2 * (1 - F(1, 2 ** n))
    assert (1 + F(1, n)) ** n <= 3 - F(2, 2 ** n) < 3
print("ok")
