"""8.2 B1: f(x) = x + 1/x; f(y) - f(x) = (y - x)(xy - 1)/(xy)."""
from fractions import Fraction as F
import random

f = lambda x: x + 1 / x
random.seed(5)
for _ in range(3000):
    x, y = sorted(F(random.randint(1, 900), random.randint(1, 90)) for _ in range(2))
    if x == y:
        continue
    assert f(y) - f(x) == (y - x) * (x * y - 1) / (x * y)
    if x >= 1:
        assert f(x) < f(y)
    if y <= 1:
        assert f(x) > f(y)
print("ok")
