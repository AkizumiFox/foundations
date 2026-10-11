"""exm-cnf-validity-glance (Section 3.7): (a) is a tautology (a table would need 16 rows); (b) is
false in the row s = T, r = T, q = F."""
from _s0607_lib import tautology, parse, value
QUOTED = {"rows": 16}
a = ("(\\neg p \\vee q \\vee p) \\wedge (r \\vee \\neg q \\vee s \\vee q) \\wedge (\\neg s \\vee \\neg r \\vee s)"
     " \\wedge (p \\vee \\neg r \\vee r \\vee q)")
b = a.replace("(\\neg s \\vee \\neg r \\vee s)", "(\\neg s \\vee \\neg r \\vee q)")
assert tautology(a) and not tautology(b) and 2 ** 4 == 16
for pv in (True, False):
    assert value(parse(b), {"P": pv, "Q": False, "R": True, "S": True}) is False
print("exm-cnf-validity-glance: all quoted values check")
