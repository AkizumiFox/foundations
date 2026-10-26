"""def-cut-negative (Section 7.3): the examples -D_0 = D_0, -D_1 = D_{-1}, the Quick check
-D_3 = D_{-3} and D_{1/2} + D_{1/3} = D_{5/6} (split x = (1/2 - d) + (1/3 - d), d = (5/6 - x)/2),
and the before-reading-on answer D_1 + D_{-1} = D_0 (s = (1 - d) + (-1 - d), d = -s/2)."""
from fractions import Fraction as Fr
import random

QUOTED = {"neg_D3": -3, "sum_half_third": "5/6"}


def in_neg_rational_cut(p, q):
    # p in -D_q iff exists r > 0 with -p - r >= q; the best margin candidate is r = -q - p
    r = -q - p
    return r > 0 and (-p - r) >= q


random.seed(7)
for q in [Fr(0), Fr(1), Fr(3), Fr(-2), Fr(5, 7)]:
    for _ in range(3000):
        p = Fr(random.randint(-4000, 4000), random.randint(1, 300))
        # margins tried: a range of small and large r; membership must match p < -q
        found = any((-p - r) >= q for r in [Fr(1, k) for k in range(1, 50)] + [Fr(k) for k in range(1, 50)] + ([(-q - p)] if -q - p > 0 else []))
        assert found == (p < -q), (q, p)
        assert in_neg_rational_cut(p, q) == (p < -q)
assert QUOTED["neg_D3"] == -3

for _ in range(2000):
    xv = Fr(random.randint(-10**4, 10**4), random.randint(1, 999))
    d = (Fr(5, 6) - xv) / 2
    assert (Fr(1, 2) - d) + (Fr(1, 3) - d) == xv
    d2 = -xv / 2
    assert (1 - d2) + (-1 - d2) == xv
    if xv < 0:
        assert 1 - d2 < 1 and -1 - d2 < -1
assert Fr(1, 2) + Fr(1, 3) == Fr(QUOTED["sum_half_third"])
for _ in range(2000):
    xv = Fr(random.randint(-5000, 832), 1000)
    if xv < Fr(5, 6):
        dv = (Fr(5, 6) - xv) / 2
        assert dv > 0 and Fr(1, 2) - dv < Fr(1, 2) and Fr(1, 3) - dv < Fr(1, 3)
print("ok")
