"""Values quoted in exr-statements-and-connectives-c2 (Section 1.1)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {"counterexample to necessity": -2}
sq = lambda x: x**2 > 1
assert implies_on_grid(lambda x: x > 1, sq)                         # sufficient
c = QUOTED["counterexample to necessity"]
assert c**2 > 1 and not c > 1                                       # not necessary
cond = lambda x: x > 1 or x < -1
assert implies_on_grid(cond, sq) and implies_on_grid(sq, cond)      # necessary and sufficient
assert implies_on_grid(sq, lambda x: abs(x) > 1) and implies_on_grid(lambda x: abs(x) > 1, sq)
print("exr-statements-and-connectives-c2: checks")
