"""exr-connective-rhetoric-a1 (Ch 5, Section 5.1): 3 < 7/2 < 4, so 7 = 2k has no integer solution."""
from fractions import Fraction as Fr

QUOTED = {"k": Fr(7, 2)}
assert 3 < QUOTED["k"] < 4 and 2 * QUOTED["k"] == 7
assert all(2 * k != 7 for k in range(-10, 11))
print("exr-connective-rhetoric-a1: all quoted values check")
