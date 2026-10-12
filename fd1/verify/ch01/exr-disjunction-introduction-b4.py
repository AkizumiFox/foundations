"""exr-disjunction-introduction-b4 (Ch 1, Section 1.5): derive or break. Each verdict by truth
table (derive: valid; break: invalid), and each break at its stated number makes the
counterexample set true; for (c) and (g) the premise holds at every grid point."""
from fractions import Fraction
from _grid import grid
from _s06s07_logic import V, And, Or, Imp, classically_valid

P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
CLAIMS = {
    "a": ([P], Or(P, And(Q, R)), "derive"),
    "b": ([P], And(P, Or(Q, R)), "break"),
    "c": ([Imp(P, R)], Imp(Or(P, Q), R), "break"),
    "d": ([Imp(Or(P, Q), R)], Imp(P, R), "derive"),
    "e": ([Imp(And(P, Q), R)], Imp(And(Q, P), Or(R, S)), "derive"),
    "f": ([And(Imp(P, Q), Imp(P, R))], Imp(P, Or(Q, R)), "derive"),
    "g": ([Imp(P, Or(Q, R))], Imp(P, Q), "break"),
}
QUOTED = {"b": 1, "c": -1, "g": 1}
for k, (prem, concl, verdict) in CLAIMS.items():
    assert classically_valid(prem, concl) == (verdict == "derive"), k

imp = lambda a, b: (not a) or b
# (b) P: x > 0, Q: x > 5, R: x < -5 at x = 1
x = Fraction(QUOTED["b"])
assert x > 0 and not (x > 5 or x < -5)
# (c) P: x > 3, Q: x < 0, R: x > 1; P -> R everywhere; at -1: P or Q true, R false
assert all(imp(t > 3, t > 1) for t in grid())
x = Fraction(QUOTED["c"])
assert (x > 3 or x < 0) and not x > 1
# (g) P: x > 0, Q: x > 5, R: x < 6; premise everywhere; at 1: P true, Q false
assert all(imp(t > 0, t > 5 or t < 6) for t in grid())
x = Fraction(QUOTED["g"])
assert x > 0 and not x > 5
print("exr-disjunction-introduction-b4: all verdicts and witnesses check")
