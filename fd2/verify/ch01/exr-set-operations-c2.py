"""exr-set-operations-c2: counterexample to the illegal step, and the true conclusion."""
from itertools import combinations, product
QUOTED = {}
A, B, C, x = {1}, {1}, set(), 1
assert x in B and x in (A | C) and x not in C and x in (A | (B & C))
U = [1, 2, 3]
subs = [frozenset(c) for k in range(4) for c in combinations(U, k)]
assert all((A | B) & (A | C) <= A | (B & C) for A, B, C in product(subs, repeat=3))
print("exr-set-operations-c2: all quoted values check")
