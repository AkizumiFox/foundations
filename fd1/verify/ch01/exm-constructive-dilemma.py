"""exm-constructive-dilemma (Ch 1, Section 1.6): the sequent (P -> R) and (Q -> S), P or Q |- R or S
is valid; the reading: x >= 1 gives x^3 >= 1 and x <= -1 gives x^3 <= -1, so every x with
x >= 1 or x <= -1 has x^3 >= 1 or x^3 <= -1."""
from _grid import grid
from _s06s07_logic import V, And, Or, Imp, classically_valid

QUOTED = {"bounds": (1, -1)}
P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
assert classically_valid([And(Imp(P, R), Imp(Q, S)), Or(P, Q)], Or(R, S))
assert classically_valid([Or(P, Q), Imp(P, R), Imp(Q, R)], R)   # the skeleton, R = S
hi, lo = QUOTED["bounds"]
for x in grid():
    if x >= hi:
        assert x ** 3 >= hi
    if x <= lo:
        assert x ** 3 <= lo
    if x >= hi or x <= lo:
        assert x ** 3 >= hi or x ** 3 <= lo
print("exm-constructive-dilemma: all quoted values check")
