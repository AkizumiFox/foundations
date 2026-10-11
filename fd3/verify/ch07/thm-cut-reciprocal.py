"""thm-cut-reciprocal and def-cut-reciprocal (Section 7.4), exr-multiplication-b2: D_2^{-1} = D_{1/2};
for 0 < p < 1, mu = (1 + 1/p)/2 has 1 < mu < 1/p and p mu < 1; for p > 0, q > 0, pq < 1 the midpoint
(p + 1/q)/2 lies strictly between p and 1/q; 1/(2q) * q = 1/2; and the whole construction on cuts."""
from fractions import Fraction as Fr
import random

QUOTED = {"D2_inverse": "1/2", "half": "1/2"}
random.seed(9)
for _ in range(5000):
    p = Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    # D_2^{-1}: p > 0 in it iff some q >= 2 has pq < 1 iff 2p < 1
    assert (2 * p < 1) == (p < Fr(QUOTED["D2_inverse"]))
    q = Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    assert (1 / (2 * q)) * q == Fr(QUOTED["half"])
    if p * q < 1:
        m = (p + 1 / q) / 2
        assert p < m < 1 / q and m * q < 1
    if p < 1:
        mu = (1 + 1 / p) / 2
        assert 1 < mu < 1 / p and p * mu < 1


def sigma(x):
    return x <= 0 or x * x < 2


for member in [lambda x: x < 2, lambda x: x < Fr(5, 3), sigma]:
    for k in range(2, 300):
        p = Fr(k - 1, k)
        mu = (1 + 1 / p) / 2
        a = Fr(1, 2)
        eps = (mu - 1) * a
        n = 0
        while member(a + (n + 1) * eps):
            n += 1
        r = a + n * eps
        assert member(r) and not member(mu * r)
        s = p / r
        assert s > 0 and s * (mu * r) < 1 and r * s == p
print("ok")
