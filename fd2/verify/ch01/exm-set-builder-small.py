"""exm-set-builder-small (Section 6.1): {x in Z : x^2 < 5} = {-2,...,2}; {x in R : x^2 < 0} is empty."""
QUOTED = {"elements": (-2, -1, 0, 1, 2), "squares": (4, 1, 0, 1, 4), "first excluded square": 9}
# integers with |x| >= 3 have x^2 >= 9 > 5, so a finite search window suffices
S = sorted(x for x in range(-50, 51) if x * x < 5)
assert tuple(S) == QUOTED["elements"]
assert tuple(x * x for x in S) == QUOTED["squares"]
assert all(x * x >= 9 for x in range(-50, 51) if abs(x) >= 3) and 3 * 3 == QUOTED["first excluded square"]
# x^2 >= 0 on a sample of reals (exact rationals)
from fractions import Fraction as F
assert all(F(n, 7) ** 2 >= 0 for n in range(-100, 101))
print("exm-set-builder-small: all quoted values check")
