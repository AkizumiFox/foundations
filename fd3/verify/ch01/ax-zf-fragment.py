"""ax-zf-fragment (Section 9.1): the list "The first sets" after the axioms, and the
Quick check after prp-zf-basic-sets (unions of small sets). Sets are frozensets."""
from itertools import combinations

E = frozenset()


def S(*xs):
    return frozenset(xs)


def union(F):
    return frozenset(x for A in F for x in A)


def power(X):
    X = list(X)
    return frozenset(frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k))


one = S(E)            # {emptyset}
two = S(E, one)       # {emptyset, {emptyset}}

QUOTED = {
    "singleton": one,
    "pair_size": 2,
    "union_of_two": one,
    "power_of_one": two,
    "separation": S(one),
    "check_union_empty": E,
    "check_union_of_singleton_empty": E,
    "check_union_third": two,
}

assert one != E
assert S(E, E) == QUOTED["singleton"]
assert len(two) == QUOTED["pair_size"]
assert union(two) == QUOTED["union_of_two"]
assert power(one) == QUOTED["power_of_one"]
assert frozenset(x for x in two if x != E) == QUOTED["separation"]
# Quick check
assert union(E) == QUOTED["check_union_empty"]
assert union(S(E)) == QUOTED["check_union_of_singleton_empty"]
assert union(S(S(E), S(E, S(E)))) == QUOTED["check_union_third"]
print("ax-zf-fragment: all quoted values check")
