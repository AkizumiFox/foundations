"""thm-kuratowski-pair (Section 9.2): the characteristic property of {{a}, {a, b}},
exhaustively on the 16 hereditarily finite sets of rank <= 3; the "Alternatively"
route (intersection {a}, union {a, b}, difference {b} or empty); the examples after
def-kuratowski-pair; and the Quick check values (emptyset, emptyset) and (emptyset, {emptyset})."""
from itertools import combinations, product

E = frozenset()


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


def S(*xs):
    return frozenset(xs)


def pair(a, b):
    return S(S(a), S(a, b))


V = [E]
for _ in range(3):
    V = power(V)
assert len(V) == 16

one = S(E)
QUOTED = {
    "pair_aa_members": 1,
    "pair_one_empty": S(S(one), S(one, E)),
    "pair_empty_one": S(one, S(E, one)),
    "check_pair_empty_empty": S(S(E)),
}

for a, b, c, d in product(V, repeat=4):
    assert (pair(a, b) == pair(c, d)) == (a == c and b == d)

for a, b in product(V, repeat=2):
    p = pair(a, b)
    inter = frozenset.intersection(*p)
    uni = frozenset.union(*p)
    assert inter == S(a) and uni == S(a, b)
    diff = uni - inter
    assert diff == (S(b) if a != b else E)
    if a == b:
        assert len(p) == QUOTED["pair_aa_members"]

assert pair(one, E) == QUOTED["pair_one_empty"]
assert pair(E, one) == QUOTED["pair_empty_one"]
assert pair(one, E) != pair(E, one)
assert pair(E, E) == QUOTED["check_pair_empty_empty"]
print("thm-kuratowski-pair: all quoted values check")
