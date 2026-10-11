"""thm-cut-rationals-dense (Section 7.5), its Quick check: q = 29/20 has q > 0, q^2 = 841/400 > 800/400 = 2,
and 29/20 < 30/20 = 3/2; so sigma < D_q < D_{3/2}. Also 10/7 works. Sigma = {p <= 0 or p^2 < 2}."""
from fractions import Fraction as F

QUOTED = {"q": F(29, 20), "q_squared": F(841, 400), "two": F(800, 400), "bound": F(30, 20),
          "upper": F(3, 2), "other": F(10, 7)}
q = QUOTED["q"]
assert q > 0 and q * q == QUOTED["q_squared"] and QUOTED["two"] == 2 and q * q > 2
assert QUOTED["bound"] == QUOTED["upper"] and q < QUOTED["upper"]
o = QUOTED["other"]
assert o > 0 and o * o > 2 and o < QUOTED["upper"]
print("ok")
