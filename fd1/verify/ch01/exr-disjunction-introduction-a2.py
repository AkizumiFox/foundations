"""exr-disjunction-introduction-a2 (Section 1.5 drill, fifteen parts): (d) from x = 5 the lines
(i), (ii) and x >= 5 written out are true; (j) premise x < -1 gives x < 0, and x = -2 breaks
x < -5; (i) 4 = 2 * 2; the derivation parts (k)-(o) and (h)'s target are valid sequents."""
from _grid import grid
from fractions import Fraction as F
from _s06s07_logic import V, And, Or, Imp, classically_valid

QUOTED = {"(j) witness": -2, "(i) n": 4}
x = F(5)
assert (x == 5 or x == 6) and (x > 4 or x == 5) and (x > 5 or x == 5)
assert all((t >= 5) == (t > 5 or t == 5) for t in grid())
assert all((not t < -1) or t < 0 for t in grid())
x = QUOTED["(j) witness"]
assert x < -1 and not x < -5
n = QUOTED["(i) n"]
assert n == 2 * 2 and n % 2 == 0
P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
for prem, concl in [
    ([And(P, Q), R], Or(S, And(Or(Q, R), R))),                 # (c)
    ([And(P, Q)], And(Or(P, R), Q)),                           # (h), in four lines
    ([P], And(Or(P, Q), Or(R, P))),                            # (k)
    ([And(P, Q)], Or(Q, R)),                                   # (l)
    ([Imp(P, Q)], Imp(P, Or(R, Q))),                           # (m)
    ([Imp(Or(P, Q), R), Q], R),                                # (n)
    ([Imp(P, And(Q, R))], Imp(P, Or(S, R))),                   # (o)
]:
    assert classically_valid(prem, concl)
print("exr-disjunction-introduction-a2: checks")
