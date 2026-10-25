"""exr-formal-derivative-r1: E(f) = f + f' is additive on random integer polynomials and on
(Z/nZ)[x]; E(f) != 0 for every non-zero f of degree <= 3 over Z/nZ, n <= 6, with E(f)_n = f_n at
n = deg f; E(x)E(x) = x^2 + 2x + 1 and E(x^2) = x^2 + 2x differ in position 0 over Z/nZ, n >= 2."""
QUOTED = {}
from fractions import Fraction as Fr
import itertools, random

random.seed(4405)


def trim(f):
    f = list(f)
    while f and f[-1] == 0:
        f.pop()
    return f


def red(f, n):
    """reduce coefficients mod n (n = 0: no reduction)"""
    return trim([c % n for c in f] if n else f)


def add(f, g, n=0):
    m = max(len(f), len(g))
    return red([(f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(m)], n)


def neg(f, n=0):
    return red([-c for c in f], n)


def mul(f, g, n=0):
    if not f or not g:
        return []
    h = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            h[i + j] += a * b
    return red(h, n)


def scal(a, f, n=0):
    return red([a * c for c in f], n)


def deriv(f, n=0):
    """(f')_k = (k + 1) * f_{k+1}, the multiple computed as repeated addition"""
    out = []
    for k in range(len(f) - 1):
        s = 0
        for _ in range(k + 1):
            s += f[k + 1]
        out.append(s)
    return red(out, n)


def power(f, m, n=0):
    r = [1] if (n != 1) else []
    for _ in range(m):
        r = mul(r, f, n)
    return red(r, n)


def comp(f, g, n=0):
    r = []
    for k, c in enumerate(f):
        r = add(r, scal(c, power(g, k, n), n), n)
    return r


def deg(f):
    return len(trim(f)) - 1 if trim(f) else None  # None = -infinity


def allpolys(n, d):
    for t in itertools.product(range(n), repeat=d + 1):
        yield trim(list(t))


def rnd(d, lo=-5, hi=5):
    return trim([random.randint(lo, hi) for _ in range(d + 1)])

E = lambda f, n=0: add(f, deriv(f, n), n)
for _ in range(200):
    f, g = rnd(random.randint(0, 6)), rnd(random.randint(0, 6))
    assert E(add(f, g)) == add(E(f), E(g))
    if f:
        assert E(f) and E(f)[deg(f)] == f[deg(f)]
for n in range(2, 7):
    for f in allpolys(n, 3):
        if f:
            assert E(f, n) and E(f, n)[deg(f)] == f[deg(f)]
        for h in [[1], [0, 1], [1, 1, 1]]:
            assert E(add(f, red(h, n), n), n) == add(E(f, n), E(red(h, n), n), n)
    Ex = E([0, 1], n)
    assert Ex == [1, 1]
    assert mul(Ex, Ex, n) == red([1, 2, 1], n) and E([0, 0, 1], n) == red([0, 2, 1], n)
    assert mul(Ex, Ex, n)[0] == 1 and E([0, 0, 1], n)[0] == 0
print("ok")
