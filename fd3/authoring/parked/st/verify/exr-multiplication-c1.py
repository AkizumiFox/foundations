"""exr-multiplication-c1: rho(D_a) = {p <= 1/a} (a > 0), with largest element 1/a; and for sigma
(outside has no least element) a smaller outside point q' makes pq' < 1 strict."""
from fractions import Fraction as Fr
import random

QUOTED = {}
random.seed(12)
for _ in range(3000):
    a = Fr(random.randint(1, 10**3), random.randint(1, 10**2))
    p = Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    # some q >= a with pq <= 1 iff pa <= 1
    assert (p * a <= 1) == (p <= 1 / a)
    assert (1 / a) * a == 1
# sigma: for q outside (q > 0, q^2 > 2), q' = (q^2 + 2)/(2q) is a smaller outside point
for _ in range(3000):
    q = Fr(random.randint(1, 10**5), random.randint(1, 10**4))
    if q * q > 2:
        qq = (q * q + 2) / (2 * q)
        assert 0 < qq < q and qq * qq > 2
        p = 1 / q
        assert p * q <= 1 and p * qq < 1
print("ok")
