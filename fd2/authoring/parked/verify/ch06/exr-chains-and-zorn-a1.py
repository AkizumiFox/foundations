"""Section 6.1, A1 (c): I = {1, 2}, A_1 = {0}, A_2 = {5, 6}. P (graphs G in I x U with (C1), (C2))
has six elements; the maximal ones are {(1,0),(2,5)} and {(1,0),(2,6)}; no greatest element."""
from itertools import combinations

A = {1: {0}, 2: {5, 6}}
U = set().union(*A.values())
QUOTED = {
    "U": {0, 5, 6},
    "P": {frozenset(), frozenset({(1, 0)}), frozenset({(2, 5)}), frozenset({(2, 6)}),
          frozenset({(1, 0), (2, 5)}), frozenset({(1, 0), (2, 6)})},
    "maximal": {frozenset({(1, 0), (2, 5)}), frozenset({(1, 0), (2, 6)})},
}
assert U == QUOTED["U"]
pairs = [(i, x) for i in A for x in U]
P = set()
for r in range(len(pairs) + 1):
    for G in combinations(pairs, r):
        c1 = all(x in A[i] for i, x in G)
        c2 = all(not (p[0] == q[0] and p[1] != q[1]) for p, q in combinations(G, 2))
        if c1 and c2:
            P.add(frozenset(G))
assert P == QUOTED["P"]
maximal = {M for M in P if not any(M < G for G in P)}
assert maximal == QUOTED["maximal"]
assert not any(all(G <= g for G in P) for g in P)
# each maximal element is the graph of a choice function
for M in maximal:
    assert {i for i, _ in M} == set(A) and all(x in A[i] for i, x in M)
print("exr-chains-and-zorn-a1: all quoted values check")
