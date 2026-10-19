"""exr-normal-forms-r3 (moved to Section 4.8, 08-completeness.md): the formula is a tautology; the derivation has 10 lines, no RAA."""
from _s0607_lib import S06, block, tautology, count_lines
QUOTED = {}
assert tautology("(p \\wedge (q \\vee r)) \\to ((p \\wedge q) \\vee r)")
t = block(S06, "exr-normal-forms-r3")
assert count_lines(t) == 10 and "\\raa" not in t
print("exr-normal-forms-r3: all quoted values check")
