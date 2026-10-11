"""exr-excluded-middle-r1 (Ch 5, Section 5.7): for m in (0, 1), a = (m + 1)/2 satisfies
a - m = (1 - m)/2 > 0 and 1 - a = (1 - m)/2 > 0, hence 0 < m < a < 1."""
from fractions import Fraction as F

QUOTED = {"witness": "(m + 1)/2"}

samples = [F(k, 1000) for k in range(1, 1000)] + [F(1, 10 ** 9), 1 - F(1, 10 ** 9)]
for m in samples:
    a = (m + 1) / 2
    assert a - m == (1 - m) / 2 > 0
    assert 1 - a == (1 - m) / 2 > 0
    assert 0 < m < a < 1
print("exr-excluded-middle-r1: all quoted values check")
