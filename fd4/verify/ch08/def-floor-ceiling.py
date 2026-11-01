"""def-floor-ceiling examples and Quick check 1: floor 3.7 = 3, floor 5 = 5,
floor -0.2 = -1, ceil 3.7 = 4; floor(-7/2) = -4, ceil(-7/2) = -3, floor(7/2)+floor(-7/2) = -1."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, ceil, rationals
QUOTED = {"ex": (3, 5, -1, 4), "qc1": (-4, -3, -1)}
assert (floor(F(37, 10)), floor(5), floor(F(-2, 10)), ceil(F(37, 10))) == QUOTED["ex"]
assert (floor(F(-7, 2)), ceil(F(-7, 2)), floor(F(7, 2)) + floor(F(-7, 2))) == QUOTED["qc1"]
for x in rationals():
    m = floor(x)
    assert m <= x < m + 1 and 0 <= x - m < 1
print("def-floor-ceiling: OK")
