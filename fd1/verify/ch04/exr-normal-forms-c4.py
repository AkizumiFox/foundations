"""exr-normal-forms-c4 (Section 3.7): (p->q)->(q and r): T-rows TTT, TFT, TFF, FTT; the DNF and
both CNFs are equivalent; four conjuncts and four clauses by the table route."""
from _s0607_lib import truth_rows, equivalent
QUOTED = {"T-rows": ["TTT", "TFT", "TFF", "FTT"]}
phi = "(p \\to q) \\to (q \\wedge r)"
vals = truth_rows(phi, "PQR")
names = ["TTT", "TTF", "TFT", "TFF", "FTT", "FTF", "FFT", "FFF"]
assert [n for n, v in zip(names, vals) if v] == QUOTED["T-rows"]
for x in ["(p \\wedge \\neg q) \\vee (q \\wedge r)", "(p \\vee q) \\wedge (p \\vee r) \\wedge (\\neg q \\vee r)",
          "(p \\vee q) \\wedge (\\neg q \\vee r)",
          "(p \\vee q) \\wedge (p \\vee r) \\wedge (\\neg q \\vee q) \\wedge (\\neg q \\vee r)"]:
    assert equivalent(phi, x), x
assert sum(vals) == 4 and len(vals) - sum(vals) == 4
print("exr-normal-forms-c4: all quoted values check")
