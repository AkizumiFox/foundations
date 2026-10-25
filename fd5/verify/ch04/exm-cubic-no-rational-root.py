"""exm-cubic-no-rational-root: the eight candidates for 3x^3 + x^2 - 2 and their values; the check 2x^2 + 3x - 2."""
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
    "values": {Fraction(1): Fraction(2), Fraction(-1): Fraction(-4), Fraction(2): Fraction(26), Fraction(-2): Fraction(-22),
               Fraction(1, 3): Fraction(-16, 9), Fraction(-1, 3): Fraction(-2), Fraction(2, 3): Fraction(-2, 3), Fraction(-2, 3): Fraction(-22, 9)},
    "check_candidates_up_to_sign": {Fraction(1), Fraction(2), Fraction(1, 2)},
    "check_roots": {Fraction(1, 2), Fraction(-2)},
}
f = [-2, 0, 1, 3]
def divisors(n):
    return [d for d in range(1, abs(n) + 1) if n % d == 0]
cands = {Fraction(s * u, v) for u in divisors(2) for v in divisors(3) for s in (1, -1)}
assert divisors(3) == [1, 3] and divisors(2) == [1, 2]
assert cands == set(QUOTED["values"])
for c, v in QUOTED["values"].items():
    assert ev(f, c) == v and v != 0
assert Fraction(3) * Fraction(8, 27) + Fraction(4, 9) - 2 == Fraction(-2, 3)
g = [-2, 3, 2]
cg = {Fraction(s * u, v) for u in divisors(2) for v in divisors(2) for s in (1, -1)}
assert cg == {s * c for c in QUOTED["check_candidates_up_to_sign"] for s in (1, -1)}
assert {c for c in cg if ev(g, c) == 0} == QUOTED["check_roots"]
assert mul([-1, 2], [2, 1]) == norm(g)
print("exm-cubic-no-rational-root: ok")
