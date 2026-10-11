"""Helpers for the Chapter 6 sidecars: all subsets of a small universe, products, functions."""
from itertools import product, chain, combinations


def subsets(u):
    u = list(u)
    return [frozenset(c) for c in chain.from_iterable(combinations(u, k) for k in range(len(u) + 1))]


def prod(a, b):
    return frozenset(product(a, b))


def functions(x, y):
    """All functions x -> y, as dicts."""
    x = sorted(x)
    return [dict(zip(x, vals)) for vals in product(sorted(y), repeat=len(x))]


def injective(f):
    return len(set(f.values())) == len(f)


def surjective(f, y):
    return set(f.values()) == set(y)


def is_function(rel, x, y):
    return rel <= prod(x, y) and all(sum(1 for (a, _) in rel if a == e) == 1 for e in x)
