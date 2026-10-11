"""exm-illegal-citation and the warning after it (Section 1.5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

QUOTED = {"refuting value x": 0}
x0 = QUOTED["refuting value x"]
B = (-1, 0, 1, 2, 3)
# P: x > 3, Q: x > 2, R: x > 1 -- both premises true for every x, R false at 0
assert implies(lambda x: x > 3, lambda x: x > 2, B) and implies(lambda x: x > 2, lambda x: x > 1, B)
assert not x0 > 1
# the warning: x > 1 gives x^2 > 1 and x^3 > 1 inside the box; x^3 > 1 fails at 0
assert implies(lambda x: x > 1, lambda x: x**2 > 1, B) and implies(lambda x: x > 1, lambda x: x**3 > 1, B)
assert not x0**3 > 1
print("exm-illegal-citation: checks")
