"""exm-images-of-square (Ch 6, Section 6.6) and the quick check after it: squaring on R."""
from fractions import Fraction as F
QUOTED = {"f([-1,2]) = [0, c]": 4, "preimage of [1,4] endpoints": [-2, -1, 1, 2],
          "check: preimage of {4}": [-2, 2]}
def grid(lo, hi, n=600):
    lo, hi = F(lo), F(hi)
    return [lo + (hi - lo) * k / n for k in range(n + 1)]
sq = lambda x: x * x
# (a): squares of [-1,2] lie in [0,4]; the witness sqrt(y) of y in [0,4] lies in [0,2] (checked on squares)
assert all(0 <= sq(a) <= 4 for a in grid(-1, 2))
assert all(0 <= r <= 2 and -1 <= r for r in grid(0, 2))   # r = sqrt(y) ranges over [0,2]
assert max(sq(a) for a in grid(-1, 2)) == 4 and min(sq(a) for a in grid(-1, 2)) == 0
# (b): 1 <= x^2 <= 4 iff x in [-2,-1] u [1,2]
inside = lambda x: -2 <= x <= -1 or 1 <= x <= 2
assert all((1 <= sq(x) <= 4) == inside(x) for x in grid(-5, 5, 2000))
# (c) and quick check
assert all(sq(x) >= 0 > -1 for x in grid(-5, 5))
assert [x for x in range(-10, 11) if sq(x) == 4] == [-2, 2]
# (d): 0 <= x^2 <= 1 iff x in [-1,1]
assert all((0 <= sq(x) <= 1) == (-1 <= x <= 1) for x in grid(-3, 3, 1200))
print("exm-images-of-square: all quoted values check")
