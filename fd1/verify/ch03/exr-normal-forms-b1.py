"""exr-normal-forms-b1 (Section 3.7): the DNFs and CNFs given are equivalent to the formulas."""
from _s0607_lib import equivalent
QUOTED = {}
pairs = [("p \\leftrightarrow \\neg q", "(p \\wedge \\neg q) \\vee (\\neg p \\wedge q)"),
         ("p \\leftrightarrow \\neg q", "(\\neg p \\vee \\neg q) \\wedge (p \\vee q)"),
         ("(p \\wedge q) \\to r", "\\neg p \\vee \\neg q \\vee r"),
         ("\\neg(p \\vee (q \\to r))", "\\neg p \\wedge q \\wedge \\neg r")]
for a, b in pairs:
    assert equivalent(a, b), (a, b)
print("exr-normal-forms-b1: all quoted values check")
