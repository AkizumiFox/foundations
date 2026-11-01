"""Quick check after cor-permutation-power-identity: [a] -> [5a] on Z/12."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits, compose

QUOTED = {"cycles": [[1, 5], [2, 10], [4, 8], [7, 11]], "fixed": [0, 3, 6, 9]}
f = {a: (5 * a) % 12 for a in range(12)}
assert 25 % 12 == 1 and compose(f, f) == {a: a for a in range(12)}
orbs = orbits(f, range(12))
assert [o for o in orbs if len(o) > 1] == QUOTED["cycles"]
assert [o[0] for o in orbs if len(o) == 1] == QUOTED["fixed"]
assert 15 % 12 == 3 and 30 % 12 == 6 and 45 % 12 == 9 and 20 % 12 == 8 and 40 % 12 == 4
assert 35 % 12 == 11 and 55 % 12 == 7 and 50 % 12 == 2
print("thm-permutation-cycles: all quoted values check")
