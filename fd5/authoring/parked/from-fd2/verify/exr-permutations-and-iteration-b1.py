"""exr-permutations-and-iteration-b1: doubling on Z/9; inverse [5a]; cycles; N = 6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits, compose, least_identity_power

QUOTED = {"cycles": [[1, 2, 4, 8, 7, 5], [3, 6]], "fixed": [0], "N": 6}
d = {a: (2 * a) % 9 for a in range(9)}
e = {a: (5 * a) % 9 for a in range(9)}
assert 10 % 9 == 1 and compose(e, d) == compose(d, e) == {a: a for a in range(9)}
orbs = orbits(d, range(9))
assert [o for o in orbs if len(o) > 1] == QUOTED["cycles"]
assert [o[0] for o in orbs if len(o) == 1] == QUOTED["fixed"]
assert 16 % 9 == 7 and 14 % 9 == 5 and 12 % 9 == 3
assert least_identity_power(d) == QUOTED["N"]
print("exr-permutations-and-iteration-b1: all quoted values check")
