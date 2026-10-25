"""exr-multiple-roots-c2: (a) the Euclidean run for f = x^4 - 2x^3 + 2x - 1 and f'; (b) x^4 + 1 over F_2."""
from fractions import Fraction
from itertools import product as _iprod

# Dense polynomials: lists of coefficients, lowest degree first. P = None means Q; P = p means F_p.
def norm(a, P=None):
    a = [Fraction(c) if P is None else c % P for c in a]
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
    return Fraction(1) / c if P is None else pow(c, P - 2, P)
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
QUOTED = {
    "fprime": [2, 0, -6, 4], "q1": [Fraction(-1, 8), Fraction(1, 4)], "r1_scalar": Fraction(-3, 4), "r1_monic": [1, -2, 1],
    "q2_scalar": Fraction(-8, 3), "q2_factor": [1, 2], "gcd": [1, -2, 1], "f_prime_factor": [1, 0, -3, 2],
}
f = [-1, 2, 0, -2, 1]
fp = deriv(f)
assert fp == norm(QUOTED["fprime"])
q1, r1 = divmod_(f, fp)
assert q1 == norm(QUOTED["q1"])
assert r1 == norm([c * QUOTED["r1_scalar"] for c in QUOTED["r1_monic"]])
q2, r2 = divmod_(fp, r1)
assert r2 == []
assert q2 == norm([c * QUOTED["q2_scalar"] for c in QUOTED["q2_factor"]])
assert gcd(f, fp) == norm(QUOTED["gcd"])
assert mul(pw(lin(1), 2), [1, 2]) == norm(QUOTED["f_prime_factor"]) and mul([2], QUOTED["f_prime_factor"]) == fp
g = [1, 0, 0, 0, 1]
assert deriv(g, 2) == [] and pw([1, 1], 4, 2) == norm(g, 2)
assert deriv([1, 0, 1], 2) == []
print("exr-multiple-roots-c2: ok")
