"""exr-relations-b4: brute force over all relations on {0,1,2} for (a), (b), (d);
counterexamples (c) {(1,2)}, {(2,1)} and (e) 1, 2, 1."""
from itertools import product
QUOTED = {}
X = [0, 1, 2]
P = list(product(X, X))
rels = [frozenset(p for p, b in zip(P, bits) if b) for bits in product([0, 1], repeat=len(P))]
refl = lambda R, X=X: all((x, x) in R for x in X)
sym = lambda R: all((y, x) in R for (x, y) in R)
anti = lambda R: all(x == y for (x, y) in R if (y, x) in R)
trans = lambda R: all((x, z) in R for (x, y) in R for (y2, z) in R if y == y2)
inv = lambda R: frozenset((y, x) for (x, y) in R)
for R in rels:
    if refl(R) and trans(R):
        E = R & inv(R)
        assert refl(E) and sym(E) and trans(E)          # (a)
    if trans(R):
        assert trans(inv(R))                            # (d)
symm = [R for R in rels if sym(R)]
assert all(sym(A | B) for A in symm for B in symm)      # (b)
R, S = {(1, 2)}, {(2, 1)}
assert anti(R) and anti(S) and not anti(R | S)          # (c)
m3 = lambda x, y: (x + y) % 3 == 0
assert m3(1, 2) and m3(2, 1) and not m3(1, 1)           # (e)
print("ok")
