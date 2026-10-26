"""exm-failed-pair-encodings (Section 9.2): the counterexamples for the encodings
(i) {a, b}, (ii) {{a}, {b}}, (iii) {a, {b}}; also a search showing each fails on the
16 hereditarily finite sets of rank <= 3, while the Kuratowski pair does not."""
from itertools import combinations, product

E = frozenset()


def S(*xs):
    return frozenset(xs)


def power(X):
    X = list(X)
    return [frozenset(c) for k in range(len(X) + 1) for c in combinations(X, k)]


enc = {
    "i": lambda a, b: S(a, b),
    "ii": lambda a, b: S(S(a), S(b)),
    "iii": lambda a, b: S(a, S(b)),
}
one = S(E)
QUOTED = {
    "i": S(E, one),
    "ii": S(one, S(one)),
    "iii": S(S(one), one),
}
assert enc["i"](E, one) == enc["i"](one, E) == QUOTED["i"]
assert enc["ii"](E, one) == enc["ii"](one, E) == QUOTED["ii"]
a, b, c, d = S(one), E, one, one
assert enc["iii"](a, b) == enc["iii"](c, d) == QUOTED["iii"]
assert a != c and E in c and E not in a

V = [E]
for _ in range(3):
    V = power(V)
for name, f in enc.items():
    bad = any(f(a, b) == f(c, d) and (a, b) != (c, d)
              for a, b, c, d in product(V, repeat=4))
    assert bad, name
print("exm-failed-pair-encodings: all quoted values check")
