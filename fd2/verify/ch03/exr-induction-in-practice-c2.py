"""exr-induction-in-practice-c2 (Ch 7, 02): the least positive denominator of a rational is in lowest
terms (no common divisor d >= 2), checked on a range of fractions."""
from fractions import Fraction as F
from math import gcd
for p in range(-60, 61):
    for q in range(1, 61):
        r = F(p, q)
        m = min(d for d in range(1, q + 1) if (r * d).denominator == 1)
        num = r * m
        assert gcd(int(num), m) == 1
print("exr-induction-in-practice-c2: all quoted values check")
