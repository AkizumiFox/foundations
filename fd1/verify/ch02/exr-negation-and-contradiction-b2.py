"""exr-negation-and-contradiction-b2 (Ch 2, Section 2.2): x^2 - x + 1 = (x - 1/2)^2 + 3/4, and
(x - 1/2)^2 = x^2 - x + 1/4, 1/4 + 3/4 = 1. Both sides are polynomials of degree 2, so agreement at
three points proves the identity; we check many exact rationals. Also -3/4 < 0."""
from fractions import Fraction as F

QUOTED = {"shift": F(1, 2), "constant": F(3, 4)}
h, c = QUOTED["shift"], QUOTED["constant"]
for p in range(-200, 201):
    for qd in (1, 2, 3, 5):
        x = F(p, qd)
        assert x * x - x + 1 == (x - h) ** 2 + c
        assert (x - h) ** 2 == x * x - x + F(1, 4)
        assert x * x - x + 1 != 0
assert F(1, 4) + c == 1 and -c < 0
print("exr-negation-and-contradiction-b2: all quoted values check")
