"""Exact rational checks for Section 1.5's sidecars: does one condition on a real x imply another?

Each condition used is a polynomial inequality in x whose truth can change only at a few points
(the boundaries, passed in).  Sampling every k/16 in [-30, 30], every boundary b and b +- 10^-9,
decides the implication for such conditions on that range; the conditions used change truth only
at boundaries inside it.
"""
from fractions import Fraction


def grid(boundaries=()):
    pts = {Fraction(k, 16) for k in range(-30 * 16, 30 * 16 + 1)}
    eps = Fraction(1, 10**9)
    for b in boundaries:
        b = Fraction(b)
        pts |= {b - eps, b, b + eps}
    return sorted(pts)


def implies(p, q, boundaries=()):
    """p(x) -> q(x) at every sample point."""
    return all((not p(x)) or q(x) for x in grid(boundaries))


def everywhere(p, boundaries=()):
    return all(p(x) for x in grid(boundaries))
