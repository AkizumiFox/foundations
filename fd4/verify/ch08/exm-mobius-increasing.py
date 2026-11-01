"""exm-mobius-increasing and Quick check 4 of 8.2: g(x) = (x - 1)/(x + 2) on (-2, oo).
Difference numerator 3(y - x); g = 1 - 3/(x + 2); inverse (1 + 2v)/(1 - v) on (-oo, 1);
x + 2 = 3/(1 - v), x - 1 = 3v/(1 - v)."""
from fractions import Fraction as F
import random

QUOTED = {"numerator_factor": 3, "inverse": lambda v: (1 + 2 * v) / (1 - v)}
g = lambda x: (x - 1) / (x + 2)
random.seed(1)
for _ in range(3000):
    x, y = (F(random.randint(-199, 999), random.randint(1, 97)) for _ in range(2))
    if x <= -2 or y <= -2:
        continue
    assert (y - 1) * (x + 2) - (x - 1) * (y + 2) == QUOTED["numerator_factor"] * (y - x)
    assert g(y) - g(x) == 3 * (y - x) / ((x + 2) * (y + 2))
    assert g(x) == 1 - F(3) / (x + 2) and g(x) < 1
    if x < y:
        assert g(x) < g(y)
    v = F(random.randint(-999, 99), random.randint(1, 97))
    if v >= 1:
        continue
    u = QUOTED["inverse"](v)
    assert u > -2 and u + 2 == 3 / (1 - v) and u - 1 == 3 * v / (1 - v)
    assert g(u) == v and QUOTED["inverse"](g(x)) == x
print("ok")
