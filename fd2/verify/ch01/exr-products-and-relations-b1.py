"""exr-products-and-relations-b1: ([0,1]x[0,2]) u ([1,2]x[0,1]) = ([0,2]x[0,1]) u ([0,1]x[1,2]),
checked on a rational grid covering [-1, 3]^2 (Ch 6 Section 6.3)."""
from fractions import Fraction as F

QUOTED = {"P": "[0, 1]", "Q": "[1, 2]"}

g = [F(k, 8) for k in range(-8, 25)]
I = lambda v, a, b: a <= v <= b
for x in g:
    for y in g:
        E = (I(x, 0, 1) and I(y, 0, 2)) or (I(x, 1, 2) and I(y, 0, 1))
        R = (I(x, 0, 2) and I(y, 0, 1)) or (I(x, 0, 1) and I(y, 1, 2))
        assert E == R, (x, y)
        assert I(x, 0, 2) == (I(x, 0, 1) or I(x, 1, 2))
print("exr-products-and-relations-b1: all quoted values check")
