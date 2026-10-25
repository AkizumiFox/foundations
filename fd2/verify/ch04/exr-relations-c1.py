"""exr-relations-c1: brute force over all relations on a 3-element set."""
from itertools import product, chain, combinations

QUOTED = {}
X = [1, 2, 3]
pairs = list(product(X, X))
diag = {(x, x) for x in X}
for c in chain.from_iterable(combinations(pairs, r) for r in range(10)):
    R = set(c)
    inv = {(y, x) for (x, y) in R}
    sym = all((y, x) in R for (x, y) in R)
    anti = all(x == y for (x, y) in R if (y, x) in R)
    assert sym == (R == inv)
    assert anti == ((R & inv) <= diag)
    assert (sym and anti) == (R <= diag)
print("ok")
