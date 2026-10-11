"""School-algebra facts quoted in Section 1.3 (03-conjunction): exm-product-in-unit-interval,
the warning on and-E applied to an implication, and exr-conjunction-b2."""
import sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {"warning refuting x": -1, "b2 sums": (4, 6)}

# exm-product-in-unit-interval: 0 < x < 1 and 0 < y < 1 give 0 < xy < 1 (sampled on a rational grid)
pts = [Fraction(k, 37) for k in range(1, 37)]
for x in pts:
    for y in pts:
        assert 0 < x * y < 1
        assert x * y < x          # multiplying y < 1 by x > 0
# the grid near the boundary as well
assert all(0 < x * y < 1 for x in (Fraction(1, 10**9), 1 - Fraction(1, 10**9)) for y in (Fraction(1, 10**9), 1 - Fraction(1, 10**9)))

# warning: (x > 0 and x > 1) -> x^2 > 1 holds for every x; x > 0 fails at x = -1
assert implies_on_grid(lambda x: x > 0 and x > 1, lambda x: x**2 > 1)
x0 = QUOTED["warning refuting x"]
assert (not (x0 > 0 and x0 > 1)) or x0**2 > 1   # the premise holds at x0
assert not x0 > 0                               # the illegal line is false there

# exr-conjunction-b2: 1 < x < 2 and 3 < y < 4 give 4 < x + y < 6
lo, hi = QUOTED["b2 sums"]
assert 1 + 3 == lo and 2 + 4 == hi
for x in [Fraction(k, 23) for k in range(24, 46)]:
    for y in [Fraction(k, 23) for k in range(70, 92)]:
        assert 1 < x < 2 and 3 < y < 4
        assert lo < x + y < hi
print("exm-product-in-unit-interval: checks")
