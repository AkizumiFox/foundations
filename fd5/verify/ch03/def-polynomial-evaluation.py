"""def-polynomial-evaluation: examples, the warning, and (x - 1)(x - 2) = x^2 - 3x + 2."""
QUOTED = {
    "x^2 - 3x + 2 at 0, 1, 2": (2, 0, 0),
    "1 - 3 + 2": (1, -3, 2),
    "4 - 6 + 2": (4, -6, 2),
    "x^3 + 2 over F_3 at 0, 1, 2": (2, 0, 1),
    "8 + 2 = 10": (8, 2, 10),
    "p_2 = 1, p_0 = 2": (1, 2),
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

p = [2, -3, 1]
assert tuple(ev(p, c) for c in (0, 1, 2)) == QUOTED["x^2 - 3x + 2 at 0, 1, 2"]
assert 1 - 3 + 2 == 0 and 4 - 6 + 2 == 0
assert tuple(ev([2, 0, 0, 1], c, 3) for c in (0, 1, 2)) == QUOTED["x^3 + 2 over F_3 at 0, 1, 2"]
assert 8 + 2 == 10 and 10 % 3 == 1
assert p[2] == 1 and p[0] == 2
assert mul([-1, 1], [-2, 1]) == p
# rational roots: among a range of rationals only 1 and 2
from fractions import Fraction as Fr
roots = {Fr(a, b) for a in range(-12, 13) for b in range(1, 7) if Fr(a, b)**2 - 3*Fr(a, b) + 2 == 0}
assert roots == {1, 2}
print("def-polynomial-evaluation: ok")
