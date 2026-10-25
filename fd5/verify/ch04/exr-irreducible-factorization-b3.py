"""exr-irreducible-factorization-b3: all 14 polynomials of degree 1, 2, 3 over F_2 and the irreducible ones."""
from fractions import Fraction as Fr
from itertools import product as _iprod

# Dense polynomials: lists of coefficients, lowest degree first. P = None means Q; P = p means F_p.
def norm(a, P=None):
    a = [Fr(c) if P is None else c % P for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a
def add(a, b, P=None):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], P)
def neg(a, P=None):
    return norm([-c for c in a], P)
def sub(a, b, P=None):
    return add(a, neg(b, P), P)
def mul(a, b, P=None):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return norm(r, P)
def mulmany(*fs, P=None):
    r = [1]
    for f in fs:
        r = mul(r, f, P)
    return norm(r, P)
def pw(a, n, P=None):
    r = [1]
    for _ in range(n):
        r = mul(r, a, P)
    return norm(r, P)
def inv(c, P=None):
    return Fr(1) / c if P is None else pow(c, P - 2, P)
def divmod_(a, b, P=None):
    a, b = norm(a, P), norm(b, P)
    assert b
    q = [0] * max(len(a) - len(b) + 1, 1)
    r = a[:]
    lb = inv(b[-1], P)
    while r and len(r) >= len(b):
        k = len(r) - len(b)
        c = r[-1] * lb
        if P is not None:
            c %= P
        q[k] = c
        r = sub(r, [0] * k + [c * x for x in b], P)
    return norm(q, P), r
def ev(a, c, P=None):
    v = 0
    for x in reversed(a):
        v = v * c + x
    return v if P is None else v % P
def deriv(a, P=None):
    return norm([k * a[k] for k in range(1, len(a))], P)
def monic(a, P=None):
    a = norm(a, P)
    l = inv(a[-1], P)
    return norm([c * l for c in a], P)
def gcd(a, b, P=None):
    a, b = norm(a, P), norm(b, P)
    while b:
        a, b = b, divmod_(a, b, P)[1]
    return monic(a, P) if a else []
def lin(c, P=None):
    return norm([-c, 1], P)
QUOTED = {"count": 14, "irreducible": [[0, 1], [1, 1], [1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1]]}
polys = [list(t) + [1] for d in (1, 2, 3) for t in _iprod((0, 1), repeat=d)]
assert len(polys) == QUOTED["count"]
def reducible(f):
    d = len(f) - 1
    for e in range(1, d):
        for g in [list(t) + [1] for t in _iprod((0, 1), repeat=e)]:
            if not divmod_(f, g, 2)[1]:
                return True
    return False
irr = [f for f in polys if not reducible(f)]
assert sorted(irr) == sorted(QUOTED["irreducible"])
# the criterion of the solution: degree 2, 3 irreducible iff constant term 1 and odd number of non-zero coefficients
for f in polys:
    if len(f) >= 3:
        assert (f in irr) == (f[0] == 1 and sum(f) % 2 == 1)
        assert (f in irr) == all(ev(f, c, 2) != 0 for c in (0, 1))
print("exr-irreducible-factorization-b3: ok")
