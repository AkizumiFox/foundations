"""def-polynomial-composition: (x^2 + 1) o (x + 1) = x^2 + 2x + 2; (x + 1)^2; p(-x) has coefficients (-1)^k p_k."""
QUOTED = {"result": [2, 2, 1], "(x+1)^2": [1, 2, 1]}

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

assert comp([1, 0, 1], [1, 1]) == QUOTED["result"]
assert power([1, 1], 2) == QUOTED["(x+1)^2"]
random.seed(5)
for _ in range(500):
    p = red([random.randrange(-5, 6) for _ in range(5)])
    assert comp(p, [0, -1]) == red([(-1) ** k * a for k, a in enumerate(p)])
    assert comp(p, [0, 1]) == p
print("def-polynomial-composition: ok")
