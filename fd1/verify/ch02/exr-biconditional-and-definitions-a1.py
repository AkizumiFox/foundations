"""exr-biconditional-and-definitions-a1 (Ch 2, Section 2.4): x^2 = x iff x in {0, 1} (x >= 0);
10 = 2*5; x = -2 has x^2 = 4 > 1 and x < 1."""
from fractions import Fraction as F

QUOTED = {"k for 10": 5, "(d) witness": -2}

pts = [F(k, 16) for k in range(0, 161)]
assert all((x * x == x) == (x in (0, 1)) for x in pts)
assert 2 * QUOTED["k for 10"] == 10
x = QUOTED["(d) witness"]
assert x * x == 4 > 1 and x < 1
print("exr-biconditional-and-definitions-a1: all quoted values check")
