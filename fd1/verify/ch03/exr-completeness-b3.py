"""exr-completeness-b3 (Section 3.6): not(p <-> q) |= not p <-> q; the table; 12 lines with rows
cited; 22 lines in primitive rules (the rows' derivations have 9 and 7 lines, with 2 premises
each, replacing one line each)."""
from _s0607_lib import S06, block, entails, check_rows_in, count_lines, truth_rows
QUOTED = {"lines": 12, "primitive": 22}
t = block(S06, "exr-completeness-b3")
assert entails(["\\neg (p \\leftrightarrow q)"], "\\neg p \\leftrightarrow q")
assert truth_rows("\\neg (p \\leftrightarrow q)", "PQ") == [False, True, True, False]
assert truth_rows("\\neg p \\leftrightarrow q", "PQ") == [False, True, True, False]
assert count_lines(t) == 12
assert check_rows_in(t) == 2
assert 12 + (9 - 2 - 1) + (7 - 2 - 1) == 22
print("exr-completeness-b3: all quoted values check")
