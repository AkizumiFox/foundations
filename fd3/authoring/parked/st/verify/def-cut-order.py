"""def-cut-order, Quick check: D_1 < sigma < D_{3/2}: (3/2)^2 = 9/4 > 2; 29/20 < 3/2 (58 < 60);
(29/20)^2 = 841/400 > 2 (841 > 800)."""
from fractions import Fraction as F

QUOTED = {"nine_quarters": F(9, 4), "cross": (58, 60), "sq": F(841, 400)}
assert F(3, 2) ** 2 == QUOTED["nine_quarters"] > 2
assert (29 * 2, 3 * 20) == QUOTED["cross"] and 58 < 60 and F(29, 20) < F(3, 2)
assert F(29, 20) ** 2 == QUOTED["sq"] > 2 and 841 > 800
assert 1 * 1 < 2
print("ok")
