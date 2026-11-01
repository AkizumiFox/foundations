"""C2: dist(nx) <= n dist(x); equality when dist(x) <= 1/(2n); x = 1/2, n = 2 gives 0 < 1."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, dist, rationals
QUOTED = {"c": (0, 1)}
for x in rationals(2000):
    for n in range(1, 9):
        assert dist(n * x) <= n * dist(x)
        if dist(x) <= F(1, 2 * n):
            assert dist(n * x) == n * dist(x)
assert (dist(1), 2 * dist(F(1, 2))) == QUOTED["c"]
print("exr-floor-and-step-functions-c2: OK")
