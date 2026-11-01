"""A2: (a) x = 1/2: floor 1 = 1, 2 floor(1/2) = 0; (b) x = y = -1/2: 1 > floor(1/4) = 0;
(c) dist(2x) <= 2 dist(x) on many rationals."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, dist, rationals
h = F(1, 2)
assert floor(2 * h) == 1 and 2 * floor(h) == 0
assert floor(-h) * floor(-h) == 1 and floor(h * h) == 0
assert all(dist(2 * x) <= 2 * dist(x) for x in rationals())
print("exr-floor-and-step-functions-a2: OK")
