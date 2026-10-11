"""Values quoted in exr-statements-and-connectives-c1 (Section 1.1)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {"counterexample to 'x^2 = 4 only if x = 2'": -2}
c = QUOTED["counterexample to 'x^2 = 4 only if x = 2'"]
assert c**2 == 4 and c != 2
# "x^2 = 4 if x = 2" holds on the grid; "x^2 > 0 unless x = 0" holds on the grid
assert implies_on_grid(lambda x: x == 2, lambda x: x**2 == 4)
assert implies_on_grid(lambda x: x != 0, lambda x: x**2 > 0)
print("exr-statements-and-connectives-c1: checks")
