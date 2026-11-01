"""Exact helpers for the Section 9.5 sidecars (vectors as tuples of Fractions)."""
from fractions import Fraction as Fr
import random


def dot(x, y): return sum(Fr(a) * Fr(b) for a, b in zip(x, y))
def n2(x): return dot(x, x)
def add(x, y): return tuple(Fr(a) + Fr(b) for a, b in zip(x, y))
def sc(c, x): return tuple(Fr(c) * Fr(a) for a in x)
def parallel(x, y):
    """y = cx or x = cy for some c (zero vectors included)."""
    for a, b in ((x, y), (y, x)):
        if all(v == 0 for v in a):
            if all(v == 0 for v in b): return True
            continue
        m = next(i for i, v in enumerate(a) if v != 0)
        c = Fr(b[m]) / Fr(a[m])
        if all(Fr(b[i]) == c * Fr(a[i]) for i in range(len(a))): return True
    return False
def rvec(n, lo=-4, hi=4): return tuple(Fr(random.randint(lo, hi)) for _ in range(n))
