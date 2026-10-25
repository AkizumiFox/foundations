"""exr-contrapositive-and-contradiction-b2 (F2.2 §04): (a) no rational r with r^2 = r + 1 (p^2 = pq + q^2,
parity cases); (b) no integers with m^2 - 8n = 5; odd squares are 8t + 1."""
from fractions import Fraction as Fr
from math import gcd
for q in range(1, 300):
    for p in range(-600, 600):
        if gcd(p, q) == 1:
            assert Fr(p, q) ** 2 != Fr(p, q) + 1
for p in range(-50, 50):
    for q in range(-50, 50):
        if p % 2 or q % 2:
            assert (p * p) % 2 != (p * q + q * q) % 2
for m in range(-3000, 3000):
    assert (m * m - 5) % 8 != 0
    if m % 2:
        assert m * m % 8 == 1
print("exr-contrapositive-and-contradiction-b2: all quoted values check")
