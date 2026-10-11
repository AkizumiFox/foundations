"""exr-using-an-implication-b2 (Section 1.4): both facts hold for every real x."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {}
assert implies_on_grid(lambda x: 0 < x < 1, lambda x: x**2 < x)
assert implies_on_grid(lambda x: x**2 < x, lambda x: x**3 < x**2)
assert implies_on_grid(lambda x: x**2 < x, lambda x: x > 0)        # x(x - 1) < 0 forces x > 0
print("exr-using-an-implication-b2: checks")
