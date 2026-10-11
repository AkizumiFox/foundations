"""exr-proving-an-implication-b3 (b): the two facts and the conclusion about |x - 2| < 1."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

p = lambda x: abs(x - 2) < 1
B = (1, 2, 3)
assert implies(p, lambda x: x > 1, B) and implies(p, lambda x: x < 3, B)
assert implies(p, lambda x: 1 < x < 3, B)
print("exr-proving-an-implication-b3: checks")
