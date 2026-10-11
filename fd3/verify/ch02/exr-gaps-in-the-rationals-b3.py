"""exr-gaps-in-the-rationals-b3: x_4 = 665857/470832, e_4 = 1/221682772224, and the check against (ii)."""
from fractions import Fraction as F
QUOTED = {"x4": F(665857, 470832), "e4": F(1, 221682772224), "num": (332929, 332928, 470832),
          "sq": (443365544449, 221682772224)}
x3 = F(577, 408)
x4 = (x3*x3 + 2) / (2*x3)
assert x4 == QUOTED["x4"] and x4.numerator == 665857 and x4.denominator == 470832
assert (577**2, 2*408**2, 2*577*408) == QUOTED["num"] and 332929 + 332928 == 665857
assert (665857**2, 470832**2) == QUOTED["sq"] and 443365544449 - 2*221682772224 == 1
assert x4*x4 - 2 == QUOTED["e4"]
assert 4*166464*332929 == 221682772224
assert F(1, 166464)**2 / (4*x3*x3) == QUOTED["e4"] and x4 < x3
print("ok")
