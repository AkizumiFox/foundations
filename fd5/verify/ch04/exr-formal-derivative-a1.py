"""exr-formal-derivative-a1: (x^5 - x)' = 5x^4 - 1 over Q and -1 (= 4) over F_5; over Z/6Z, a
cubic with leading coefficient [2] has deg f' <= 1, all of 1, 0, -infinity occur, witnesses
[2]x^3 + x^2 -> [2]x, [2]x^3 + x -> 1, [2]x^3 -> 0; (x^2)' = 0 over F_2."""
QUOTED = {"(a)": "5x^4 - 1"}
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

assert deriv([0, -1, 0, 0, 0, 1]) == [-1, 0, 0, 0, 5]
assert deriv([0, -1, 0, 0, 0, 1], 5) == [4]
degs = set()
for t in itertools.product(range(6), repeat=3):
    f = list(t) + [2]
    d = deg(deriv(f, 6))
    degs.add(d)
    assert d is None or d <= 1
assert degs == {1, 0, None}
assert deriv([0, 0, 1, 2], 6) == [0, 2]
assert deriv([0, 1, 0, 2], 6) == [1]
assert deriv([0, 0, 0, 2], 6) == []
assert deriv([0, 0, 1], 2) == []
print("ok")
