"""exr-polynomial-gcd-a1 (c): the ideal of polynomials vanishing at 1 and -1."""
from fractions import Fraction
from _s0102_poly import P, ev

QUOTED = {"least degree": 2}
d = P(1, 0, -1)
assert ev(d, 1) == 0 and ev(d, -1) == 0 and len(d) - 1 == QUOTED["least degree"]
# a x + b vanishing at 1 and -1 forces a = b = 0 (solve the 2x2 system exactly)
# a + b = 0, -a + b = 0  =>  determinant 1*1 - 1*(-1) = 2 != 0
assert 1 * 1 - 1 * (-1) == 2
print("ok")
