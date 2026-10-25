"""exm-q-sqrt2-field: product formula in Q(sqrt 2), the conjugate norm c^2 - 2d^2,
the inverse formula, and the inverse of 1 + 2 sqrt 2 (N = -7, inverse (-1 + 2 sqrt 2)/7).
Elements a + b sqrt 2 are exact pairs (a, b) of fractions, multiplied with r^2 = 2."""
from fractions import Fraction as F
import random

QUOTED = {
    "N_for_1_plus_2sqrt2": -7,
    "inverse_of_1_plus_2sqrt2": (F(-1, 7), F(2, 7)),
    "check_product": 7,  # (1 + 2 sqrt 2)(-1 + 2 sqrt 2)
}


def mul(u, v):
    (a, b), (c, d) = u, v
    return (a * c + 2 * b * d, a * d + b * c)


def inv(u):
    c, d = u
    n = c * c - 2 * d * d
    assert n != 0
    return (c / n, -d / n)


random.seed(5)
for _ in range(3000):
    u = (F(random.randint(-30, 30), random.randint(1, 9)), F(random.randint(-30, 30), random.randint(1, 9)))
    if u == (0, 0):
        continue
    c, d = u
    assert mul(u, (c, -d)) == (c * c - 2 * d * d, 0)
    assert mul(u, inv(u)) == (1, 0)

y = (F(1), F(2))
N = y[0] ** 2 - 2 * y[1] ** 2
assert N == QUOTED["N_for_1_plus_2sqrt2"]
assert inv(y) == QUOTED["inverse_of_1_plus_2sqrt2"]
assert mul(y, (F(-1), F(2))) == (QUOTED["check_product"], 0)
# the expanded check: -1 + 2 sqrt2 - 2 sqrt2 + 8 = 7
assert -1 + 8 == 7
print("ok")
