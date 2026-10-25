"""exr-relations-b3: intersection of transitive relations is transitive (all relations on 3 points);
{(1,2)} u {(2,3)} is not."""
from itertools import product, chain, combinations

QUOTED = {}
X = [1, 2, 3]
pairs = list(product(X, X))
trans = lambda R: all((x, z) in R for (x, y) in R for (y2, z) in R if y == y2)
T = [frozenset(c) for c in chain.from_iterable(combinations(pairs, r) for r in range(10)) if trans(set(c))]
assert all(trans(A & B) for A in T for B in T)
R, S = {(1, 2)}, {(2, 3)}
assert trans(R) and trans(S) and not trans(R | S)
print("ok")
