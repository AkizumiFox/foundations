"""A1: floor(-0.01) = -1; ceil 2 = 2; floor 2.999 + ceil(-2.999) = 0; dist(-2.7) = 0.3; dist(13/4) = 1/4."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, ceil, dist
QUOTED = {"a": -1, "b": 2, "c": 0, "d": F(3, 10), "e": F(1, 4)}
assert floor(F(-1, 100)) == QUOTED["a"] and ceil(2) == QUOTED["b"]
assert floor(F(2999, 1000)) + ceil(F(-2999, 1000)) == QUOTED["c"]
assert dist(F(-27, 10)) == QUOTED["d"] and floor(F(-27, 10)) == -3
assert dist(F(13, 4)) == QUOTED["e"] and floor(F(13, 4)) == 3
print("exr-floor-and-step-functions-a1: OK")
