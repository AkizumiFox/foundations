"""The readings of exm-first-boxes (c) and prp-curry (Section 1.5)."""
from fractions import Fraction

pts = [Fraction(k, 7) for k in range(-70, 71)]
# (c): if a > 0 and x > 1 then ax > a
assert all(a * x > a for a in pts for x in pts if a > 0 and x > 1)
# prp-curry: if x > 0 and y > 0 then xy > 0
assert all(x * y > 0 for x in pts for y in pts if x > 0 and y > 0)
print("exm-first-boxes: checks")
