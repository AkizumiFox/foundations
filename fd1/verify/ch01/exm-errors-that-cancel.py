"""exm-errors-that-cancel (Section 1.4, fold "Two errors that cancel"): x = -4 breaks the step
"x^2 > 9, so x > 3"; the claim "x > 3 implies x^2 > 9" is true (on a grid); the box would earn
"(x^2 > 9) -> (x > 3)", which is false."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid

QUOTED = {"x": -4, "x^2": 16}
x = QUOTED["x"]
assert x * x == QUOTED["x^2"] and x * x > 9 and not x > 3
assert all((not t > 3) or (t > 0 and t * t > 3 * t > 9) for t in grid())
assert not all((not t * t > 9) or t > 3 for t in grid())
print("exm-errors-that-cancel: checks")
