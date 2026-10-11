"""exm-product-of-intervals: ([0,2] x [0,1]) n ([1,3] x [0,2]) = [1,2] x [0,1] (Ch 6 Section 6.3).
Checked on a fine rational grid covering [-1, 4]^2, endpoints included."""
from fractions import Fraction as F

QUOTED = {"answer": "[1, 2] \\times [0, 1]"}

grid = [F(k, 8) for k in range(-8, 33)]
inside = lambda v, a, b: a <= v <= b
for x in grid:
    for y in grid:
        lhs = (inside(x, 0, 2) and inside(y, 0, 1)) and (inside(x, 1, 3) and inside(y, 0, 2))
        rhs = inside(x, 1, 2) and inside(y, 0, 1)
        assert lhs == rhs, (x, y)
print("exm-product-of-intervals: all quoted values check")
