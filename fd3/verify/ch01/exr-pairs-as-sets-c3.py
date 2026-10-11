"""exr-pairs-as-sets-c3 (Section 9.2): Wiener's encoding {{{a}, 0}, {{b}}} (0 = emptyset)
has the characteristic property on the 16 hereditarily finite sets of rank <= 3."""
from itertools import combinations, product

E = frozenset()


def S(*xs):
    return frozenset(xs)


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


def W(a, b):
    return S(S(S(a), E), S(S(b)))


QUOTED = {}  # no numeric value is quoted in the text; the checks below are exhaustive
V = [E]
for _ in range(3):
    V = power(V)
assert len(V) == 16
for a, b, c, d in product(V, repeat=4):
    assert (W(a, b) == W(c, d)) == (a == c and b == d)
    assert len(W(a, b)) == 2  # the two members always differ
print("exr-pairs-as-sets-c3: all quoted values check")
