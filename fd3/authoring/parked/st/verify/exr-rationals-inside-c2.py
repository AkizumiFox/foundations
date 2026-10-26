"""exr-rationals-inside-c2 (Section 7.5), the cube-root cut tau = {p <= 0 or p^3 < 2}.
Setup: d = 2 - p^3, h = d/(3p^2 + 3p + 2) in (0, 1), (p + h)^3 < p^3 + h(3p^2 + 3p + 1) < 2.
Blank: t = 2/x - 1 in (0, 1], mu = 1 + t/7, mu^3 <= 1 + (169/343) t < 1 + t = 2/x, with
147 + 21 + 1 = 169 over 343; the remark: c = 1/3 fails at x = 1 (mu = 4/3, mu^3 = 64/27 > 2);
and the walk gives r with r^3 > x, u = x/r^2 < r."""
from fractions import Fraction as F
import random

QUOTED = {"num": 169, "den": 343, "parts": (147, 21, 1), "mu_bad": F(4, 3), "mu_bad_cubed": F(64, 27)}
assert sum(QUOTED["parts"]) == QUOTED["num"] and 7 ** 3 == QUOTED["den"]
assert F(3, 7) == F(147, 343) and F(3, 49) == F(21, 343) and F(1, 343) == F(1, 343)
assert QUOTED["mu_bad"] ** 3 == QUOTED["mu_bad_cubed"] and QUOTED["mu_bad_cubed"] > 2

# cubic identities, checked at many points (more than the degree in each variable)
for k in range(-40, 41):
    T = F(k, 9)
    assert (1 + T / 7) ** 3 == 1 + 3 * T / 7 + 3 * T ** 2 / 49 + T ** 3 / 343
    for j in range(-12, 13):
        P, H = F(k, 9), F(j, 5)
        # p^3 + h(3p^2 + 3p + 1) - (p + h)^3 = 3p h (1 - h) + h (1 - h^2)
        assert P ** 3 + H * (3 * P ** 2 + 3 * P + 1) - (P + H) ** 3 == 3 * P * H * (1 - H) + H * (1 - H ** 2)

def in_tau(p):
    return p <= 0 or p ** 3 < 2

random.seed(13)
for _ in range(3000):
    p = F(random.randint(1, 1259), 1000)             # 0 < p, p^3 < 2 (1.259^3 < 2)
    assert p ** 3 < 2
    d = 2 - p ** 3
    h = d / (3 * p * p + 3 * p + 2)
    assert 0 < d <= 2 and 0 < h < 1
    assert (p + h) ** 3 < p ** 3 + h * (3 * p * p + 3 * p + 1) < 2
for _ in range(300):
    x = 1 + F(random.randint(0, 9999), 10000)        # 1 <= x < 2
    t = 2 / x - 1
    mu = 1 + t / 7
    assert 0 < t <= 1 and mu > 1 and mu ** 3 <= 1 + F(169, 343) * t < 2 / x
    if x > F(19, 10):
        continue
    r = F(1, 2)
    while in_tau(mu * r):
        r = mu * r
    assert r > 0 and in_tau(r) and not in_tau(mu * r) and r ** 3 > x
    u = x / (r * r)
    assert 0 < u < r and in_tau(u) and r * r * u == x
print("ok")
