"""exr-completeness-b2 (Section 3.6): p, p -> q |= q; the method's derivation has 21 lines with
one correct row citation; the direct derivation has 3 lines."""
from _s0607_lib import S06, block, entails, check_rows_in, count_lines
QUOTED = {"lines": 21, "direct": 3}
t = block(S06, "exr-completeness-b2")
assert entails(["p", "p \\to q"], "q")
assert count_lines(t) == 21
assert check_rows_in(t) == 1
print("exr-completeness-b2: all quoted values check")
