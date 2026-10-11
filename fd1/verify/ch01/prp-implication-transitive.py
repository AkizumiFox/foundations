"""The instance after prp-implication-transitive (Section 1.5): P: x > 3, Q: x^2 > 9, R: x^2 > 4."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies

QUOTED = {"P": "x > 3", "Q": "x^2 > 9", "R": "x^2 > 4"}
P = lambda x: x > 3
Q = lambda x: x**2 > 9
R = lambda x: x**2 > 4
B = (-3, -2, 0, 2, 3)
assert implies(P, Q, B)                                   # x > 3 gives x^2 > 3x > 9
assert implies(P, lambda x: x**2 > 3 * x, B) and implies(P, lambda x: 3 * x > 9, B)
assert implies(Q, R, B)                                   # since 4 < 9
assert implies(P, R, B)
print("prp-implication-transitive: checks")
