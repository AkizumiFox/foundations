"""exr-biconditional-and-definitions-a2 (Ch 2, Section 2.4): (c) x^2 = 4 exactly at x = 2 and x = -2
(by factoring, and on a grid of rationals); (d) 12 = 3 * 4."""
from fractions import Fraction as F

QUOTED = {"roots": {2, -2}, "12": (3, 4)}

# x^2 - 4 = (x - 2)(x + 2), zero exactly when a factor is zero
assert all(x * x - 4 == (x - 2) * (x + 2) for x in range(-50, 51))
for k in range(-400, 401):
    x = F(k, 20)
    assert (x * x == 4) == (x in QUOTED["roots"])
assert QUOTED["12"][0] * QUOTED["12"][1] == 12
print("exr-biconditional-and-definitions-a2: all quoted values check")
