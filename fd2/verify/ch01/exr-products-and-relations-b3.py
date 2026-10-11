"""exr-products-and-relations-b3 and c1, c2: brute force over subsets of {0, 1, 2}
(Ch 6 Section 6.3)."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import subsets, prod

QUOTED = {"identities checked": True}

S = subsets({0, 1, 2})
E = frozenset()
for A in S:
    for B in S:
        # B3
        assert prod(A, B) & prod(B, A) == prod(A & B, A & B)
        # C1 (b), (c)
        U = A | B
        assert prod(A, A) | prod(B, B) <= prod(U, U)
        assert prod(U, U) == prod(A, A) | prod(A, B) | prod(B, A) | prod(B, B)
        # C2
        assert (prod(A, B) <= prod(B, A)) == (A == B or A == E or B == E)
# C1 (a) witness
A, B = frozenset({1}), frozenset({2})
assert (1, 2) in prod(A | B, A | B) and prod(A, A) | prod(B, B) == {(1, 1), (2, 2)}
print("exr-products-and-relations-b3: all identities check")
