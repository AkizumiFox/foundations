"""exm-right-inverses-finite (Ch 6, Section 6.5): parity map q: {1,2,3,4} -> {0,1}."""
from itertools import product
QUOTED = {"number of right inverses": 4,
          "the list (k(0), k(1))": [(2, 1), (2, 3), (4, 1), (4, 3)]}
q = {1: 1, 2: 0, 3: 1, 4: 0}
rights = sorted((k0, k1) for k0, k1 in product([1, 2, 3, 4], repeat=2)
                if q[k0] == 0 and q[k1] == 1)
assert len(rights) == QUOTED["number of right inverses"]
assert rights == QUOTED["the list (k(0), k(1))"]
print("exm-right-inverses-finite: all quoted values check")
