"""exr-connective-rhetoric-c2 (Ch 5, Section 5.1): eps = x^2 gives x^2 < x^2 when x != 0."""
from fractions import Fraction as Fr

QUOTED = {"eps": "x^2"}
for k in range(-20, 21):
    x = Fr(k, 3)
    if x != 0:
        e = x * x
        assert e > 0 and not (x * x < e)
    else:
        assert x * x == 0
print("exr-connective-rhetoric-c2: all quoted values check")
