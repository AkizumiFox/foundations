"""Values quoted around def-rules-implication (Section 1.5): the hook "if x > 2, then x^2 > 4"."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

QUOTED = {"refuting value x": 0}
B = (-2, 0, 2)
assert implies(lambda x: x > 2, lambda x: x > 0, B)
assert implies(lambda x: x > 2, lambda x: x**2 > 2 * x, B)
assert implies(lambda x: x > 2, lambda x: 2 * x > 4, B)
assert implies(lambda x: x > 2, lambda x: x**2 > 4, B)
x0 = QUOTED["refuting value x"]
assert not (x0**2 > 2 * x0) and not (2 * x0 > 4) and not (x0**2 > 4)   # all three fail at 0
print("def-rules-implication: checks")
