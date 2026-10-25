"""def-preimage and the other new quick checks of Section 1.7 (squaring on R; constant map), checked on fine rational grids."""
from fractions import Fraction as F
QUOTED = {"f({-1,2})": [1, 4], "pre {9}": [-3, 3], "pre [-1,4]": [-2, 2], "f([1,3])": [1, 9],
          "pre [1,9]": [-3, -1, 1, 3], "pre [-4,9]": [-3, 3, -4, 9], "f([-3,3])": [0, 9]}
sq = lambda x: x * x
grid = lambda lo, hi, n=1200: [F(lo) + (F(hi) - F(lo)) * k / n for k in range(n + 1)]
assert sorted({sq(x) for x in (-1, 2)}) == QUOTED["f({-1,2})"]
assert [x for x in range(-20, 21) if sq(x) == 9] == QUOTED["pre {9}"]
assert all((-1 <= sq(x) <= 4) == (-2 <= x <= 2) for x in grid(-6, 6))
assert all(not (sq(x) < 0) for x in grid(-6, 6))
assert min(sq(x) for x in grid(1, 3)) == 1 and max(sq(x) for x in grid(1, 3)) == 9
assert all((1 <= sq(x) <= 9) == (-3 <= x <= -1 or 1 <= x <= 3) for x in grid(-6, 6))
assert all((-4 <= sq(x) <= 9) == (-3 <= x <= 3) for x in grid(-6, 6))
assert min(sq(x) for x in grid(-3, 3)) == 0 and max(sq(x) for x in grid(-3, 3)) == 9
# constant map: c({x1} & {x2}) = empty, c({x1}) & c({x2}) = {y0}
x1, x2, y0 = "p", "q", "y0"
c = lambda A: {y0 for _ in A}
assert c({x1} & {x2}) == set() and c({x1}) & c({x2}) == {y0}
print("1.7 quick checks: ok")
