"""exr-contradiction-and-vacuous-truth-b3 (Ch 2, Section 2.1): x^2 + 1 >= 1 > 0 for real x, so the
hypothesis x^2 + 1 <= 0 never holds (checked on a grid of exact rationals); no real is both > 100
and < -100."""
from fractions import Fraction as F

QUOTED = {"lower bound of x^2 + 1": 1}
xs = [F(p, q) for p in range(-400, 401) for q in (1, 2, 3, 7, 10)]
for x in xs:
    assert x * x + 1 >= QUOTED["lower bound of x^2 + 1"] > 0
    assert not (x * x + 1 <= 0)
    assert not (x > 100 and x < -100)
print("exr-contradiction-and-vacuous-truth-b3: all quoted values check")
