"""exr-normal-forms-b2 (Section 3.7): the {not, and} forms of p or q and p <-> q."""
from _s0607_lib import equivalent, truth_rows
QUOTED = {}
assert equivalent("p \\vee q", "\\neg(\\neg p \\wedge \\neg q)")
x = "\\neg(p \\wedge \\neg q) \\wedge \\neg(\\neg p \\wedge q)"
assert equivalent("p \\leftrightarrow q", x)
assert truth_rows(x, "PQ") == [True, False, False, True]
print("exr-normal-forms-b2: all quoted values check")
