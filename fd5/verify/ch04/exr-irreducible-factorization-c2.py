"""exr-irreducible-factorization-c2: the coefficient comparison for (x^2 + ax + b)(x^2 + cx + d) = x^4 + 1 and the candidates +-1."""
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
QUOTED = {"values_at_pm1": 2}
assert ev([1, 0, 0, 0, 1], 1) == QUOTED["values_at_pm1"] == ev([1, 0, 0, 0, 1], -1)
# symbolic check of the coefficient formula on random rationals
import random
random.seed(1)
for _ in range(200):
    a, b, c, d = (Fr(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4))
    lhs = mul([b, a, 1], [d, c, 1])
    rhs = norm([b * d, a * d + b * c, b + d + a * c, a + c, 1])
    assert lhs == rhs
# no rational solution: a^2 = 2b with b = +-1, or b^2 = -1; search a small box
sols = [(a, b, c, d) for a in [Fr(s, t) for s in range(-12, 13) for t in range(1, 7)]
        for b in (Fr(1), Fr(-1)) for c in [-a] for d in [b]
        if mul([b, a, 1], [d, c, 1]) == norm([1, 0, 0, 0, 1])]
assert sols == []
print("exr-irreducible-factorization-c2: ok")
