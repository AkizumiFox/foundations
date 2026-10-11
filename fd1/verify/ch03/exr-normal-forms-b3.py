"""exr-normal-forms-b3 (Section 3.7): the parity DNF is T exactly in the rows with an odd number
of T's; any conjunct omitting an atom covers two rows of different parity."""
import itertools
from _s0607_lib import parse, value
QUOTED = {}
f = parse("(p \\wedge q \\wedge r) \\vee (p \\wedge \\neg q \\wedge \\neg r) \\vee (\\neg p \\wedge q \\wedge \\neg r)"
          " \\vee (\\neg p \\wedge \\neg q \\wedge r)")
for a, b, c in itertools.product([True, False], repeat=3):
    assert value(f, {"P": a, "Q": b, "R": c}) == ((a + b + c) % 2 == 1)
print("exr-normal-forms-b3: all quoted values check")
