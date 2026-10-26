"""exm-polynomial-function-finite-field: (a) x^3 + 2x on F_3 and its factorization; (b) x^p - x = prod (x - c) for p <= 7; the warning's values."""
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
QUOTED = {"values_F3": [0, 0, 0], "eight_minus_two": 6}
f = [0, 2, 0, 1]
assert [ev(f, c, 3) for c in range(3)] == QUOTED["values_F3"]
assert norm(f, 3) == norm([0, -1, 0, 1], 3)
assert mulmany(lin(0, 3), lin(1, 3), lin(2, 3), P=3) == norm(f, 3)
assert mulmany(lin(0), lin(1), lin(2)) == norm([0, 2, -3, 1])
assert 8 - 2 == QUOTED["eight_minus_two"]
for p in (2, 3, 5, 7):
    xp = norm([0, -1] + [0] * (p - 2) + [1], p)
    assert mulmany(*[lin(c, p) for c in range(p)], P=p) == xp
    assert all(ev(xp, c, p) == 0 for c in range(p))
print("exm-polynomial-function-finite-field: ok")
