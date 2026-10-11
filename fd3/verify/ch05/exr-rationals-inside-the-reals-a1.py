"""exr-rationals-inside-the-reals-a1 (b): d_1 = 7/5, d_2 = 141/100, d_2 + 1/100 = 71/50;
7/5 <= d_j < 71/50 for j >= 2; integer parts: r -> 1, 10r -> 14 (14 <= 10r <= 71/5 < 15)."""
from fractions import Fraction as F
from math import isqrt, floor
QUOTED = {"d1": F(7, 5), "d2": F(141, 100), "upper": F(71, 50), "ip_r": 1, "ip_10r": 14, "upper10": F(71, 5)}
def d(k):
    m = isqrt(2 * 10 ** (2 * k))
    return F(m, 10 ** k)
assert d(1) == QUOTED["d1"] and d(2) == QUOTED["d2"]
assert d(2) + F(1, 100) == QUOTED["upper"] == F(142, 100)
assert all(QUOTED["d1"] <= d(j) < QUOTED["upper"] for j in range(2, 30))
assert 1 <= QUOTED["d1"] and QUOTED["upper"] < 2
assert floor(QUOTED["d1"]) == floor(QUOTED["upper"]) == QUOTED["ip_r"]
assert 10 * QUOTED["d1"] == 14 and 10 * QUOTED["upper"] == QUOTED["upper10"] < 15
assert floor(10 * QUOTED["d1"]) == floor(QUOTED["upper10"]) == QUOTED["ip_10r"]
# cross-check with the Newton sequence (same class): late terms in the same bracket
x = F(2)
for _ in range(6):
    x = x / 2 + 1 / x
assert QUOTED["d1"] <= x <= QUOTED["upper"]
print("ok")
