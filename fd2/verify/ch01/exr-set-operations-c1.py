"""exr-set-operations-c1: power-set identities by brute force on a 3-element universe."""
from itertools import combinations, product
QUOTED = {}
U = [1, 2, 3]
subs = [frozenset(c) for k in range(4) for c in combinations(U, k)]
def P(s):
    s = sorted(s)
    return {frozenset(c) for k in range(len(s) + 1) for c in combinations(s, k)}
for A, B in product(subs, repeat=2):
    assert P(A - B) != P(A) - P(B)
    assert frozenset() in P(A - B) and frozenset() not in P(A) - P(B)
    assert all(S in P(A) - P(B) for S in P(A - B) if S)
    assert P(A) | P(B) <= P(A | B)
    assert (P(A) | P(B) == P(A | B)) == (A <= B or B <= A)
A, B = frozenset({1}), frozenset({2})
assert frozenset({1, 2}) in P(A | B) and frozenset({1, 2}) not in P(A) | P(B)
print("exr-set-operations-c1: all quoted values check")
