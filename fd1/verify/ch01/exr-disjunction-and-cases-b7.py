"""exr-disjunction-and-cases-b7 (Ch 1, Section 1.6): all fifteen sequents are valid by truth
table (each derivation is also checked by tools/check_fitch.py)."""
from _s06s07_logic import V, And, Or, Imp, classically_valid

P, Q, R, S, T = V("P"), V("Q"), V("R"), V("S"), V("T")
SEQUENTS = {
    1: ([Q], Imp(Imp(P, R), Imp(P, And(Q, R)))),
    2: ([], Imp(And(P, Q), Imp(Imp(Q, R), And(R, P)))),
    3: ([Imp(Or(P, Q), R)], Imp(P, Imp(S, And(R, P)))),
    4: ([Imp(P, Imp(Q, R))], Imp(And(S, P), Imp(Q, Or(R, S)))),
    5: ([Imp(Q, R)], Imp(P, Imp(Imp(P, Q), And(R, P)))),
    6: ([Imp(P, And(Q, R))], Imp(And(P, S), And(R, S))),
    7: ([And(P, Imp(Q, R)), Imp(P, Q)], And(R, P)),
    8: ([Imp(And(P, Q), R), Imp(P, Q)], Imp(P, R)),
    9: ([Imp(P, Imp(Q, R)), Imp(S, Q)], Imp(And(P, S), R)),
    10: ([Imp(Imp(And(P, Q), R), S), Imp(P, T), Imp(And(T, Q), R)], S),
    11: ([Or(Imp(P, Q), And(Q, R)), P], Q),
    12: ([Or(Imp(P, R), Imp(Q, R))], Imp(And(P, Q), R)),
    13: ([Or(Imp(P, Q), Imp(P, R))], Imp(P, Or(Q, R))),
    14: ([Or(P, Q), Imp(S, Imp(Q, R))], Or(Imp(S, And(P, S)), Imp(S, R))),
    15: ([Or(P, And(Q, R)), Imp(P, And(R, S))], And(R, Or(S, Q))),
}
QUOTED = {"count": 15}
assert len(SEQUENTS) == QUOTED["count"]
for k, (prem, concl) in SEQUENTS.items():
    assert classically_valid(prem, concl), k
print("exr-disjunction-and-cases-b7: all fifteen sequents valid")
