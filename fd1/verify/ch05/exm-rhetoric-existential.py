"""exm-rhetoric-existential (Ch 5, Section 5.2): 1/n -> 0; N an integer > 1/eps is positive,
1/N < eps, and n >= N gives 0 < 1/n <= 1/N; for eps = 0.03, 1/eps = 33.3..., N = 34 works."""
from fractions import Fraction as Fr
import math

QUOTED = {"eps": Fr(3, 100), "one_over_eps (33.3...)": 33.3, "N": 34}

e = QUOTED["eps"]
assert math.floor(1 / e) == 33 and abs(float(1 / e) - QUOTED["one_over_eps (33.3...)"]) < 0.04 and 1 / e != 33
N = QUOTED["N"]
assert N > 1 / e and Fr(1, N) < e
assert Fr(1, 33) > e      # 33 is too small: N must exceed 1/eps
for eps in [Fr(1), Fr(1, 2), Fr(3, 100), Fr(1, 997), Fr(5), Fr(7, 3)]:
    Nv = math.floor(1 / eps) + 1   # one integer beyond 1/eps
    assert Nv > 1 / eps > 0 and Nv >= 1 and Fr(1, Nv) < eps
    for n in range(Nv, Nv + 300):
        assert 0 < Fr(1, n) <= Fr(1, Nv) < eps
print("exm-rhetoric-existential: all quoted values check")
