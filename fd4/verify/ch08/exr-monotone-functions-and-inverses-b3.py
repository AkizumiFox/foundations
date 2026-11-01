"""8.2 B3: s(x) = x|x|; on x < y <= 0, s(y) - s(x) = (x - y)(x + y); s strictly increasing;
s(-sqrt(-v)) = v for v < 0 (checked on squares)."""
from fractions import Fraction as F
import random

s = lambda x: x * abs(x)
random.seed(7)
for _ in range(3000):
    x, y = sorted(F(random.randint(-500, 500), random.randint(1, 40)) for _ in range(2))
    if x == y:
        continue
    if y <= 0:
        assert s(y) - s(x) == (x - y) * (x + y)
    assert s(x) < s(y)
    r = F(random.randint(1, 300), random.randint(1, 30))   # r = sqrt(-v) for v = -r^2
    assert s(-r) == -(r * r) and s(r) == r * r
print("ok")
