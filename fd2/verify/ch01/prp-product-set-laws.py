"""prp-product-set-laws: all eight laws, checked on every triple of subsets of a
three-element universe (Ch 6 Section 6.3). No numeric values are quoted."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import subsets, prod

QUOTED = {"laws checked": True}

S = subsets({0, 1, 2})
E = frozenset()
for A in S:
    assert prod(A, E) == E and prod(E, A) == E
    for B in S:
        for C in S:
            assert prod(A, B | C) == prod(A, B) | prod(A, C)
            assert prod(A, B & C) == prod(A, B) & prod(A, C)
            assert prod(A, B - C) == prod(A, B) - prod(A, C)
            assert prod(B | C, A) == prod(B, A) | prod(C, A)
            assert prod(B & C, A) == prod(B, A) & prod(C, A)
            assert prod(B - C, A) == prod(B, A) - prod(C, A)
# the remark: A x B empty iff A or B empty
for A in S:
    for B in S:
        assert (prod(A, B) == E) == (A == E or B == E)
print("prp-product-set-laws: all laws check")
