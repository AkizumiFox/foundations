"""def-cut-product-positive (Section 7.4, lead-in): if 0 is in alpha and beta, every rational is a product
(x = (-1)(-x) for x > 0, 0 = 0*0, x = a*(x/a) for x < 0, a > 0 in alpha); for D_1 the factors are in D_1;
for D_{-1}: x > 1 is p q with p = -(1 + x)/2 < -1, q = -2x/(1 + x) < -1, and p, q < -1 give pq > 1."""
from fractions import Fraction as Fr
import random

QUOTED = {"neg_one": -1}
random.seed(4)
D1 = lambda v: v < 1
Dm1 = lambda v: v < -1
a = Fr(1, 2)  # a positive element of D_1
for _ in range(5000):
    x = Fr(random.randint(-10**5, 10**5), random.randint(1, 10**3))
    if x > 0:
        assert QUOTED["neg_one"] * (-x) == x and D1(Fr(-1)) and D1(-x)
    elif x < 0:
        assert a * (x / a) == x and D1(a) and D1(x / a)
    if x > 1:
        p = -(1 + x) / 2
        q = -2 * x / (1 + x)
        assert Dm1(p) and Dm1(q) and p * q == x
    p = -1 - Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    q = -1 - Fr(random.randint(1, 10**4), random.randint(1, 10**3))
    assert p * q > 1
# {x > 1} contains 2, not 0
assert 2 > 1 and not 0 > 1
print("ok")
