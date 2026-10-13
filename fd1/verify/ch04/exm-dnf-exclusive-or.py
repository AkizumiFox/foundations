"""exm-dnf-exclusive-or (Section 3.7): (p and not q) or (not p and q) is T exactly in rows TF, FT."""
from _s0607_lib import truth_rows
QUOTED = {}
assert truth_rows("(p \\wedge \\neg q) \\vee (\\neg p \\wedge q)", "PQ") == [False, True, True, False]
print("exm-dnf-exclusive-or: all quoted values check")
