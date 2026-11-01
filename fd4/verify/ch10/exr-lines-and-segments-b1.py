"""exr-lines-and-segments-b1: (1-s)(p+av)+s(p+bv) = p+(a+s(b-a))v; s = (t-a)/(b-a) in [0,1] gives p+tv (random exact)."""
import random
from fractions import Fraction as Fr

random.seed(7)
R = lambda: Fr(random.randint(-30, 30), random.randint(1, 7))
for _ in range(300):
    p = tuple(R() for _ in range(3)); v = tuple(R() for _ in range(3))
    a = R(); b = a + abs(R()) + Fr(1, 3)
    t = a + (b - a) * Fr(random.randint(0, 10), 10)
    s = (t - a) / (b - a)
    assert 0 <= s <= 1
    lhs = tuple((1 - s) * (pi + a * vi) + s * (pi + b * vi) for pi, vi in zip(p, v))
    assert lhs == tuple(pi + (a + s * (b - a)) * vi for pi, vi in zip(p, v)) == tuple(pi + t * vi for pi, vi in zip(p, v))
print("ok")
