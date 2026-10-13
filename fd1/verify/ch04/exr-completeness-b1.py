"""exr-completeness-b1 (Section 3.6): the three primitive derivations have 5, 5 and 9 lines."""
from _s0607_lib import S06, block, derivations
QUOTED = {"lines": [5, 5, 9]}
t = block(S06, "exr-completeness-b1")
assert [len(o) for o, _ in derivations(t)] == [5, 5, 9]
assert "\\raa" not in t
print("exr-completeness-b1: all quoted values check")
