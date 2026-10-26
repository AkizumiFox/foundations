"""exr-rationals-inside-b2 (Section 7.5): rho = {p <= 0 or p^2 < 3}. For 1 <= x < 3, t = 3/x - 1 in (0, 2],
mu = 1 + t/3 > 1, mu^2 < 1 + t = 3/x because t < 3; and the walk produces r with r^2 > x, s = x/r < r."""
from fractions import Fraction as F
import random

QUOTED = {"t_max": 2, "three": 3, "nine": 9}
assert 3 / F(1) - 1 == QUOTED["t_max"] and QUOTED["three"] ** 2 == QUOTED["nine"]

def in_rho(p):
    return p <= 0 or p * p < 3

random.seed(5)
for _ in range(300):
    x = 1 + F(random.randint(0, 19999), 10000)       # 1 <= x < 3
    t = 3 / x - 1
    mu = 1 + t / 3
    assert 0 < t <= 2 and mu > 1 and mu * mu < 3 / x
    if x > F(29, 10):
        continue
    r = F(1, 2)
    while in_rho(mu * r):
        r = mu * r
    assert r > 0 and in_rho(r) and not in_rho(mu * r) and r * r > x
    s = x / r
    assert 0 < s < r and in_rho(s) and r * s == x
print("ok")
