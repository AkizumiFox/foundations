"""prp-polynomial-units: the warning (1 + [2]x)^2 = 1 in (Z/4Z)[x]; units of Z[x] small search."""
QUOTED = {"square over Z": [1, 4, 4], "lc*lc": (2, 2)}

# Polynomials as coefficient lists (index k = coefficient of x^k), over Z or Z/nZ (n given).
from fractions import Fraction
import itertools, random

def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p

def red(p, n=None):
    return trim([c % n for c in p] if n else p)

def add(p, q, n=None):
    m = max(len(p), len(q))
    return red([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(m)], n)

def neg(p, n=None):
    return red([-c for c in p], n)

def mul(p, q, n=None):
    if not p or not q:
        return []
    r = [0] * (len(p) + len(q) - 1)
    for k in range(len(r)):
        r[k] = sum(p[i] * q[k - i] for i in range(k + 1) if i < len(p) and 0 <= k - i < len(q))
    return red(r, n)

def power(p, e, n=None):
    r = [1]
    for _ in range(e):
        r = mul(r, p, n)
    return red(r, n)

def deg(p):
    p = trim(p)
    return len(p) - 1 if p else None   # None stands for -infinity

def ev(p, c, n=None):
    v = sum(a * c ** k for k, a in enumerate(p))
    return v % n if n else v

def comp(p, q, n=None):
    r = []
    for k, a in enumerate(p):
        r = add(r, mul([a], power(q, k, n), n), n)
    return r

assert mul([1, 2], [1, 2]) == QUOTED["square over Z"]
assert mul([1, 2], [1, 2], 4) == [1]
assert (2 * 2) % 4 == 0
# over Z (an integral domain) no non-constant unit with small coefficients and degree <= 2
for p in itertools.product(range(-3, 4), repeat=3):
    p = red(p)
    for q in itertools.product(range(-3, 4), repeat=3):
        q = red(q)
        if mul(p, q) == [1]:
            assert deg(p) == 0 and p[0] in (1, -1)
print("prp-polynomial-units: ok")
