"""exr-ordered-field-of-rationals-b1: -3/5 < -7/12 < -4/7, with the six integer products."""
from fractions import Fraction as F
QUOTED = {"products": (-36, -35, -49, -48, -21, -20)}
a, b, c = F(-7, 12), F(-3, 5), F(-4, 7)
assert ((-3) * 12, (-7) * 5, (-7) * 7, (-4) * 12, (-3) * 7, (-4) * 5) == QUOTED["products"]
assert -36 < -35 and -49 < -48 and -21 < -20
assert b < a < c
print("ok")
