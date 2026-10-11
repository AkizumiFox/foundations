"""exr-proving-an-implication-b2 (c): x^2 >= 0 for every real x, so x > 5 implies x^2 >= 0."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies, everywhere

assert everywhere(lambda x: x**2 >= 0, (0, 5))
assert implies(lambda x: x > 5, lambda x: x**2 >= 0, (0, 5))
print("exr-proving-an-implication-b2: checks")
