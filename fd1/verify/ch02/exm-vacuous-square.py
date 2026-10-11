"""exm-vacuous-square (Ch 2, Section 2.1): the premise not(x^2 < 0) holds for every real x (checked on
exact rationals), so the implication "x^2 < 0 -> x = 7" is vacuously true; the 7 is arbitrary and
is never computed with."""
from fractions import Fraction as F

QUOTED = {"x = 7": 7}
for p in range(-300, 301):
    for q in (1, 2, 3, 9):
        x = F(p, q)
        assert not (x * x < 0)
        # the implication is true at x: hypothesis false (or conclusion true)
        assert (not (x * x < 0)) or x == QUOTED["x = 7"]
print("exm-vacuous-square: all quoted values check")
