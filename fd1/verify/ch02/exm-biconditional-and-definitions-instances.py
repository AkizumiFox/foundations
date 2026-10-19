"""exm-biconditional-and-definitions-instances (Ch 2, Section 2.4), with the Not-allowed pair after
the card: P: x > 5, Q: x > 3; at x = 4 the premise P -> Q is true and P <-> Q is false.
Also: P -> Q holds for every x on a grid, so the left list's form P -> Q |- P <-> Q breaks."""
from fractions import Fraction as F

QUOTED = {"x": 4}

imp = lambda a, b: (not a) or b
x = QUOTED["x"]
P, Q = x > 5, x > 3
assert imp(P, Q) and not (P == Q)
assert all(imp(y > 5, y > 3) for y in [F(k, 8) for k in range(-80, 120)])
print("exm-biconditional-and-definitions-instances: all quoted values check")
