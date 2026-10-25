"""Shared helper for the Section 7.4 sidecars: properties of a binary relation R on a
finite domain D, by direct enumeration (independent of the satisfaction evaluator)."""
import itertools


def refl(D, R):
    return all((d, d) in R for d in D)


def irrefl(D, R):
    return all((d, d) not in R for d in D)


def sym(D, R):
    return all((e, d) in R for (d, e) in R)


def antisym(D, R):
    return all(d == e for (d, e) in R if (e, d) in R)


def trans(D, R):
    return all((d, f) in R for (d, e) in R for (e2, f) in R if e == e2)


def conn(D, R):
    return all((d, e) in R or (e, d) in R for d in D for e in D)


def all_relations(D):
    pairs = list(itertools.product(D, repeat=2))
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        yield {p for p, b in zip(pairs, bits) if b}
