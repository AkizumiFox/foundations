"""exr-quantifier-rhetoric-c2 (Ch 5, Section 5.2): forall x > 0 exists n (1/n < x) true (n > 1/x);
exists n forall x > 0 (1/n < x) false (x = 1/n)."""
from fractions import Fraction as Fr
import math

QUOTED = {"refuting_x": "1/n"}
for x in [Fr(1, 1000), Fr(1, 3), Fr(2), Fr(7, 5)]:
    n = math.floor(1 / x) + 1
    assert n >= 1 and Fr(1, n) < x
for n in range(1, 200):
    x = Fr(1, n)
    assert x > 0 and not (Fr(1, n) < x)
print("exr-quantifier-rhetoric-c2: all quoted values check")
