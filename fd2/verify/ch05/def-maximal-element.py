"""Quick check in Section 7.6: in P({1,2,3}) minus {1,2,3}, under inclusion, the maximal elements
are the three two-element sets and there is no greatest element."""
from itertools import combinations

QUOTED = {"maximal": {frozenset(s) for s in ({1, 2}, {1, 3}, {2, 3})}}

U = {1, 2, 3}
P = [frozenset(c) for r in range(4) for c in combinations(sorted(U), r) if r < 3]
mx = {m for m in P if not any(m < a for a in P)}
gr = {g for g in P if all(a <= g for a in P)}
assert mx == QUOTED["maximal"] and not gr
print("def-maximal-element: all quoted values check")
