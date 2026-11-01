"""8.2 B2 (c), (d): h = x^3 - x at -1, -1/2, 0 is 0, 3/8, 0; bracket at 1/2, 3/5 is 0.91;
f(1/2) = -3/8 = -375/1000, f(3/5) = -48/125 = -384/1000; on [1, oo) the bracket exceeds 2."""
from fractions import Fraction as F
import random

h = lambda x: x ** 3 - x
QUOTED = {"c": [0, F(3, 8), 0], "bracket": F(91, 100), "f12": F(-3, 8), "f35": F(-48, 125)}
assert [h(F(-1)), h(F(-1, 2)), h(F(0))] == QUOTED["c"]
x, y = F(1, 2), F(3, 5)
br = x * x + x * y + y * y - 1
assert x * x + x * y + y * y == F(25, 100) + F(30, 100) + F(36, 100)
assert br == QUOTED["bracket"] - 1 < 0
assert h(y) - h(x) == (y - x) * br
assert h(x) == QUOTED["f12"] == F(-375, 1000) and h(y) == QUOTED["f35"] == F(-384, 1000)
assert h(x) > h(y)
random.seed(6)
for _ in range(2000):
    a, b = sorted(F(random.randint(100, 3000), 100) for _ in range(2))
    if a == b:
        continue
    assert a * a + a * b + b * b - 1 > 2 and h(a) < h(b)
print("ok")
