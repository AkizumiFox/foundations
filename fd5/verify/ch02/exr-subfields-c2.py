"""exr-subfields-c2: 1/(1+1) = 1/2 != 2 = 1/1 + 1/1; for a = b = 1 the wrong formula gives
1 + (1/2) sqrt 2, and (1 + sqrt 2)(1 + (1/2) sqrt 2) = 2 + (3/2) sqrt 2 != 1;
the true inverse of 1 + sqrt 2 is -1 + sqrt 2."""
from fractions import Fraction as F

QUOTED = {"wrong_product": (F(2), F(3, 2)), "true_inverse": (F(-1), F(1))}


def mul(u, v):
    (a, b), (c, d) = u, v
    return (a * c + 2 * b * d, a * d + b * c)


assert F(1, 2) != F(1) + F(1)
assert mul((F(1), F(1)), (F(1), F(1, 2))) == QUOTED["wrong_product"]
assert QUOTED["wrong_product"] != (1, 0)
assert mul((F(1), F(1)), QUOTED["true_inverse"]) == (1, 0)
# 1/(b sqrt 2) = (1/(2b)) sqrt 2 for b != 0: (b sqrt2)(1/(2b) sqrt2) = 1
for b in [F(1), F(-3), F(2, 5)]:
    assert mul((0, b), (0, 1 / (2 * b))) == (1, 0)
print("ok")
