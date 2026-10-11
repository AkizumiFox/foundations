"""exr-degree-b3: |F_p[x]_{<=n}| = p^(n+1), |F_p[x]_{=n}| = (p-1)p^n; the F_2 example 8 and 4."""
QUOTED = {"F2 at most 2": 8, "F2 exactly 2": 4, "2^3": (2, 3), "1*2^2": (1, 2, 2)}

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

for p in (2, 3, 5):
    for n in range(0, 4):
        allp = [red(t) for t in itertools.product(range(p), repeat=n + 1)]
        assert len(allp) == p ** (n + 1)
        assert len([t for t in allp if deg(t) is not None and deg(t) <= n]) + 1 == p ** (n + 1)
        assert len([t for t in allp if deg(t) == n]) == (p - 1) * p ** n
assert 2 ** 3 == QUOTED["F2 at most 2"] and 1 * 2 ** 2 == QUOTED["F2 exactly 2"]
print("exr-degree-b3: ok")
