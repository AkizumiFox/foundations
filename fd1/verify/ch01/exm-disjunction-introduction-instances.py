"""exm-disjunction-introduction-instances (Ch 1, Section 1.5), with the Quick check and the
Not-allowed block after the rule card: each gallery row is an instance of a schema of or-I
(the new line is the cited line or-ed with psi, on the stated side); the look-alike
P or (Q or R) from P or Q is no instance of either schema; Quick check: from Q, or-I may write
Q or (P and R), (P and R) or Q, Q or Q, and not Q and Q."""
from _s06s07_logic import V, Not, And, Or, Imp

P, Q, R, S = V("P"), V("Q"), V("R"), V("S")


def instances(cited):
    """Is `new` written by or-I from `cited`? (either schema, any psi)"""
    def ok(new):
        return new[0] == "or" and (new[1] == cited or new[2] == cited)
    return ok


ROWS = [  # (schema, phi, psi, cited, new)
    ("first", Imp(P, Q), And(R, Not(S)), Imp(P, Q), Or(Imp(P, Q), And(R, Not(S)))),
    ("second", Or(P, Q), And(P, Not(R)), Or(P, Q), Or(And(P, Not(R)), Or(P, Q))),
    ("second", Imp(And(P, Q), R), Not(R), Imp(And(P, Q), R), Or(Not(R), Imp(And(P, Q), R))),
]
QUOTED = {"rows": len(ROWS)}
for schema, phi, psi, cited, new in ROWS:
    assert cited == phi
    assert new == (Or(phi, psi) if schema == "first" else Or(psi, phi))
    assert phi[0] != "var" and psi[0] != "var"   # compound substitutions
# look-alike
assert not instances(Or(P, Q))(Or(P, Or(Q, R)))
assert instances(Or(P, Q))(Or(Or(P, Q), R)) and instances(Or(P, Q))(Or(R, Or(P, Q)))
# Quick check
ok = instances(Q)
assert ok(Or(Q, And(P, R))) and ok(Or(And(P, R), Q)) and ok(Or(Q, Q)) and not ok(And(Q, Q))
# Not-allowed block: none of the five is an instance
assert not instances(Or(P, Q))(P)
assert not instances(P)(And(P, Q))
assert not instances(Or(P, Q))(Or(Q, P))
print("exm-disjunction-introduction-instances: all quoted values check")
