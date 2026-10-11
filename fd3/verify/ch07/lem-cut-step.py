"""lem-cut-step: walk through sigma from a = 1 by 1/10 gives k_0 = 5, n = 4, pair 7/5, 3/2
(196 < 200, 225 > 200); Quick check: from 7/5 by 1/100 gives k_0 = 2, n = 1, pair 141/100, 71/50
(141^2 = 19881 < 20000, 142^2 = 20164 > 20000)."""
from fractions import Fraction as F

QUOTED = {"walk1": (5, 4, F(7, 5), F(3, 2)), "walk2": (2, 1, F(141, 100), F(71, 50)),
          "squares": (196, 225, 19881, 20164)}


def in_sigma(p):
    return p <= 0 or p * p < 2


def walk(a, eps):
    k = 0
    while in_sigma(a + k * eps):
        k += 1
    return k, k - 1, a + (k - 1) * eps, a + k * eps


assert walk(F(1), F(1, 10)) == QUOTED["walk1"]
assert walk(F(7, 5), F(1, 100)) == QUOTED["walk2"]
assert (14 ** 2, 15 ** 2, 141 ** 2, 142 ** 2) == QUOTED["squares"]
assert 196 < 200 < 225 and 19881 < 20000 < 20164
assert F(142, 100) == F(71, 50)
print("ok")
