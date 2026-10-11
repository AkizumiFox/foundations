"""thm-formal-derivative-rules: linearity, product rule and power rule checked exhaustively on
(Z/nZ)[x] of degree <= 2 for n <= 6, and on random integer polynomials; the quick check
((x + 1)^3)' = 0 over F_3 with (x + 1)^3 = x^3 + 1."""
QUOTED = {"check expansion": "x^3 + 1"}
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

for n in range(2, 7):
    P = list(allpolys(n, 2))
    for f in P:
        for g in P:
            assert deriv(add(f, g, n), n) == add(deriv(f, n), deriv(g, n), n)
            assert deriv(mul(f, g, n), n) == add(mul(deriv(f, n), g, n), mul(f, deriv(g, n), n), n)
        for a in range(n):
            assert deriv(scal(a, f, n), n) == scal(a, deriv(f, n), n)
        for m in range(1, 6):
            lhs = deriv(power(f, m, n), n)
            rhs = scal(m, mul(power(f, m - 1, n), deriv(f, n), n), n)
            assert lhs == rhs
    for c in range(n):
        for m in range(1, 7):
            assert deriv(power(red([-c, 1], n), m, n), n) == scal(m, power(red([-c, 1], n), m - 1, n), n)
for _ in range(300):
    f, g = rnd(random.randint(0, 6)), rnd(random.randint(0, 6))
    assert deriv(mul(f, g)) == add(mul(deriv(f), g), mul(f, deriv(g)))
assert power([1, 1], 3, 3) == [1, 0, 0, 1]
assert deriv(power([1, 1], 3, 3), 3) == [] and scal(3, power([1, 1], 2, 3), 3) == []
print("ok")
