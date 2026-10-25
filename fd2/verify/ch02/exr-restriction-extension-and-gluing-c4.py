"""exr-restriction-extension-and-gluing-c4: (1-u)+(1-v)-(1-u)(1-v) = 1-uv; complement law and
c(c(A)) = A on all subsets of a 4-element set; Phi(c(A)) = 1 - Phi(A); 1 - (1 - t) = t."""
from fractions import Fraction as F
from itertools import chain, combinations

QUOTED = {"lhs": lambda u, v: 1 - u * v}
# both sides are polynomials of degree <= 1 in each variable: agreement on a 3 x 3 grid
# (indeed on any grid with 2 values per variable) proves the identity; we check more
pts = [F(k, 3) for k in range(-6, 7)]
assert all((1 - u) + (1 - v) - (1 - u) * (1 - v) == QUOTED["lhs"](u, v) for u in pts for v in pts)
assert all(1 - (1 - t) == t for t in pts)
X = frozenset({1, 2, 3, 4})
subsets = [frozenset(s) for s in chain.from_iterable(combinations(X, r) for r in range(5))]
ind = lambda A: tuple(1 if x in A else 0 for x in sorted(X))
for A in subsets:
    assert ind(X - A) == tuple(1 - a for a in ind(A))
    assert X - (X - A) == A
    for B in subsets:
        assert X - (A & B) == (X - A) | (X - B)
        assert ind(X - (A & B)) == tuple(1 - a * b for a, b in zip(ind(A), ind(B)))
print("exr-restriction-extension-and-gluing-c4: all quoted values check")
