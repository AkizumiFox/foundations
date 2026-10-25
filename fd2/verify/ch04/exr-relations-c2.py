"""exr-relations-c2: symmetric + transitive => reflexive on the domain D and R subset of D x D."""
from itertools import product, chain, combinations

QUOTED = {}
X = [1, 2, 3]
pairs = list(product(X, X))
count = 0
for c in chain.from_iterable(combinations(pairs, r) for r in range(10)):
    R = set(c)
    sym = all((y, x) in R for (x, y) in R)
    trans = all((x, z) in R for (x, y) in R for (y2, z) in R if y == y2)
    if sym and trans:
        count += 1
        D = {x for (x, y) in R}
        assert all((x, x) in R for x in D)
        assert all(x in D and y in D for (x, y) in R)
# the warning's witness: the empty relation on {1}
assert not all((x, x) in set() for x in [1])
print("ok")
