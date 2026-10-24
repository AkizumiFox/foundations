"""Tiny truth-table helper for the Section 6.3 and 6.4 sidecars (skeleton verdicts).
Formulas are Python lambdas over a dict of atom values; bot is the constant False."""
import itertools


def entails(atoms, premises, conclusion):
    for vals in itertools.product([False, True], repeat=len(atoms)):
        v = dict(zip(atoms, vals))
        if all(p(v) for p in premises) and not conclusion(v):
            return False
    return True


def satisfiable(atoms, formulas):
    for vals in itertools.product([False, True], repeat=len(atoms)):
        v = dict(zip(atoms, vals))
        if all(f(v) for f in formulas):
            return True
    return False


def imp(a, b):
    return (not a) or b
