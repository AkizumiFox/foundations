"""exm-rhetoric-implication (Ch 5, Section 5.1): |x - 1| < 1 implies x > 0; x <= 0 implies |x - 1| >= 1."""
from fractions import Fraction as Fr

QUOTED = {"|x-1|<1 -> x>0": True, "x<=0 -> |x-1|>=1": True}

xs = [Fr(k, 7) for k in range(-70, 71)]
for x in xs:
    if abs(x - 1) < 1:
        assert -1 < x - 1 < 1 and x > 0
    if x <= 0:
        assert abs(x - 1) >= 1
print("exm-rhetoric-implication: all quoted values check")
