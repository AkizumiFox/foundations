"""exr-degree-b2: inverses in (Z/9Z)[x] and (Z/4Z)[x]."""
QUOTED = {
    "(b) inverse 1 + [6]x": [1, 6],
    "-[3]*[3] = -[9]": 9,
    "(c) square coefficients over Z": [1, 4, 8, 8, 4],
    "(c) middle sums": (2, 4, 2),
}

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

assert mul([1, 3], [1, -3], 9) == [1]
assert (-3) % 9 == 6 and mul([1, 3], QUOTED["(b) inverse 1 + [6]x"], 9) == [1]
p = [1, 2, 2]
assert mul(p, p) == QUOTED["(c) square coefficients over Z"]
assert p[0]*p[2] == 2 and p[1]*p[1] == 4 and p[2]*p[0] == 2
assert mul(p, p, 4) == [1]
print("exr-degree-b2: ok")
