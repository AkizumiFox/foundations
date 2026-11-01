"""exr-dot-product-a1: (a) value; (b) <2x,2y> = 4<x,y>, counterexample x = y = e1; (d) e1 perp e2."""
from fractions import Fraction as Fr


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"a": -1, "b_lhs": 4, "b_rhs": 2}
assert dot((1, -2, 0, 3), (4, 1, 7, -1)) == QUOTED["a"]
e1, e2 = (1, 0), (0, 1)
assert dot((2, 0), (2, 0)) == QUOTED["b_lhs"] and 2 * dot(e1, e1) == QUOTED["b_rhs"]
assert dot(e1, e2) == 0
print("ok")
