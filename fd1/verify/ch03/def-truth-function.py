"""def-truth-function (Section 3.7): 2^(2^n) truth functions: 4 with one input, 16 with two; the
majority formula expresses majority."""
import itertools
from _s0607_lib import parse, value
QUOTED = {"one input": 4, "two inputs": 16}
assert 2 ** 2 ** 1 == 4 and 2 ** 2 ** 2 == 16
assert len(set(itertools.product([0, 1], repeat=4))) == 16
f = parse("(p \\wedge q) \\vee (p \\wedge r) \\vee (q \\wedge r)")
for a, b, c in itertools.product([True, False], repeat=3):
    assert value(f, {"P": a, "Q": b, "R": c}) == (a + b + c >= 2)
print("def-truth-function: all quoted values check")
