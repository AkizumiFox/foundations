"""8.2 C1: f(x) = x^3 - 3x; f(y) - f(x) = (y - x)(y^2 + xy + x^2 - 3); at x = y = 1 the bracket is 0
(the illegal step's witness 1 * 0 = 0 shape); strictly increasing on [1, oo) (sampled)."""
from fractions import Fraction as F
import random

f = lambda x: x ** 3 - 3 * x
assert 1 + 1 + 1 - 3 == 0
random.seed(8)
for _ in range(3000):
    x, y = (F(random.randint(-500, 500), random.randint(1, 40)) for _ in range(2))
    assert f(y) - f(x) == (y - x) * (y * y + x * y + x * x - 3)
    a, b = sorted((abs(x) + 1, abs(y) + 1))
    if a < b:
        assert b * b + a * b + a * a > 3 and f(a) < f(b)
print("ok")
