"""The warning after def-surjective (Ch 6 Section 6.4): x^2 + x hits 0, 2, 6, 12 at 0, 1, 2, 3,
and never -1, since x^2 + x + 1 = (x + 1/2)^2 + 3/4."""
from fractions import Fraction as F

QUOTED = {"values": (0, 2, 6, 12), "missed": -1, "3/4": F(3, 4)}

f = lambda x: x * x + x
assert tuple(f(x) for x in range(4)) == QUOTED["values"]
pts = [F(k, 18) for k in range(-90, 91)]
assert all(x * x + x + 1 == (x + F(1, 2)) ** 2 + QUOTED["3/4"] for x in pts)
assert all(f(x) != QUOTED["missed"] for x in pts)
assert min(f(x) for x in pts) == F(-1, 4) > -1   # attained at x = -1/2
print("def-surjective: all quoted values check")
