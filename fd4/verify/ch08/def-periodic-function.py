"""def-periodic-function examples: x - floor(x) and dist(., Z) have period 1 (and every
non-zero integer), dist does not have period 1/2."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, dist, rationals
for x in rationals():
    for p in (1, -1, 2, -3):
        assert (x + p) - floor(x + p) == x - floor(x) and dist(x + p) == dist(x)
assert dist(F(1, 2)) != dist(0)
print("def-periodic-function: OK")
