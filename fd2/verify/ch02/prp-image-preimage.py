"""The example after the two-readings remark (Ch 6, Section 6.6): a(x) = 3x - 2, B = [1,4]."""
from fractions import Fraction as F
QUOTED = {"preimage": [1, 2], "B": [1, 4]}
a = lambda x: 3 * x - 2
b = lambda y: (y + 2) / 3
assert b(F(1)) == 1 and b(F(4)) == 2 and a(F(1)) == 1 and a(F(2)) == 4
xs = [F(k, 50) for k in range(-200, 300)]
assert all((1 <= a(x) <= 4) == (1 <= x <= 2) for x in xs)
print("prp-image-preimage: all quoted values check")
