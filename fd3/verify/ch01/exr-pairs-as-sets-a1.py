"""exr-pairs-as-sets-a1 (Section 9.2): (b) the run of the proof on ({0}, 0) = (c, d)
forces c = {0}, d = 0 (0 = emptyset); searched over the 16 sets of rank <= 3."""
from itertools import combinations, product

E = frozenset()


def S(*xs):
    return frozenset(xs)


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


def pair(a, b):
    return S(S(a), S(a, b))


one = S(E)
QUOTED = {"c": one, "d": E}
V = [E]
for _ in range(3):
    V = power(V)
sols = [(c, d) for c, d in product(V, repeat=2) if pair(c, d) == pair(one, E)]
assert sols == [(QUOTED["c"], QUOTED["d"])]
print("exr-pairs-as-sets-a1: all quoted values check")
