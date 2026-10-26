"""thm-constructed-rationals-dense: the direct density proof now lives in the solution of
exr-rationals-inside-the-reals-c3 (a) (Section 5.4); this script checks the values quoted there. With q = (a_N + b_N)/2,
q - a_n = (a_N - a_n) + (b_N - a_N)/2 and b_n - q = (b_n - b_N) + (b_N - a_N)/2;
-delta/4 + delta/2 = delta/4. Checked as identities on random rationals, and the bound on samples."""
from fractions import Fraction as F
import random
QUOTED = {"margin": F(1, 4)}  # margin delta/4, as a multiple of delta
random.seed(1)
rq = lambda: F(random.randint(-10**6, 10**6), random.randint(1, 10**4))
for _ in range(2000):
    aN, bN, an, bn = rq(), rq(), rq(), rq()
    q = (aN + bN) / 2
    assert q - an == (aN - an) + (bN - aN) / 2
    assert bn - q == (bn - bN) + (bN - aN) / 2
    delta = abs(rq()) + F(1, 7)
    assert -delta / 4 + delta / 2 == QUOTED["margin"] * delta
    # if |aN - an| < delta/4, |bN - bn| < delta/4, bN - aN >= delta, then both gaps > delta/4
    aN2 = rq(); bN2 = aN2 + delta + abs(rq()) / 1000
    an2 = aN2 + (random.random() - 0.5) * F(1, 2) * delta / 2
    bn2 = bN2 + (random.random() - 0.5) * F(1, 2) * delta / 2
    an2, bn2 = F(an2), F(bn2)
    assert abs(aN2 - an2) < delta / 4 and abs(bN2 - bn2) < delta / 4
    q2 = (aN2 + bN2) / 2
    assert q2 - an2 > delta / 4 and bn2 - q2 > delta / 4
print("ok")
