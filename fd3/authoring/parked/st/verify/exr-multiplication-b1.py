"""exr-multiplication-b1: D_2 D_3 = D_6; for 0 < x < 6, lambda = (1 + x/6)/2, r = 2 lambda, s = x/(2 lambda)."""
from fractions import Fraction as Fr
import random

QUOTED = {"product": 6}
random.seed(10)
for _ in range(5000):
    x = Fr(random.randint(1, 5999), 1000) * Fr(random.randint(1, 1000), 1000)
    if 0 < x < 6:
        lam = (1 + x / 6) / 2
        r, s = 2 * lam, x / (2 * lam)
        assert x / 6 < lam < 1 and 0 < r < 2 and 0 < s < 3 and r * s == x
    r = Fr(random.randint(1, 1999), 1000)
    s = Fr(random.randint(1, 2999), 1000)
    assert r * s < QUOTED["product"]
assert 2 * 3 == QUOTED["product"]
print("ok")
