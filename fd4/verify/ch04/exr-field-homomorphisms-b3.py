"""exr-field-homomorphisms-b3: on (Q, +, odot) with a odot b = 2ab, the one is 1/2;
f(x) = 2x satisfies f(a + b) = f(a) + f(b), f(a odot b) = 4ab = f(a) f(b), f(1/2) = 1,
and x -> x/2 is its two-sided inverse."""
from fractions import Fraction as F
import random

QUOTED = {"one_of_F": F(1, 2), "f_of_one": 1}
odot = lambda a, b: 2 * a * b
f = lambda x: 2 * x
g = lambda x: x / 2
random.seed(17)
for _ in range(2000):
    a = F(random.randint(-60, 60), random.randint(1, 9))
    b = F(random.randint(-60, 60), random.randint(1, 9))
    assert odot(a, QUOTED["one_of_F"]) == a
    assert f(a + b) == f(a) + f(b)
    assert f(odot(a, b)) == 4 * a * b == f(a) * f(b)
    assert g(f(a)) == a and f(g(a)) == a
assert f(QUOTED["one_of_F"]) == QUOTED["f_of_one"]
print("ok")
