"""exr-evaluation-and-substitution-a1: (c) [1 + 6 + 4] = [11] = [1], [3][2]^2 = [12] = [2]; (e) values 2, 0, 1 and the product."""
QUOTED = {"(c) terms": (1, 6, 4, 11), "(c) 3x^2": 12, "(e) values": (2, 0, 1),
          "(e) product over Z": [2, 3, 3, 1]}

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

assert 1 + 3 * 2 + 1 * 2 ** 2 == 11 and 11 % 5 == 1 and ev([1, 3, 1], 2, 5) == 1
assert 3 * 2 ** 2 == 12 and 12 % 5 == 2
prod = mul([2, 1], [1, 1, 1])
assert prod == QUOTED["(e) product over Z"]
assert red(prod, 3) == [2, 0, 0, 1]
assert tuple(ev(prod, c, 3) for c in (0, 1, 2)) == QUOTED["(e) values"]
assert ((2 + 2) % 3, (4 + 2 + 1) % 3) == (1, 1) and 4 % 3 == 7 % 3 == 1
print("exr-evaluation-and-substitution-a1: ok")
