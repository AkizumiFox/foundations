"""exm-method-floor-inequality and the warning: floor(-2.5) = -3, truncation gives -2;
x - 1/2 <= x < (x - 1/2) + 1 for every x."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, rationals
QUOTED = {"floor(-2.5)": -3, "truncation": -2}
assert floor(F(-5, 2)) == QUOTED["floor(-2.5)"]
assert int(-2.5) == QUOTED["truncation"] and not (-2 <= F(-5, 2))
for x in rationals():
    assert x - F(1, 2) <= x < x - F(1, 2) + 1
print("exm-method-floor-inequality: OK")
