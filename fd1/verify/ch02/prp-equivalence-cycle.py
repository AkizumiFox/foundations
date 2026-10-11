"""prp-equivalence-cycle (Ch 2, Section 2.4) and the two-arrow warning after it:
(a) x > 0, (b) 2x > 0, (c) x > 1; x = 1/2 satisfies (a), (b) but not (c)."""
from fractions import Fraction as F

QUOTED = {"witness": F(1, 2)}

pts = [F(k, 8) for k in range(-80, 81)]
assert all((x > 0) == (2 * x > 0) for x in pts)
x = QUOTED["witness"]
assert x > 0 and 2 * x > 0 and not x > 1
print("prp-equivalence-cycle: all quoted values check")
