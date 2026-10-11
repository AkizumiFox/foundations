"""exm-normal-forms-two-routes (Section 3.7): (p->q)->(not q->r) has one F-row (FFF), seven
T-rows; the seven-conjunct DNF, the three-conjunct DNF, the distributed CNF and p or q or r are
all equivalent to it."""
from _s0607_lib import truth_rows, equivalent
QUOTED = {"T-rows": 7}
phi = "(p \\to q) \\to (\\neg q \\to r)"
assert truth_rows(phi, "PQR") == [True] * 7 + [False]
dnf7 = ("(p \\wedge q \\wedge r) \\vee (p \\wedge q \\wedge \\neg r) \\vee (p \\wedge \\neg q \\wedge r)"
        " \\vee (p \\wedge \\neg q \\wedge \\neg r) \\vee (\\neg p \\wedge q \\wedge r)"
        " \\vee (\\neg p \\wedge q \\wedge \\neg r) \\vee (\\neg p \\wedge \\neg q \\wedge r)")
for x in [dnf7, "\\neg(\\neg p \\vee q) \\vee (\\neg\\neg q \\vee r)", "(\\neg\\neg p \\wedge \\neg q) \\vee (q \\vee r)",
          "(p \\wedge \\neg q) \\vee q \\vee r", "(p \\vee q \\vee r) \\wedge (\\neg q \\vee q \\vee r)", "p \\vee q \\vee r"]:
    assert equivalent(phi, x), x
print("exm-normal-forms-two-routes: all quoted values check")
