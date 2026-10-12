"""exr-disjunction-and-cases-b5 (Ch 1, Section 1.6): derive or break. Each verdict by truth
table, and each break at its stated number makes the counterexample set true."""
from fractions import Fraction
from _s06s07_logic import V, And, Or, Imp, classically_valid

P, Q, R = V("P"), V("Q"), V("R")
CLAIMS = {
    "a": ([Or(P, Q), R], Or(And(P, R), Q), "derive"),
    "b": ([And(Or(P, Q), Or(P, R))], And(P, Or(Q, R)), "break"),
    "c": ([Or(P, Or(Q, R)), Imp(Q, P)], Or(P, R), "derive"),
    "d": ([Imp(Or(P, Q), R)], Or(Imp(P, R), Imp(Q, R)), "derive"),
    "e": ([Or(Imp(P, R), Imp(Q, R))], Imp(Or(P, Q), R), "break"),
    "f": ([Or(P, Q), Imp(P, R)], Or(R, Q), "derive"),
    "g": ([Or(P, Imp(Q, R)), Q], Or(P, R), "derive"),
    "h": ([Or(P, Imp(Q, R))], Imp(Or(P, Q), Or(P, R)), "derive"),
    "i": ([Imp(Or(P, Q), Or(P, R))], Imp(Q, R), "break"),
}
QUOTED = {"b": 1, "e": 1, "i": 2}
for k, (prem, concl, verdict) in CLAIMS.items():
    assert classically_valid(prem, concl) == (verdict == "derive"), k

imp = lambda a, b: (not a) or b
x = Fraction(QUOTED["b"])                   # P: x > 5, Q: x > 0, R: x < 10
p, q, r = x > 5, x > 0, x < 10
assert (p or q) and (p or r) and not (p and (q or r))
x = Fraction(QUOTED["e"])                   # P: x < 0, Q: x > 0, R: x > 5
p, q, r = x < 0, x > 0, x > 5
assert (imp(p, r) or imp(q, r)) and not imp(p or q, r) and imp(p, r)
x = Fraction(QUOTED["i"])                   # P: x > 0, Q: x > 1, R: x > 5
p, q, r = x > 0, x > 1, x > 5
assert (p or r) and imp(p or q, p or r) and q and not r
print("exr-disjunction-and-cases-b5: all verdicts and witnesses check")
