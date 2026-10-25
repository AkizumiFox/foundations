"""Section 6.1, B3: A = {1, 2}, B = {b}. Relations G in A x B with each element of A and of B in at
most one pair: {}, {(1,b)}, {(2,b)}; maximal: {(1,b)}, {(2,b)}; each pairs all of B, none all of A.
Also B4 (c) on a finite window: in the subsets of {0..9} with no two consecutive numbers, the evens
and the odds are both maximal, and no element is greatest."""
from itertools import combinations

A, B = [1, 2], ["b"]
QUOTED = {"P": {frozenset(), frozenset({(1, "b")}), frozenset({(2, "b")})},
          "maximal": {frozenset({(1, "b")}), frozenset({(2, "b")})}}
pairs = [(a, b) for a in A for b in B]
ok = lambda G: all(p[0] != q[0] and p[1] != q[1] for p, q in combinations(G, 2))
P = {frozenset(G) for r in range(len(pairs) + 1) for G in combinations(pairs, r) if ok(G)}
assert P == QUOTED["P"]
maximal = {M for M in P if not any(M < G for G in P)}
assert maximal == QUOTED["maximal"]
for M in maximal:
    assert {b for _, b in M} == set(B) and {a for a, _ in M} != set(A)
# B4 (c), window {0, ..., 9}
N = list(range(10))
noncons = lambda S: all(abs(x - y) != 1 for x, y in combinations(S, 2))
Q = [frozenset(c) for r in range(len(N) + 1) for c in combinations(N, r) if noncons(c)]
E, O = frozenset(range(0, 10, 2)), frozenset(range(1, 10, 2))
assert E in Q and O in Q
assert not any(E < S for S in Q) and not any(O < S for S in Q)
assert not any(all(S <= g for S in Q) for g in Q)
print("exr-chains-and-zorn-b3: all quoted values check")
