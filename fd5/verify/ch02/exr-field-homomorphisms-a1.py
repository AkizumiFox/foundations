"""exr-field-homomorphisms-a1 (c): with conjugation on C, a = 1 + i, b = 1 - i:
a - b = 2i, conj(2i) = -2i, conj(a) = 1 - i, conj(b) = 1 + i.
Also the warning and B3 of Section 2.4: f(x) = 2x has f(1*1) = 2 != 4 = f(1)f(1);
on (Q, +, odot) with a odot b = 2ab, f(a odot b) = f(a) f(b) and f(1/2) = 1."""
from fractions import Fraction as F
import random

QUOTED = {"a_minus_b": (0, 2), "conj_a_minus_b": (0, -2), "conj_a": (1, -1), "conj_b": (1, 1)}


def conj(z):
    return (z[0], -z[1])


a, b = (1, 1), (1, -1)
d = (a[0] - b[0], a[1] - b[1])
assert d == QUOTED["a_minus_b"]
assert conj(d) == QUOTED["conj_a_minus_b"]
assert conj(a) == QUOTED["conj_a"] and conj(b) == QUOTED["conj_b"]
assert conj(a) != conj(b)

f = lambda x: 2 * x
assert f(1 * 1) == 2 and f(1) * f(1) == 4
random.seed(13)
for _ in range(1000):
    x = F(random.randint(-50, 50), random.randint(1, 9))
    y = F(random.randint(-50, 50), random.randint(1, 9))
    assert f(x + y) == f(x) + f(y)
    assert f(2 * x * y) == f(x) * f(y)
assert f(F(1, 2)) == 1
print("ok")
