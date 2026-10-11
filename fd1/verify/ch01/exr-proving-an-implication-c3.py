"""exr-proving-an-implication-c3 (b): P: x > 5, Q: x > 4, R: x^2 > 16, S: x^2 > 9."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

QUOTED = {"P": "x > 5", "Q": "x > 4", "R": "x^2 > 16", "S": "x^2 > 9"}
P = lambda x: x > 5
Q = lambda x: x > 4
R = lambda x: x**2 > 16
S = lambda x: x**2 > 9
B = (-5, -4, -3, 0, 3, 4, 5)
assert implies(P, Q, B)
assert implies(Q, lambda x: x**2 > 4 * x, B) and implies(Q, lambda x: 4 * x > 16, B)
assert implies(Q, R, B)
assert implies(R, S, B)
assert implies(P, S, B)
print("exr-proving-an-implication-c3: checks")
