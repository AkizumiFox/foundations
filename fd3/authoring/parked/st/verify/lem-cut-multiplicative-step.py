"""lem-cut-multiplicative-step (Section 7.4): mu r - (r + eps) = (mu - 1)(r - a) for eps = (mu - 1) a,
and the construction run on rational cuts and on sigma: r in alpha, r > 0, mu r not in alpha."""
from fractions import Fraction as Fr
import random

QUOTED = {}
random.seed(8)
for _ in range(3000):
    mu = 1 + Fr(random.randint(1, 10**4), random.randint(1, 10**4))
    a = Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    r = Fr(random.randint(-10**4, 10**4), random.randint(1, 10**3))
    eps = (mu - 1) * a
    assert mu * r - (r + eps) == (mu - 1) * (r - a)


def sigma(x):
    return x <= 0 or x * x < 2


cuts = [(lambda x, c=c: x < c, Fr(c) / 2) for c in [Fr(1), Fr(7, 3), Fr(100)]] + [(sigma, Fr(1))]
for member, a in cuts:
    for k in range(1, 200):
        mu = 1 + Fr(1, k)
        eps = (mu - 1) * a
        n = 0
        while member(a + (n + 1) * eps):
            n += 1
        r = a + n * eps
        assert member(r) and r > 0 and not member(mu * r)
print("ok")
