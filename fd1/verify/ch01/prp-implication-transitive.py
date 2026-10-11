"""prp-implication-transitive (Section 1.4): the instance after the proposition
(P: x > 3, Q: x^2 > 9, R: x^2 > 4), and the section after it, "Argument B, diagnosed":
B's algebra line, the affirming-the-consequent witness x = -3, and the x^3 Quick check."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _implies import implies, grid

QUOTED = {"P": "x > 3", "Q": "x^2 > 9", "R": "x^2 > 4", "repair witness x": -3}
P = lambda x: x > 3
Q = lambda x: x**2 > 9
R = lambda x: x**2 > 4
B = (-3, -2, 0, 2, 3)
assert implies(P, Q, B)                                   # x > 3 gives x^2 > 3x > 9
assert implies(P, lambda x: x**2 > 3 * x, B) and implies(P, lambda x: 3 * x > 9, B)
assert implies(Q, R, B)                                   # since 4 < 9
assert implies(P, R, B)

# Argument B's line 2: n = 2k gives n^2 = 4k^2 = 2(2k^2), so n^2 is even
for k in range(-500, 501):
    n = 2 * k
    assert n**2 == 4 * k**2 == 2 * (2 * k**2) and (n**2) % 2 == 0

# The repair is affirming the consequent: "if x > 2 then x^2 > 4" holds for every x,
# and at x = -3 the premise x^2 > 4 holds (9 > 4) while x > 2 fails.
assert implies(lambda x: x > 2, lambda x: x**2 > 4, (-2, 2))
x0 = QUOTED["repair witness x"]
assert x0**2 == 9 and x0**2 > 4 and not x0 > 2

# Quick check: "if x^3 > 8 then x > 2" is true (cubes increase), and the box
# "suppose x > 2 ... x^3 > 8" earns the converse, which is also true.
assert implies(lambda x: x**3 > 8, lambda x: x > 2, (2,))
assert implies(lambda x: x > 2, lambda x: x**3 > 8, (2,))
# the solution's route for the claim: x <= 2 gives x^3 <= 2^3 = 8
assert implies(lambda x: x <= 2, lambda x: x**3 <= 8, (2,))
assert all((a < b) <= (a**3 < b**3) for a in grid((2,))[::40] for b in grid((2,))[::40])
print("prp-implication-transitive: checks")
