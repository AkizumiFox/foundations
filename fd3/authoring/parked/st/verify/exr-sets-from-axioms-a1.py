"""exr-sets-from-axioms-a1 (Section 9.1): P(emptyset) = {emptyset}, U{emptyset} = emptyset,
and U{a} = a on a small universe."""
from itertools import combinations

E = frozenset()


def power(X):
    X = list(X)
    return frozenset(frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k))


def union(F):
    return frozenset(x for A in F for x in A)


QUOTED = {"power_empty": frozenset({E}), "union_singleton_empty": E}
assert power(E) == QUOTED["power_empty"]
assert union(frozenset({E})) == QUOTED["union_singleton_empty"]
V = [E]
for _ in range(3):
    V = list(power(V))
for a in V:
    assert union(frozenset({a})) == a
    for b in V:
        assert (frozenset({a}) == frozenset({b})) == (a == b)
print("exr-sets-from-axioms-a1: all quoted values check")
