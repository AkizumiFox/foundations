"""exm-subfields-gaussian: in Q(i), (a + bi)(c + di) = (ac - bd) + (ad + bc)i,
(c + di)(c - di) = c^2 + d^2 > 0 for (c, d) != (0, 0), and the inverse c/M - (d/M) i;
in Z[i], 2u = 1 has no solution (u would be 1/2)."""
from fractions import Fraction as F
import random

QUOTED = {"inverse_of_2_in_C": (F(1, 2), F(0))}


def mul(u, v):
    (a, b), (c, d) = u, v
    return (a * c - b * d, a * d + b * c)


random.seed(7)
for _ in range(3000):
    u = (F(random.randint(-30, 30), random.randint(1, 9)), F(random.randint(-30, 30), random.randint(1, 9)))
    if u == (0, 0):
        continue
    c, d = u
    M = c * c + d * d
    assert M > 0
    assert mul(u, (c, -d)) == (M, 0)
    assert mul(u, (c / M, -d / M)) == (1, 0)

# inverse of 2 in C is 1/2 + 0i, whose real part is not an integer
assert mul((F(2), F(0)), QUOTED["inverse_of_2_in_C"]) == (1, 0)
assert QUOTED["inverse_of_2_in_C"][0].denominator != 1
# no Gaussian integer u with 2u = 1 (search a box; the algebra shows none exists at all)
for a in range(-10, 11):
    for b in range(-10, 11):
        assert mul((2, 0), (a, b)) != (1, 0)
print("ok")
