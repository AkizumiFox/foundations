"""exm-unit-interval-tfae (Ch 2, Section 2.4): 0 < x < 1, x^2 < x, (x > 0 and 1/x > 1) agree."""
from fractions import Fraction as F

QUOTED = {"interval": (0, 1)}

pts = sorted({F(k, 64) for k in range(-256, 257)} | {F(1, 10**6), 1 - F(1, 10**6), F(-1, 10**6)})
for x in pts:
    a = 0 < x < 1
    b = x * x < x
    c = x > 0 and 1 / x > 1
    assert a == b == c
print("exm-unit-interval-tfae: all quoted values check")
