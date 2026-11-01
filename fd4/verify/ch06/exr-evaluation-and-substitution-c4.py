"""exr-evaluation-and-substitution-c4: a^(p-1) = 1 in F_p; b -> ab bijective; x^p - x vanishes on F_p and is non-zero."""
QUOTED = {}

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

for p in (2, 3, 5, 7, 11, 13):
    for a in range(1, p):
        assert sorted((a * b) % p for b in range(1, p)) == list(range(1, p))
        assert pow(a, p - 1, p) == 1
    f = [0, -1] + [0] * (p - 2) + [1]
    f = red(f, p)
    assert deg(f) == p and all(ev(f, c, p) == 0 for c in range(p))
    P = [1]
    for c in range(p):
        P = mul(P, [-c, 1], p)
    assert P == f
print("exr-evaluation-and-substitution-c4: ok")
