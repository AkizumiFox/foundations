"""thm-cut-rationals-dense (Section 7.5), its Quick check: q = 29/20 has q > 0, q^2 = 841/400 > 800/400 = 2,
and 29/20 < 30/20 = 3/2; strictness of sigma < D_q: 10/7 > 0, (10/7)^2 = 100/49 > 98/49 = 2 and
10/7 < 29/20 (200/140 < 203/140). Also q = 10/7 works, with witness 17/12: (17/12)^2 = 289/144 > 2 and
17/12 < 10/7 (119/84 < 120/84). Sigma = {p <= 0 or p^2 < 2}."""
from fractions import Fraction as F

QUOTED = {"q": F(29, 20), "q_squared": F(841, 400), "two": F(800, 400), "bound": F(30, 20),
          "upper": F(3, 2), "other": F(10, 7), "other_sq": F(100, 49), "two_49": F(98, 49),
          "w_lo": F(200, 140), "w_hi": F(203, 140), "w2": F(17, 12), "w2_sq": F(289, 144),
          "w2_lo": F(119, 84), "w2_hi": F(120, 84)}


def in_sigma(p):
    return p <= 0 or p * p < 2


q = QUOTED["q"]
assert q > 0 and q * q == QUOTED["q_squared"] and QUOTED["two"] == 2 and q * q > 2
assert QUOTED["bound"] == QUOTED["upper"] and q < QUOTED["upper"]
o = QUOTED["other"]
assert o > 0 and o * o == QUOTED["other_sq"] and QUOTED["two_49"] == 2 and o * o > 2 and not in_sigma(o)
assert QUOTED["w_lo"] == o and QUOTED["w_hi"] == q and o < q          # 10/7 in D_{29/20} \ sigma
assert o < QUOTED["upper"]
w = QUOTED["w2"]
assert w > 0 and w * w == QUOTED["w2_sq"] and w * w > 2 and not in_sigma(w)
assert QUOTED["w2_lo"] == w and QUOTED["w2_hi"] == o and w < o       # 17/12 in D_{10/7} \ sigma
print("ok")
