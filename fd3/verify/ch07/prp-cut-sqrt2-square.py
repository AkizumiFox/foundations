"""prp-cut-sqrt2-square (Section 7.5): for 1 <= x < 2, t = 2/x - 1 in (0, 1], mu = 1 + t/3 > 1 and
mu^2 < 1 + t = 2/x (since t^2/9 < t/3 iff t < 3). The example x = 3/2: t = 1/3, mu = 10/9,
mu^2 = 100/81 < 108/81 = 4/3 = 2/x. Also the (subseteq) bound: r, s in (0, sqrt 2) give rs < 2,
and a simulation of the walk: for r with mu r outside sigma, r^2 > x and s = x/r < r."""
from fractions import Fraction as F
import random

QUOTED = {"x": F(3, 2), "t": F(1, 3), "mu": F(10, 9), "mu_sq": F(100, 81), "bound": F(108, 81),
          "two_over_x": F(4, 3)}
x = QUOTED["x"]
t = 2 / x - 1
mu = 1 + t / 3
assert t == QUOTED["t"] and mu == QUOTED["mu"] and mu * mu == QUOTED["mu_sq"]
assert QUOTED["bound"] == QUOTED["two_over_x"] == 2 / x and mu * mu < 2 / x

# (1 + t/3)^2 - (1 + t) = t^2/9 - t/3 = t(t - 3)/9, a quadratic identity: check it at many points
for k in range(-50, 51):
    T = F(k, 7)
    assert (1 + T / 3) ** 2 - (1 + T) == T * (T - 3) / 9

def in_sigma(p):
    return p <= 0 or p * p < 2

random.seed(11)
for i in range(3000):
    x = 1 + F(random.randint(0, 9999), 10000)        # 1 <= x < 2
    t = 2 / x - 1
    mu = 1 + t / 3
    assert 0 < t <= 1 and mu > 1 and mu * mu < 2 / x
    if i >= 200 or x > F(19, 10):
        continue
    # walk up by the factor mu from a = 1/2 (as lem-cut-multiplicative-step does) until leaving sigma
    r = F(1, 2)
    while in_sigma(mu * r):
        r = mu * r
    assert in_sigma(r) and r > 0 and not in_sigma(mu * r)
    assert r * r > x
    s = x / r
    assert 0 < s < r and in_sigma(s) and r * s == x
for _ in range(3000):
    r = F(random.randint(1, 1414), 1000)
    s = F(random.randint(1, 1414), 1000)
    assert r * r < 2 and s * s < 2 and r * s < 2
print("ok")
