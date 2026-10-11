"""exr-set-operations-b3: A = {1}, B = empty, C = {1}; and the characterization, by brute force."""
from itertools import combinations, product
QUOTED = {}
A, B, C = {1}, set(), {1}
assert A | B == A | C and B != C
U = [1, 2, 3]
subs = [frozenset(c) for k in range(4) for c in combinations(U, k)]
for A, B, C in product(subs, repeat=3):
    odd = (B - C) | (C - B)
    assert (A | B == A | C) == (odd <= A)
    assert (B != C) == (len(odd) > 0)
print("exr-set-operations-b3: all quoted values check")
