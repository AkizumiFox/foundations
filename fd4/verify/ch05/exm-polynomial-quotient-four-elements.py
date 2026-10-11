"""exm-polynomial-quotient-four-elements: F_2[x]/<x^2 + x + 1> is a field with four elements,
alpha^2 = alpha + 1, alpha(alpha + 1) = 1, (alpha + 1)^2 = alpha, alpha^3 = 1, the table; R[x]/<x^2 + 1>: [x]^2 = [-1]."""
from fractions import Fraction as F

QUOTED = {"elements": 4, "alpha^3": 1, "m values": (1, 1)}

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

import itertools
p, m = 2, [1, 1, 1]
assert (ev(m, 0, p), ev(m, 1, p)) == QUOTED["m values"]
els = [tuple(trim(list(c), p)) for c in itertools.product(range(2), repeat=2)]
assert len(set(els)) == QUOTED["elements"]
red = lambda f: tuple(pdivmod(list(f), m, p)[1])
a, a1 = (0, 1), (1, 1)
assert red(mul(list(a), list(a), p)) == a1
assert red(mul(list(a), list(a1), p)) == (1,)
assert red(mul(list(a1), list(a1), p)) == a
assert red(mul(mul(list(a), list(a), p), list(a), p)) == (QUOTED["alpha^3"],)
nz = [e for e in els if e]
for e in nz:
    assert sum(1 for f in nz if red(mul(list(e), list(f), p)) == (1,)) == 1
for e, f, g in itertools.product(els, repeat=3):
    assert red(mul(list(e), add(list(f), list(g), p), p)) == red(add(mul(list(e), list(f), p), mul(list(e), list(g), p), p))
# R[x]/<x^2 + 1>: x^2 = (x^2 + 1) - 1
assert pdivmod([0, 0, 1], [1, 0, 1])[1] == [-1]
print("ok")
