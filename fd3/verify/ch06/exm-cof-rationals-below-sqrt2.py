"""exm-cof-rationals-below-sqrt2: Q_R(sqrt 2) = {q < 0} u {q >= 0 : q^2 < 2}, checked against the
real number sqrt 2 on many rationals; and the warning in Section 6.2: -2 is in Q_R(sqrt 2) but not in
A = {x : x^2 < 2}, and the elements of Q_R(sqrt 2) outside A are negative (below 0, which is in A)."""
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import random

QUOTED = {"omitted": -2, "omitted_square": 4}
getcontext().prec = 60
r = Decimal(2).sqrt()
random.seed(2)
for _ in range(5000):
    q = Fr(random.randint(-5000, 5000), random.randint(1, 1000))
    below = Decimal(q.numerator) / Decimal(q.denominator) < r
    described = (q < 0) or (q >= 0 and q * q < 2)
    assert bool(below) == described
    inA = q * q < 2
    if described and not inA:
        assert q < 0
q = Fr(QUOTED["omitted"])
assert q * q == QUOTED["omitted_square"] and q < 0 and not q * q < 2
assert 0 * 0 < 2
print("ok")
