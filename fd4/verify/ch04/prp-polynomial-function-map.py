"""prp-polynomial-function-map: (c) (p o q)(c) = p(q(c)); (d) P = prod (x - c) monic of degree r, vanishing on R,
for R = F_2, F_3, Z/4Z, Z/6Z."""
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

for n in (2, 3, 4, 6):
    P = [1]
    for c in range(n):
        P = mul(P, [-c, 1], n)
    assert deg(P) == n and P[-1] == 1
    assert all(ev(P, c, n) == 0 for c in range(n))
random.seed(6)
for n in (5, 6, None):
    for _ in range(500):
        p = red([random.randrange(-4, 5) for _ in range(4)], n)
        q = red([random.randrange(-4, 5) for _ in range(3)], n)
        c = random.randrange(-3, 4)
        lhs = ev(comp(p, q, n), c, n)
        rhs = ev(p, ev(q, c, n), n)
        assert (lhs - rhs) % n == 0 if n else lhs == rhs
print("prp-polynomial-function-map: ok")
