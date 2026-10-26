"""exr-rationals-as-classes-a1 (Section 10.4): the inverse of [(-3, 5)] is [(-5, 3)];
j(2)^{-1} = [(1, 2)]."""
from fractions import Fraction
QUOTED = {"inverse": (-5, 3), "product": (15, 15), "j2inv": (1, 2)}
a, b = QUOTED["inverse"]
assert b > 0 and (-3 * a, 5 * b) == QUOTED["product"]
assert Fraction(-3, 5) * Fraction(a, b) == 1
c, d = QUOTED["j2inv"]
assert (2 * c, 1 * d) == (2, 2) and Fraction(2, 1) * Fraction(c, d) == 1
print("exr-rationals-as-classes-a1: all quoted values check")
