"""exr-evaluation-and-substitution-b2: the table of F_2[x]_{<=2}; four functions, two polynomials each."""
QUOTED = {
    "rows": [((), None, 0, 0), ((1,), 0, 1, 1), ((0, 1), 1, 0, 1), ((1, 1), 1, 1, 0),
             ((0, 0, 1), 2, 0, 1), ((1, 0, 1), 2, 1, 0), ((0, 1, 1), 2, 0, 0), ((1, 1, 1), 2, 1, 1)],
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

rows = QUOTED["rows"]
seen = set()
for coeffs, d, v0, v1 in rows:
    p = list(coeffs)
    assert deg(p) == d and ev(p, 0, 2) == v0 and ev(p, 1, 2) == v1
    seen.add(tuple(p))
assert seen == {tuple(red(t)) for t in itertools.product(range(2), repeat=3)}
from collections import Counter
cnt = Counter((v0, v1) for _, _, v0, v1 in rows)
assert len(cnt) == 4 == 2 * 2 and set(cnt.values()) == {2}
for (c1, _, a0, a1) in rows:
    for (c2, _, b0, b1) in rows:
        if (a0, a1) == (b0, b1) and c1 != c2:
            assert add(list(c1), list(c2), 2) == [0, 1, 1]
print("exr-evaluation-and-substitution-b2: ok")
