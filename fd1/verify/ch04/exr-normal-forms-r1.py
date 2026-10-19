"""exr-normal-forms-r1 (moved to Section 4.8, 08-completeness.md): the sequent is valid; the derivation has 9 lines, no RAA."""
from _s0607_lib import S06, block, entails, count_lines
QUOTED = {}
assert entails(["p \\vee q", "\\neg(p \\wedge r)", "r"], "q")
t = block(S06, "exr-normal-forms-r1")
assert count_lines(t) == 9 and "\\raa" not in t
print("exr-normal-forms-r1: all quoted values check")
