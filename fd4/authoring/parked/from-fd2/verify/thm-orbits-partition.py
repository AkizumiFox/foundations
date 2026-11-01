"""thm-orbits-partition quick check: orbits of (1 2 3 4 5 / 3 5 1 2 4) are {1,3}, {2,5,4}."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits

QUOTED = {"orbits": [[1, 3], [2, 5, 4]]}
sigma = dict(zip([1, 2, 3, 4, 5], [3, 5, 1, 2, 4]))
assert orbits(sigma, [1, 2, 3, 4, 5]) == QUOTED["orbits"]
assert all(sigma[x] != x for x in sigma)
print("thm-orbits-partition: all quoted values check")
