"""exr-sets-from-axioms-b1 (Section 9.1): P(P(emptyset)) = {emptyset, {emptyset}};
U P(X) = X on every hereditarily finite set of rank <= 3."""
from itertools import combinations

E = frozenset()


def power(X):
    X = list(X)
    return frozenset(frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k))


def union(F):
    return frozenset(x for A in F for x in A)


QUOTED = {"ppe": frozenset({E, frozenset({E})})}
assert power(power(E)) == QUOTED["ppe"]
V = [E]
for _ in range(3):
    V = list(power(V))
for X in V:
    assert union(power(X)) == X
print("exr-sets-from-axioms-b1: all quoted values check")
