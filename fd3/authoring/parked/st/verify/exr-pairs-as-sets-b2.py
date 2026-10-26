"""exr-pairs-as-sets-b2 (Section 9.2): ((0, 0), 0) != (0, (0, 0)) with 0 = emptyset,
and the characteristic property of nested pairs on a small universe."""
from itertools import combinations, product

E = frozenset()


def S(*xs):
    return frozenset(xs)


def pair(a, b):
    return S(S(a), S(a, b))


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


QUOTED = {"first_coord_left": S(S(E))}
assert pair(E, E) == QUOTED["first_coord_left"]
assert pair(pair(E, E), E) != pair(E, pair(E, E))
V = [E]
for _ in range(2):
    V = power(V)
for a, b, c, a2, b2, c2 in product(V, repeat=6):
    assert (pair(pair(a, b), c) == pair(pair(a2, b2), c2)) == ((a, b, c) == (a2, b2, c2))
print("exr-pairs-as-sets-b2: all quoted values check")
