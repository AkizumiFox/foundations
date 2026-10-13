"""exr-normal-forms-a1 (Section 3.7): (c) the first CNF is refuted at p = q = F, the second is a
tautology; (d) p and not p is unsatisfiable."""
from _s0607_lib import tautology, parse, value, rows
QUOTED = {}
x = "(p \\vee q) \\wedge (\\neg p \\vee p \\vee r)"
assert not tautology(x)
for r in (True, False):
    assert value(parse(x), {"P": False, "Q": False, "R": r}) is False
assert tautology("(q \\vee \\neg q) \\wedge (\\neg r \\vee p \\vee r)")
assert not any(value(parse("p \\wedge \\neg p"), e) for e in rows("P"))
print("exr-normal-forms-a1: all quoted values check")
