"""exr-evaluation-and-substitution-c3: (a) the identity; (b) factor theorem; (c) roots of x^2 - 1 in Z/8Z."""
QUOTED = {"squares mod 8": [0, 1, 4, 1, 0, 1, 4, 1], "roots": [1, 3, 5, 7], "[5]^2, [7]^2": (25, 49),
          "[2][4]": (2, 4, 8)}

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

for c in range(-4, 5):
    for n in range(1, 7):
        u = [c ** (n - 1 - j) for j in range(n)]
        lhs = red([-(c ** n)] + [0] * (n - 1) + [1])
        assert mul([-c, 1], u) == lhs
assert [(k * k) % 8 for k in range(8)] == QUOTED["squares mod 8"]
assert [k for k in range(8) if (k * k - 1) % 8 == 0] == QUOTED["roots"]
assert 5 * 5 == 25 and 7 * 7 == 49 and 25 % 8 == 1 and 49 % 8 == 1
assert ((3 - 1) * (3 + 1)) % 8 == 0 and (3 - 1) % 8 and (3 + 1) % 8
# (b): for every p with p(c) = 0 over Z/8Z there is q with p = (x - c) q (synthetic division)
for p in itertools.product(range(8), repeat=3):
    p = red(p, 8)
    for c in range(8):
        if ev(p, c, 8) == 0:
            # divide by x - c (monic): synthetic division
            if not p:
                continue
            coeffs = p[::-1]
            out = [coeffs[0]]
            for a in coeffs[1:]:
                out.append((a + c * out[-1]) % 8)
            assert out[-1] == 0
            q = red(out[:-1][::-1], 8)
            assert mul([-c, 1], q, 8) == p
print("exr-evaluation-and-substitution-c3: ok")
