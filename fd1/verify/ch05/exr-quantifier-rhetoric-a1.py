"""exr-quantifier-rhetoric-a1 (Ch 5, Section 5.2): |a_n - L| < L/2 gives a_n > L/2 > 0."""
from fractions import Fraction as Fr

QUOTED = {"eps": "L/2"}
for L in [Fr(1), Fr(3, 7), Fr(10)]:
    for k in range(-99, 100):
        an = L + Fr(k, 100) * (L / 2)      # |a_n - L| < L/2
        if abs(an - L) < L / 2:
            assert L - an <= abs(an - L) and an > L / 2 > 0
print("exr-quantifier-rhetoric-a1: all quoted values check")
