"""exr-interpolation-and-congruences-b3: (a) the addition and multiplication tables of
F_2[x]/<x^2 + x + 1>; (b) the product identity (a + bx)(c + dx) = (ac - bd) + (ad + bc)x + bd(x^2 + 1) on random rationals."""
from fractions import Fraction as F

QUOTED = {"elements": 4}

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

import itertools, random
p, m = 2, [1, 1, 1]
els = [[], [1], [0, 1], [1, 1]]
assert len(els) == QUOTED["elements"]
red = lambda f: pdivmod(f, m, p)[1]
mt = {(i, j): els.index(red(mul(els[i], els[j], p))) for i in range(4) for j in range(4)}
assert [mt[(2, j)] for j in range(4)] == [0, 2, 3, 1] and [mt[(3, j)] for j in range(4)] == [0, 3, 1, 2]
at = {(i, j): els.index(add(els[i], els[j], p)) for i in range(4) for j in range(4)}
assert [at[(1, j)] for j in range(4)] == [1, 0, 3, 2] and [at[(2, j)] for j in range(4)] == [2, 3, 0, 1]
random.seed(6)
for _ in range(50):
    a, b, c, d = (F(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4))
    assert mul([a, b], [c, d]) == add([a * c - b * d, a * d + b * c], scal(b * d, [1, 0, 1]))
print("ok")
