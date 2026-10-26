"""exr-completeness-and-archimedes-b3:
(a) for a > 0 with a rational square root r, the elements b with b^2 = a among many rationals are exactly r and -r;
(d) the identity (x + 1/2)^2 - 1/4 = x^2 + x, and x = sqrt(a + 1/4) - 1/2 > 0 with x^2 + x = a (exact, on
    a = t^2 - 1/4 for rational t > 1/2, and numerically on random a);
(e) the sequence 1 - 1/n stays below 1 and comes within any sampled epsilon of 1."""
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import random

random.seed(63)
getcontext().prec = 60
# (a)
for _ in range(300):
    r = Fr(random.randint(1, 200), random.randint(1, 30))
    a = r * r
    assert r != -r
    roots = set()
    for k in range(-400, 401):
        for d in range(1, 31):
            b = Fr(k, d)
            if b * b == a:
                roots.add(b)
    if abs(r) <= 400 / 30:  # only then every candidate of the grid with denominator <= 30 is covered
        assert roots == {r, -r}
    else:
        assert roots <= {r, -r}
# (d) identity
for _ in range(5000):
    x = Fr(random.randint(-9999, 9999), random.randint(1, 999))
    assert (x + Fr(1, 2)) ** 2 - Fr(1, 4) == x * x + x
# (d) exact instances: a = t^2 - 1/4 with t > 1/2, so sqrt(a + 1/4) = t
for _ in range(5000):
    t = Fr(1, 2) + Fr(random.randint(1, 9999), random.randint(1, 999))
    a = t * t - Fr(1, 4)
    assert a > 0
    x = t - Fr(1, 2)
    assert x > 0 and x * x + x == a
# (d) numerically
for _ in range(2000):
    a = Decimal(random.randint(1, 10**6)) / Decimal(random.randint(1, 10**4))
    x = (a + Decimal("0.25")).sqrt() - Decimal("0.5")
    assert x > 0 and abs(x * x + x - a) < Decimal(10) ** -40
# (e)
for _ in range(2000):
    eps = Fr(1, random.randint(1, 10**6))
    n = int(1 / eps) + 1
    assert 1 - Fr(1, n) < 1 and 1 - (1 - Fr(1, n)) < eps
print("exr-completeness-and-archimedes-b3: OK")
