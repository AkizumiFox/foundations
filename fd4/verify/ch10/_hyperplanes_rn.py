"""Shared exact helpers for the ch10 sidecars (fractions only)."""
from fractions import Fraction as Fr


def vec(*xs):
    return tuple(Fr(x) for x in xs)


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def mul(t, x):
    return tuple(Fr(t) * a for a in x)


def nsq(x):
    return dot(x, x)
