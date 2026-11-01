"""prp-linear-over-power-null: n/r^n <= 4/(n h^2) for n >= 2, h = r - 1; C(n,2)*2 = n(n-1); n(n-1) >= n^2/2;
and the remark that k = 1 gives only n/r^n < 1/h. Also exm-binomial-bound's n/2^n <= 2/(n-1), recalled."""
from fractions import Fraction as F
from math import comb
import math

QUOTED = {"C_numerator": 4, "n0": 2}
for n in range(2, 300):
    assert comb(n, 2) * 2 == n * (n - 1)
    assert n * (n - 1) >= F(n * n, 2)
    assert F(n, 2 ** n) <= F(2, n - 1)
for r in [F(11, 10), F(3, 2), F(2), F(7)]:
    h = r - 1
    for n in range(QUOTED["n0"], 300):
        assert r ** n >= F(n * (n - 1), 2) * h ** 2 >= F(n * n, 4) * h ** 2 > 0
        assert F(n) / r ** n <= F(QUOTED["C_numerator"]) / (n * h * h)
        assert F(n) / r ** n < 1 / h                   # the k = 1 bound
    C = F(QUOTED["C_numerator"]) / (h * h)
    for eps in [F(1), F(1, 10), F(1, 100)]:
        N = max(QUOTED["n0"], math.floor(C / eps) + 1)
        assert all(F(n) / r ** n < eps for n in range(N, N + 200))
print("ok")
