"""6.2 B2: (a) the size-ordered list of P({1,2,3}) respects proper inclusion;
(b) exactly two total orders on P({1,2}) contain inclusion."""
from itertools import permutations

L = [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
assert all(i < j for i, A in enumerate(L) for j, B in enumerate(L) if A < B)
S2 = [frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})]
good = [p for p in permutations(S2)
        if all(p.index(A) < p.index(B) for A in S2 for B in S2 if A < B)]
assert len(good) == 2
print("exr-using-zorn-b2: ok")
