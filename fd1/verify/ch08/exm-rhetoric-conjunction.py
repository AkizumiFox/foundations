"""exm-rhetoric-conjunction (Ch 8, Section 8.1): for 0 < x < 1, x^2 < x and x^2 > 0,
checked exactly on rationals and on a grid."""
from fractions import Fraction as Fr

QUOTED = {"hyp": "0 < x < 1", "c1": "x^2 < x", "c2": "x^2 > 0"}

pts = [Fr(p, q) for q in range(2, 80) for p in range(1, q)]
pts += [Fr(k, 10**4) for k in range(1, 10**4)]
for x in pts:
    assert 0 < x < 1
    assert x * x < x          # multiply x < 1 by x > 0
    assert x * x > 0
    assert x * x == x * x and x * 1 == x
print("exm-rhetoric-conjunction: all quoted values check")
