"""thm-polynomial-interpolation: the warning (5 + 3x and 5 + 2x + x^2 through (0, 5), (1, 8));
parts (b)-(d) on random data over Q and F_7."""
from fractions import Fraction as F

QUOTED = {"values": (5, 8), "second": "5 + 2x + x^2"}

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

a, b = [5, 3], [5, 2, 1]
assert b == add(a, mul([0, 1], lin(1)))
assert (ev(a, 0), ev(a, 1)) == QUOTED["values"] == (ev(b, 0), ev(b, 1))
import random, itertools
random.seed(2)
for p in (None, 7):
    for _ in range(40):
        n = random.randint(0, 4)
        pool = list(range(p)) if p else list(range(-8, 9))
        nodes = random.sample(pool, n + 1)
        ys = [random.randint(-5, 5) for _ in nodes]
        P = []
        for i, y in enumerate(ys):
            P = add(P, scal(y, lagrange(nodes, i, p), p), p)
        assert len(P) - 1 <= n
        assert all(ev(P, c, p) == (y % p if p else y) for c, y in zip(nodes, ys))
        q = trim([random.randint(-4, 4) for _ in range(n + 1)], p)
        rebuilt = []
        for i, c in enumerate(nodes):
            rebuilt = add(rebuilt, scal(ev(q, c, p), lagrange(nodes, i, p), p), p)
        assert rebuilt == q
# uniqueness by exhaustion over F_5 with 3 nodes: exactly one polynomial of degree <= 2 per value triple
p = 5
for ys in itertools.product(range(p), repeat=3):
    sols = [c for c in itertools.product(range(p), repeat=3)
            if all(ev(list(c), x, p) == y for x, y in zip((0, 1, 3), ys))]
    assert len(sols) == 1
print("ok")
