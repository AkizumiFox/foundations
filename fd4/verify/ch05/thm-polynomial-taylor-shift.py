"""thm-polynomial-taylor-shift: x^2 = 1 + 2(x - 1) + (x - 1)^2; the check: x^3 at 1 has coefficients 1, 3, 3, 1."""
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
QUOTED = {"x2": [1, 2, 1], "x3": [1, 3, 3, 1],
          "x3_divisions": [([1, 1, 1], 1), ([2, 1], 3), ([1], 3)]}
def taylor(f, c, P=None):
    bs, q = [], norm(f, P)
    while q:
        q, r = divmod_(q, lin(c, P), P)
        bs.append(r[0] if r else 0)
    return bs
def recombine(bs, c, P=None):
    r = []
    for j, b in enumerate(bs):
        r = add(r, mul([b], pw(lin(c, P), j, P), P), P)
    return r
assert taylor([0, 0, 1], 1) == QUOTED["x2"] and recombine(QUOTED["x2"], 1) == norm([0, 0, 1])
assert taylor([0, 0, 0, 1], 1) == QUOTED["x3"] and recombine(QUOTED["x3"], 1) == norm([0, 0, 0, 1])
q = [0, 0, 0, 1]
for qq, r in QUOTED["x3_divisions"]:
    q2, r2 = divmod_(q, lin(1))
    assert q2 == norm(qq) and (r2 or [0])[0] == r
    q = q2
print("thm-polynomial-taylor-shift: ok")
