"""exr-sets-and-subsets-b1: x^2 - 3x + 2 = (x - 1)(x - 2), roots {1, 2}."""
from fractions import Fraction as F
QUOTED = {"roots": (1, 2)}
# the factorization, checked as polynomial identity at more points than the degree
for n in range(-10, 11):
    x = F(n, 3)
    assert x * x - 3 * x + 2 == (x - 1) * (x - 2)
# roots: the quadratic formula gives (3 +- 1)/2
disc = 3 * 3 - 4 * 2
assert disc == 1
assert tuple(sorted(((3 - 1) // 2, (3 + 1) // 2))) == QUOTED["roots"]
assert 1 - 3 + 2 == 0 and 4 - 6 + 2 == 0
print("exr-sets-and-subsets-b1: all quoted values check")
