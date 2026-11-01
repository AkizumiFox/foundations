"""thm-polynomial-quotient-ring: the quick check after the theorem
(x^2 - 2 = (x - 1)(x + 1) - 1; [x + 1]^{-1} = [x - 1] in Q[x]/<x^2 - 2>)."""
from fractions import Fraction as F

QUOTED = {"division": "x^2 - 2 = (x - 1)(x + 1) - 1", "inverse": "[x - 1]"}

# --- small dense-polynomial helpers (coefficients low degree first; p=None: exact Fractions, else mod p) ---
from fractions import Fraction as F


def trim(a, p=None):
    a = [(c % p) if p else c for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p=None):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], p)


def scal(c, a, p=None):
    return trim([c * x for x in a], p)


def sub(a, b, p=None):
    return add(a, scal(-1, b), p)


def mul(a, b, p=None):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out, p)


def prod(lst, p=None):
    out = [1]
    for f in lst:
        out = mul(out, f, p)
    return out


def inv(c, p=None):
    return pow(c % p, p - 2, p) if p else F(1) / c


def pdivmod(a, b, p=None):
    a, b = trim(a, p), trim(b, p)
    assert b
    q = [0] * max(len(a) - len(b) + 1, 1)
    r = list(a)
    lb = inv(b[-1], p)
    while len(r) >= len(b) and r:
        k = len(r) - len(b)
        c = (r[-1] * lb) % p if p else r[-1] * lb
        q[k] = c
        r = sub(r, [0] * k + scal(c, b, p), p)
    return trim(q, p), r


def ev(a, x, p=None):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v % p if p else v


def deriv(a, p=None):
    return trim([i * a[i] for i in range(1, len(a))], p)


def monic(a, p=None):
    a = trim(a, p)
    return scal(inv(a[-1], p), a, p) if a else a


def pgcd(a, b, p=None):
    a, b = trim(a, p), trim(b, p)
    while b:
        a, b = b, pdivmod(a, b, p)[1]
    return monic(a, p)


X = [0, 1]


def lin(c, p=None):
    return trim([-c, 1], p)


def lagrange(nodes, i, p=None):
    out = [1]
    for j, cj in enumerate(nodes):
        if j != i:
            out = mul(out, scal(inv(nodes[i] - cj, p), lin(cj, p), p), p)
    return out
# --- end helpers ---

m = [-2, 0, 1]
f = [1, 1]
a = [-1, 1]
# x^2 - 2 = (x - 1)(x + 1) - 1
assert m == add(mul(a, f), [-1])
q, r = pdivmod(m, f)
assert q == [-1, 1] and r == [-1]
# (x - 1)(x + 1) + (-1)(x^2 - 2) = 1
assert add(mul(a, f), scal(-1, m)) == [1]
assert pgcd(f, m) == [1]
# (x + 1)(x - 1) = x^2 - 1 reduces to 1 modulo x^2 - 2
assert mul(f, a) == [-1, 0, 1]
assert pdivmod(mul(f, a), m)[1] == [1]
print("ok")
