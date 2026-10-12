"""exm-disjunction-and-cases-instances (Ch 1, Section 1.6): each gallery row is an instance of
or-E (the boxes open with the two sides of the cited disjunction and end in one common line,
which is the new line), every substitution is compound, and each box is a correct derivation
of its last line from its assumption (valid by truth table); the look-alike's cited line is a
conjunction, not a disjunction."""
from _s06s07_logic import V, And, Or, Imp, classically_valid

P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
ROWS = [  # (disjunction, first box (asm, last), second box (asm, last), new line)
    (Or(And(P, Q), And(P, R)), (And(P, Q), Or(P, S)), (And(P, R), Or(P, S)), Or(P, S)),
    (Or(Imp(P, Q), And(R, S)), (Imp(P, Q), Or(And(R, S), Imp(P, Q))),
     (And(R, S), Or(And(R, S), Imp(P, Q))), Or(And(R, S), Imp(P, Q))),
    (Or(Or(P, Q), And(Q, S)), (Or(P, Q), Or(P, Q)), (And(Q, S), Or(P, Q)), Or(P, Q)),
]
QUOTED = {"rows": len(ROWS)}
for d, (a1, l1), (a2, l2), new in ROWS:
    assert d[0] == "or" and d[1] == a1 and d[2] == a2
    assert l1 == l2 == new
    assert a1[0] != "var" and a2[0] != "var" and new[0] != "var"
    assert classically_valid([a1], l1) and classically_valid([a2], l2)
assert And(Or(P, Q), R)[0] == "and"
print("exm-disjunction-and-cases-instances: all quoted values check")
