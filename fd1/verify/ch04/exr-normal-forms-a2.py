"""exr-normal-forms-a2 (Section 4.9): the twelve drill answers."""
from _logic import parse, val, rows, equivalent
assert equivalent("p \\wedge (p \\vee q)", "p")                                  # (a)
assert equivalent("\\neg(p \\to q)", "p \\wedge \\neg q")                        # (b)
assert equivalent("\\neg(p \\to q)", "\\neg(\\neg p \\vee q)")
assert equivalent("\\neg(\\neg p \\vee q)", "\\neg\\neg p \\wedge \\neg q")
assert equivalent("(p \\vee q) \\wedge \\neg p", "\\neg p \\wedge q")            # (c)
assert equivalent("(p \\vee q) \\wedge \\neg p", "(p \\wedge \\neg p) \\vee (q \\wedge \\neg p)")
assert equivalent("(p \\wedge q) \\vee (p \\wedge \\neg q)", "p")                # (d)
assert equivalent("(p \\wedge q) \\vee (p \\wedge \\neg q)", "p \\wedge (q \\vee \\neg q)")
# (e)-(h): signs and monotonicity are checked in thm-monotonicity.py
assert equivalent("p \\leftrightarrow q", "(p \\wedge q) \\vee (\\neg p \\wedge \\neg q)")   # (i)
assert equivalent("p \\leftrightarrow q", "(\\neg p \\vee q) \\wedge (p \\vee \\neg q)")     # (j)
assert sum(1 for _ in rows("pqr")) == 8                                          # (k)
assert equivalent("p \\vee q", "\\neg p \\to q")                                 # (l)
print("exr-normal-forms-a2: all quoted values check")
