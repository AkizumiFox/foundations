"""exr-permutations-and-iteration-r1: f(x) = 2x + 1 has f^n(x) = 2^n x + 2^n - 1 (exact rationals)."""
from fractions import Fraction as F

QUOTED = {"factor": 2, "shift": 1}  # f(x) = 2x + 1


def formula(n, x):
    return 2 ** n * x + 2 ** n - 1


a, b = QUOTED["factor"], QUOTED["shift"]
for x in [F(0), F(1), F(-3, 2), F(7, 3)]:
    y = x
    for n in range(12):
        assert y == formula(n, x)
        assert 2 * formula(n, x) + 1 == formula(n + 1, x)
        y = a * y + b
print("exr-permutations-and-iteration-r1: all quoted values check")
