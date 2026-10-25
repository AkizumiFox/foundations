"""cor-polynomial-coefficient-change: 2x^2 + 3x - 1 -> x + 1 over F_2; 6x^3 + 5x^2 + x -> [5]x^2 + x mod 6."""
QUOTED = {"source": [-1, 3, 2], "image over F_2": [1, 1], "degrees": (2, 1), "mod 6": [0, 1, 5]}

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

assert red([-1, 3, 2], 2) == QUOTED["image over F_2"]
assert deg([-1, 3, 2]) == 2 and deg(red([-1, 3, 2], 2)) == 1
assert red([0, 1, 5, 6], 6) == QUOTED["mod 6"]
# phi_* is a ring homomorphism Z[x] -> (Z/nZ)[x] (random)
random.seed(4)
for n in (2, 3, 6):
    for _ in range(1000):
        p = [random.randrange(-9, 10) for _ in range(4)]
        q = [random.randrange(-9, 10) for _ in range(4)]
        assert red(mul(p, q), n) == mul(red(p, n), red(q, n), n)
        assert red(add(p, q), n) == add(red(p, n), red(q, n), n)
print("cor-polynomial-coefficient-change: ok")
