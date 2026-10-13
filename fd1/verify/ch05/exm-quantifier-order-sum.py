"""exm-quantifier-order-sum (Ch 4, Section 4.1): forall x exists y (x+y=0) true, the swap false."""
from fractions import Fraction as Fr

QUOTED = {"(ii) defeating x = 1 - y gives x + y": 1}

R = sorted({Fr(p, q) for p in range(-40, 41) for q in range(1, 9)})
assert all(x + (-x) == 0 for x in R)            # witness y = -x
assert all((1 - y) + y == 1 != 0 for y in R)     # challenger's answer to any y
print("exm-quantifier-order-sum: all quoted values check")
