"""prp-indicator-arithmetic: the four-row table (a), (b), (d) and (c), (e) checked against
membership on all subsets of a small set; the quick checks after it: ind_{A minus B} = u - uv,
and ind_{A triangle B} on X = {1,2,3,4}, A = {1,2}, B = {2,3} is (1,0,1,0)."""
from itertools import combinations

QUOTED = {
    "table_uv": [1, 0, 0, 0],          # rows (1,1),(1,0),(0,1),(0,0)
    "table_1_minus_u": [0, 0, 1, 1],
    "table_sym": [0, 1, 1, 0],
    "qc_sym_values": (1, 0, 1, 0),
    "qc_ind_A": (1, 1, 0, 0),
    "qc_ind_B": (0, 1, 1, 0),
}
rows = [(1, 1), (1, 0), (0, 1), (0, 0)]
assert [u * v for u, v in rows] == QUOTED["table_uv"]
assert [1 - u for u, v in rows] == QUOTED["table_1_minus_u"]
assert [u + v - 2 * u * v for u, v in rows] == QUOTED["table_sym"]

X = frozenset(range(4))
subs = [frozenset(c) for r in range(5) for c in combinations(sorted(X), r)]
ind = lambda S, x: 1 if x in S else 0
for A in subs:
    for B in subs:
        incl = A <= B
        pointwise = all(ind(A, x) <= ind(B, x) for x in X)
        assert incl == pointwise
        for x in X:
            u, v = ind(A, x), ind(B, x)
            assert ind(A & B, x) == u * v
            assert ind(X - A, x) == 1 - u
            assert ind(A | B, x) == u + v - u * v == 1 - (1 - u) * (1 - v)
            assert ind(A ^ B, x) == u + v - 2 * u * v
            assert ind(A - B, x) == u * (1 - v) == u - u * v

Xq, A, B = (1, 2, 3, 4), {1, 2}, {2, 3}
iA = tuple(ind(A, x) for x in Xq); iB = tuple(ind(B, x) for x in Xq)
assert iA == QUOTED["qc_ind_A"] and iB == QUOTED["qc_ind_B"]
assert tuple(u + v - 2 * u * v for u, v in zip(iA, iB)) == QUOTED["qc_sym_values"]
assert tuple(ind(A ^ B, x) for x in Xq) == QUOTED["qc_sym_values"] and A ^ B == {1, 3}
print("prp-indicator-arithmetic: all quoted values check")
