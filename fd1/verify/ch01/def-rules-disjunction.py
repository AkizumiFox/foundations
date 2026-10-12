"""def-rules-disjunction and its surroundings (Ch 1, Section 1.6): the affirming-a-disjunct
warning (n = 6 is even and a multiple of 3, so P or Q and P are true and not-Q false; the form
is invalid); the Not-allowed pair: (P and Q) or R, R -> Q |- Q is valid, while
(P and Q) or R |- Q breaks at x = -1 with P: x > 0, Q: x > 1, R: x < 0."""
from fractions import Fraction
from _s06s07_logic import V, Not, And, Or, Imp, classically_valid

QUOTED = {"affirming a disjunct n": 6, "wrong/right witness": -1}
P, Q, R = V("P"), V("Q"), V("R")
# affirming a disjunct
assert not classically_valid([Or(P, Q), P], Not(Q))
n = QUOTED["affirming a disjunct n"]
assert n % 2 == 0 and n % 3 == 0
# WRONG / RIGHT pair
assert classically_valid([Or(And(P, Q), R), Imp(R, Q)], Q)
assert not classically_valid([Or(And(P, Q), R)], Q)
x = Fraction(QUOTED["wrong/right witness"])
assert ((x > 0 and x > 1) or x < 0) and not x > 1
print("def-rules-disjunction: all quoted values check")
