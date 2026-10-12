"""exr-disjunction-and-cases-b6 (Ch 1, Section 1.6): (a) the parity facts behind the premises
(every integer even or odd; n even => n(n+1) even; n odd => n+1 even; n+1 even => n(n+1) even)
for |n| <= 100, and the sequent is valid; (b) the form P -> R, Q -> R, R |- P or Q is invalid,
broken at x = 1/2 with R: x != 0 (both implications true on the grid); with the argument's own
content, x^2 > 1 implies x > 1 or x < -1 on the grid; the repaired sequent is valid."""
from fractions import Fraction
from _grid import grid
from _s06s07_logic import V, Or, Imp, classically_valid

QUOTED = {"(b) witness": Fraction(1, 2)}
for n in range(-100, 101):
    E, O, F, M = n % 2 == 0, n % 2 != 0, (n + 1) % 2 == 0, n * (n + 1) % 2 == 0
    assert E or O
    assert (not E or M) and (not O or F) and (not F or M) and M
E, O, F, M = V("E"), V("O"), V("F"), V("M")
assert classically_valid([Or(E, O), Imp(E, M), Imp(O, F), Imp(F, M)], M)
P, Q, R = V("P"), V("Q"), V("R")
assert not classically_valid([Imp(P, R), Imp(Q, R), R], Or(P, Q))
assert classically_valid([Imp(R, Or(P, Q)), R], Or(P, Q))
for t in grid():
    assert (not t > 1) or t != 0
    assert (not t < -1) or t != 0
    assert (not t * t > 1) or (t > 1 or t < -1)
    assert (not t > 1) or t * t > 1
    assert (not t < -1) or t * t > 1
x = QUOTED["(b) witness"]
assert x != 0 and not (x > 1 or x < -1)
print("exr-disjunction-and-cases-b6: all quoted values check")
