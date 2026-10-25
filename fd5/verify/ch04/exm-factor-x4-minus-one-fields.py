"""exm-factor-x4-minus-one-fields: x^4 - 1 over Q, R, F_3, F_5, F_2; (x + 1)^2 = x^2 + 1 over F_2; x^2 + x + 1 over F_2, F_3 (check)."""
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
QUOTED = {
    "x2p1_values_F3": [1, 2, 2],
    "F5_roots_of_x2p1": [2, 3],
    "F5_factors": [1, 2, 3, 4],
    "x2px1_values_F2": [1, 1],
}
X4M1 = [-1, 0, 0, 0, 1]
for P in (None, 2, 3, 5):
    assert mulmany(lin(1, P), lin(-1, P), [1, 0, 1], P=P) == norm(X4M1, P)
assert [ev([1, 0, 1], c, 3) for c in range(3)] == QUOTED["x2p1_values_F3"]
assert [c for c in range(5) if ev([1, 0, 1], c, 5) == 0] == QUOTED["F5_roots_of_x2p1"]
assert mul(lin(2, 5), lin(3, 5), 5) == norm([1, 0, 1], 5)
assert mulmany(*[lin(c, 5) for c in QUOTED["F5_factors"]], P=5) == norm(X4M1, 5)
assert lin(-1, 5) == lin(4, 5)
assert pw([1, 1], 2, 2) == norm([1, 0, 1], 2)
assert pw([1, 1], 4, 2) == norm(X4M1, 2)
assert lin(1, 2) == lin(-1, 2)
# Q: x^2 + 1 has no rational root since c^2 + 1 >= 1; spot-check on a grid
assert all(ev([1, 0, 1], Fr(a, b)) >= 1 for a in range(-20, 21) for b in range(1, 8))
assert [ev([1, 1, 1], c, 2) for c in range(2)] == QUOTED["x2px1_values_F2"]
assert ev([1, 1, 1], 1, 3) == 0 and pw(lin(1, 3), 2, 3) == norm([1, 1, 1], 3)
print("exm-factor-x4-minus-one-fields: ok")
