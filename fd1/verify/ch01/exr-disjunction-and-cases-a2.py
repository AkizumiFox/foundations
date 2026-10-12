"""exr-disjunction-and-cases-a2 (Section 1.6 drill, fifteen parts): (a) |x|^2 = x^2 in each case
of x >= 0 or x < 0; (i) n = 0 lies in neither n > 0 nor n < 0; (j) at x = 0 the split
(x >= 1) or (x <= -1) fails and x^2 >= 1 fails; the derivation parts and (d)-(f) are valid."""
from _grid import grid
from _s06s07_logic import V, And, Or, Imp, classically_valid

QUOTED = {"(i) n": 0, "(j) x": 0}
for x in grid():
    assert x >= 0 or x < 0
    assert abs(x) ** 2 == x ** 2 and (-x) ** 2 == x ** 2
n = QUOTED["(i) n"]
assert not (n > 0 or n < 0)
x = QUOTED["(j) x"]
assert not (x >= 1 or x <= -1) and not x ** 2 >= 1
assert all(t ** 2 >= 1 for t in grid() if t >= 1 or t <= -1)
P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
for prem, concl in [
    ([Or(P, Q)], Or(Q, Or(P, R))),                              # (l)
    ([Or(And(P, Q), And(P, R))], P),                            # (m)
    ([Or(P, Q), Imp(Q, P)], P),                                 # (n)
    ([Or(And(P, Q), And(R, S))], Or(Q, R)),                     # (o)
    ([Or(P, And(Q, R)), Imp(P, S), Imp(R, S)], S),              # (f)
]:
    assert classically_valid(prem, concl)
print("exr-disjunction-and-cases-a2: checks")
