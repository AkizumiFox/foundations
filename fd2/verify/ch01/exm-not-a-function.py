"""exm-not-a-function (Ch 6 Section 6.4): the circle at x = 0 and x = 2; 1/2 = 2/4."""
from fractions import Fraction as F

QUOTED = {"y^2 at x = 2": -3, "numerators of 1/2": (1, 2)}

assert 0 ** 2 + 1 ** 2 == 1 and 0 ** 2 + (-1) ** 2 == 1
assert 1 - 2 ** 2 == QUOTED["y^2 at x = 2"]
assert F(1, 2) == F(2, 4)
print("exm-not-a-function: all quoted values check")
