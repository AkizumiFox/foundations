"""exm-method-power-lower-bound and the fold "When the one-term bound fails":
(1 + h)^n >= C(n, k) h^k for h >= 0; fails at h = -1, n = 2, k = 2 (0 >= 1); Bernoulli holds for -1 <= h < 0."""
from fractions import Fraction as F
from math import comb

QUOTED = {"fold_lhs": 0, "fold_rhs": 1}
for h in [F(0), F(1, 10), F(1), F(3, 2), F(5)]:
    for n in range(0, 40):
        for k in range(0, n + 1):
            assert (1 + h) ** n >= comb(n, k) * h ** k
h, n = F(-1), 2
assert (1 + h) ** n == QUOTED["fold_lhs"] and comb(2, 2) * h ** 2 == QUOTED["fold_rhs"]
assert not ((1 + h) ** n >= comb(2, 2) * h ** 2)
for h in [F(-1), F(-1, 2), F(-1, 10)]:
    for n in range(0, 60):
        assert (1 + h) ** n >= 1 + n * h
print("ok")
