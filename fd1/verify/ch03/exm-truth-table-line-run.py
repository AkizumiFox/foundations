"""exm-truth-table-line-run (Section 3.6): phi = p -> (q and not p) is F at p = q = T; the
derivation has 5 lines and each row citation is an instance of its sequent."""
from _s0607_lib import S06, block, parse, value, check_rows_in, count_lines

QUOTED = {"lines": 5}
t = block(S06, "exm-truth-table-line-run")
assert value(parse("p \\to (q \\wedge \\neg p)"), {"P": True, "Q": True}) is False
assert count_lines(t) == QUOTED["lines"]
assert check_rows_in(t) == 3
print("exm-truth-table-line-run: all quoted values check")
