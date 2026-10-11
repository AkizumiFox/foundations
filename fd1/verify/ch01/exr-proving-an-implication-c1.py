"""exr-proving-an-implication-c1 (c): P: x > 2, Q: x > 3, R: x > 1."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

QUOTED = {"refuting value x": 0}
assert implies(lambda x: x > 2 and x > 3, lambda x: x > 1, (1, 2, 3))   # premise true for every x
assert not QUOTED["refuting value x"] > 1                              # conclusion fails at 0
print("exr-proving-an-implication-c1: checks")
