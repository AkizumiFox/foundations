"""exr-countable-unions-and-choice-b1 (a): n + 1/2 lies strictly between n and n + 1."""
from fractions import Fraction

QUOTED = {"half": Fraction(1, 2)}            # n + \frac12
h = QUOTED["half"]
assert all(n < n + h < n + 1 for n in range(1000))
print("exr-countable-unions-and-choice-b1: all quoted values check")
