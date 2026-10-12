"""exm-early-choice (Ch 1, Section 1.5): with P: x > 1, Q: x > 0, R: x^2 > x, S: x > 5, the
premise P -> R holds for every real x; at x = 2 the assumption P and Q is true, the subgoal S
is false, and the goal's right side R is true (4 > 2). The sequent itself is valid."""
from fractions import Fraction
from _grid import grid
from _s06s07_logic import V, And, Or, Imp, classically_valid

QUOTED = {"witness": 2, "R at witness": (4, 2)}

P = lambda x: x > 1
Q = lambda x: x > 0
R = lambda x: x * x > x
S = lambda x: x > 5
assert all((not P(x)) or R(x) for x in grid())          # premise true everywhere
x = Fraction(QUOTED["witness"])
assert P(x) and Q(x) and not S(x) and R(x)
assert (x * x, x) == QUOTED["R at witness"]
p, q, r, s = V("P"), V("Q"), V("R"), V("S")
assert classically_valid([Imp(p, r)], Imp(And(p, q), Or(s, r)))
assert not classically_valid([Imp(p, r), And(p, q)], s)  # the early subgoal does not follow
assert classically_valid([Imp(p, s)], Imp(And(p, q), Or(s, r)))  # Quick check variant
print("exm-early-choice: all quoted values check")
