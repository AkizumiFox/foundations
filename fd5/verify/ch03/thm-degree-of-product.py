"""thm-degree-of-product (a) on random pairs over Z/6Z and Z: (pq)_k = 0 above m+n, (pq)_{m+n} = lc lc."""
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

random.seed(1)
for n in (6, None, 4, 9):
    for _ in range(3000):
        p = red([random.randrange(-9, 10) for _ in range(random.randrange(1, 6))], n)
        q = red([random.randrange(-9, 10) for _ in range(random.randrange(1, 6))], n)
        if not p or not q:
            continue
        m, k = deg(p), deg(q)
        full = [0] * (m + k + 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                full[i + j] += a * b
        r = mul(p, q, n)
        top = (p[-1] * q[-1]) % n if n else p[-1] * q[-1]
        assert len(r) <= m + k + 1
        assert (r[m + k] if len(r) > m + k else 0) == top
        if top != 0:
            assert deg(r) == m + k
# degree of a sum
for _ in range(2000):
    p = red([random.randrange(-3, 4) for _ in range(random.randrange(0, 5))])
    q = red([random.randrange(-3, 4) for _ in range(random.randrange(0, 5))])
    s = add(p, q)
    dp, dq, ds = deg(p), deg(q), deg(s)
    M = max([d for d in (dp, dq) if d is not None], default=None)
    if M is None:
        assert ds is None
    else:
        assert ds is None or ds <= M
        if dp != dq:
            assert ds == M
print("thm-degree-of-product: ok")
