"""thm-polynomial-substitution: the try-it-first value [3][2][2] + [1] = [13] = [3] in Z/5Z; random checks."""
QUOTED = {"3x^2 + 1 at [2] mod 5": (13, 3)}

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

assert 3 * 2 * 2 + 1 == 13 and 13 % 5 == 3
assert ev([1, 0, 3], 2, 5) == 3
# Phi for phi: Z -> Z/nZ, s in Z/nZ is a ring homomorphism (random)
random.seed(3)
for n in (5, 6, 8):
    for _ in range(1000):
        p = [random.randrange(-7, 8) for _ in range(4)]
        q = [random.randrange(-7, 8) for _ in range(4)]
        s = random.randrange(n)
        Phi = lambda r: sum((a % n) * s ** k for k, a in enumerate(r)) % n
        assert Phi(add(p, q)) == (Phi(p) + Phi(q)) % n
        assert Phi(mul(p, q)) == (Phi(p) * Phi(q)) % n
print("thm-polynomial-substitution: ok")
