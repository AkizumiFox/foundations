"""exm-formal-derivatives: (x^4 - 2x^3 + 2x - 1)' = 4x^3 - 6x^2 + 2 over Q (coefficients 2, 0,
-6, 4); a' = 0, x' = 1, (x - c)' = 1; (x^3 + x)' = 1 over F_3; (x^2)' = 0 over F_2;
([2]x^3 + x)' = 1 over Z/6Z (degree 3 -> 0, 3 * [2] = [6] = [0]); (x^n)' = n x^(n-1) over Z;
the hook: 2(x - 1) vanishes at 1."""
QUOTED = {"(i)": "4x^3 - 6x^2 + 2", "(i) coeffs": [2, 0, -6, 4], "(iv)": "[6] x^2 + 1 = 1"}
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

f = [-1, 2, 0, -2, 1]
assert deriv(f) == [2, 0, -6, 4]
for n in [0, 2, 3, 6, 7]:
    for a in range(-3, 4):
        assert deriv(red([a], n), n) == []
        assert deriv(red([-a, 1], n), n) == red([1], n)
    assert deriv([0, 1], n) == red([1], n)
assert deriv([0, 1, 0, 1], 3) == [1]
assert deriv([0, 0, 1], 2) == []
g = [0, 1, 0, 2]
assert deriv(g, 6) == [1] and deg(g) == 3 and deg(deriv(g, 6)) == 0 and (3 * 2) % 6 == 0
for n in range(1, 12):
    assert deriv([0] * n + [1]) == [0] * (n - 1) + [n]
# hook: ((x-1)^2)' = 2(x - 1), value 0 at 1
d = deriv(power([-1, 1], 2))
assert d == [-2, 2] and sum(c * 1 ** k for k, c in enumerate(d)) == 0
print("ok")
