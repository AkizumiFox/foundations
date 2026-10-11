"""Dense polynomials for the sidecars of fd4 ch05 sections 01-02.

A polynomial is a tuple of coefficients, constant term first, with no trailing zeros
(the zero polynomial is ()). Coefficients are Fractions (p=None) or residues mod p.
"""
from fractions import Fraction as Fr


def norm(a, p=None):
    a = [x % p if p else Fr(x) for x in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def P(*coeffs_high_first, p=None):
    """P(2, -3, 1) is 2x^2 - 3x + 1."""
    return norm(list(reversed(coeffs_high_first)), p)


def deg(a):
    return len(a) - 1 if a else None  # None stands for -infinity


def add(a, b, p=None):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], p)


def neg(a, p=None):
    return norm([-x for x in a], p)


def sub(a, b, p=None):
    return add(a, neg(b, p), p)


def mul(a, b, p=None):
    if not a or not b:
        return ()
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return norm(c, p)


def inv(c, p=None):
    if p:
        c %= p
        assert c != 0
        return pow(c, p - 2, p)
    return 1 / Fr(c)


def divmod_(f, g, p=None):
    """Long division: returns (q, r) and asserts f = qg + r, deg r < deg g."""
    assert g
    q, r = (), f
    b_inv = inv(g[-1], p)
    while r and len(r) >= len(g):
        t = [0] * (len(r) - len(g)) + [r[-1] * b_inv]
        t = norm(t, p)
        q = add(q, t, p)
        r = sub(r, mul(t, g, p), p)
    assert add(mul(q, g, p), r, p) == norm(f, p)
    assert not r or len(r) < len(g)
    return q, r


def monic(a, p=None):
    return norm([x * inv(a[-1], p) for x in a], p) if a else ()


def gcd_run(f, g, p=None):
    """Euclidean algorithm; returns (list of (u, q, v, r), monic gcd)."""
    rows = []
    u, v = f, g
    while v:
        q, r = divmod_(u, v, p)
        rows.append((u, q, v, r))
        u, v = v, r
    return rows, monic(u, p)


def ev(a, c, p=None):
    s = 0
    for x in reversed(a):
        s = s * c + x
    return s % p if p else s


def xpow(n, p=None):
    return norm([0] * n + [1], p)
