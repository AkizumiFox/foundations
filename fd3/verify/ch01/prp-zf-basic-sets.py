"""prp-zf-basic-sets (Section 9.1): part (d), {a, b} = {c, d} iff (a = c and b = d) or
(a = d and b = c), and its special case {a} = {c, d} iff a = c = d, checked exhaustively
on the 16 hereditarily finite sets of rank at most 3; also the independence of the
intersection from the chosen member A_0, on all non-empty sets of such sets of size <= 3."""
from itertools import combinations, product

E = frozenset()


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


V = [E]
for _ in range(3):
    V = power(V)
assert len(V) == 16

QUOTED = {}  # no numeric value is quoted in the text; the checks below are exhaustive
assert len(V) == 16

for a, b, c, d in product(V, repeat=4):
    lhs = frozenset({a, b}) == frozenset({c, d})
    rhs = (a == c and b == d) or (a == d and b == c)
    assert lhs == rhs
    single = frozenset({a}) == frozenset({c, d})
    assert single == (a == c and c == d)

for k in (1, 2, 3):
    for F in combinations(V, k):
        results = {frozenset(x for x in A0 if all(x in S for S in F)) for A0 in F}
        assert len(results) == 1
print("prp-zf-basic-sets: part (d) and the intersection check")
