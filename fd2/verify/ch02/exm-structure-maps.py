"""exm-structure-maps (a)-(d) and the projection Quick check (F2.6 §02):
brute force over sets of sizes 0..3."""
import sys
sys.path.insert(0, "verify/ch01")
from _sets import subsets, prod, injective, surjective

QUOTED = {"c o c": "id"}

sets = [frozenset(range(n)) for n in range(4)]
for X in sets:
    # (a) inclusion
    for A in subsets(X):
        inc = {a: a for a in A}
        assert injective(inc)
        assert surjective(inc, X) == (A == X)
    # (c) diagonal
    d = {x: (x, x) for x in X}
    assert injective(d)
    assert surjective(d, prod(X, X)) == (len(X) <= 1)
    # (d) complement
    P = subsets(X)
    c = {S: X - S for S in P}
    assert all(c[c[S]] == S for S in P)   # c o c = id
    assert injective(c) and surjective(c, P)
    for Y in [frozenset(range(10, 10 + m)) for m in range(4)]:
        XY = prod(X, Y)
        p1 = {pq: pq[0] for pq in XY}
        p2 = {pq: pq[1] for pq in XY}
        # (b) and its mirror image
        assert surjective(p1, X) == (len(Y) > 0 or len(X) == 0)
        assert surjective(p2, Y) == (len(X) > 0 or len(Y) == 0)
        # Quick check
        assert injective(p1) == (len(X) == 0 or len(Y) <= 1)
print("exm-structure-maps: all statements check")
