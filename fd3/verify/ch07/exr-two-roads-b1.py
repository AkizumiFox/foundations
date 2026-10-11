"""exr-two-roads-b1 (Section 7.6): for q < x + y, d = x + y - q, a rational a with x - d/2 < a < x and
b = q - a satisfy b < y - d/2 < y. Checked with exact rationals standing in for x, y (any ordered field)."""
from fractions import Fraction as F
import random

QUOTED = {"half": True}
random.seed(17)
for _ in range(5000):
    x = F(random.randint(-500, 500), random.randint(1, 60))
    y = F(random.randint(-500, 500), random.randint(1, 60))
    q = x + y - F(random.randint(1, 400), random.randint(1, 60))
    d = x + y - q
    a = x - d / 2 + (d / 2) * F(random.randint(1, 99), 100)   # strictly between x - d/2 and x
    b = q - a
    assert d > 0 and x - d / 2 < a < x
    assert b < y - d / 2 < y and a + b == q
print("ok")
