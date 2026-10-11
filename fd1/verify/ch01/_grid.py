"""Shared helper for the Chapter 1 sidecars: exact rational sample points."""
from fractions import Fraction


def grid(lo=-20, hi=20, den=8):
    """Every rational k/den in [lo, hi], plus near-boundary points of the inequalities used."""
    pts = {Fraction(k, den) for k in range(lo * den, hi * den + 1)}
    for b in (-3, -2, -1, 0, 1, 2, 3):
        for eps in (Fraction(1, 10**6), Fraction(1, 10**9)):
            pts |= {Fraction(b) - eps, Fraction(b), Fraction(b) + eps}
    return sorted(pts)


def implies_on_grid(p, q):
    """p(x) -> q(x) at every sample point."""
    return all((not p(x)) or q(x) for x in grid())
