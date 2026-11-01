"""prp-root-estimates (05): (a) a^(1/n) <= 1 + (a-1)/n, i.e. (1 + (a-1)/n)^n >= a; (b) (1 + w)^n >= n with w = sqrt(2/(n-1)),
checked through the binomial bound n(n-1)/2 * w^2 = n. Quick check: 1 + 4/n < 1.01 iff n > 400 (N = 401);
the least n with 5^(1/n) < 1.01 is 162, i.e. 1.01^162 > 5 >= 1.01^161."""
from fractions import Fraction as F
from math import comb

QUOTED = {"N_qc": 401, "least": 162}
for a in [F(1), F(3, 2), F(2), F(5), F(17), F(100)]:
    for n in range(1, 300):
        assert (1 + (a - 1) / n) ** n >= a
for n in range(2, 400):
    w2 = F(2, n - 1)
    assert comb(n, 2) * w2 == n          # so (1 + w)^n >= binom(n,2) w^2 = n
assert all((1 + F(4, n) < F(101, 100)) == (n > 400) for n in range(1, 2000))
q = F(101, 100)
assert q ** QUOTED["least"] > 5 >= q ** (QUOTED["least"] - 1)
print("ok")
