"""exr-relations-a1: (c) |x - y| <= 1 on a grid; (d) 4 reflexive relations on a 2-element set."""
from itertools import product, chain, combinations
from fractions import Fraction as Fr

QUOTED = {"reflexive_count": 4}
X = ["p", "q"]
pairs = list(product(X, X))
rels = [set(c) for c in chain.from_iterable(combinations(pairs, r) for r in range(5))]
assert sum(all((x, x) in R for x in X) for R in rels) == QUOTED["reflexive_count"]
close = lambda x, y: abs(x - y) <= 1
assert close(0, 1) and close(1, 2) and not close(0, 2) and close(1, 0)
grid = [Fr(n, 3) for n in range(-9, 10)]
assert all(close(x, x) for x in grid) and all(close(y, x) for x in grid for y in grid if close(x, y))
print("ok")
