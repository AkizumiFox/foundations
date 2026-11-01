"""prp-formal-derivative-zero: k * 1 = 0 in F_p iff p | k; over Q, deg f' = deg f - 1 and f' = 0
only for constants; over F_2, F_3, F_5: f' = 0 iff f_k = 0 for p not dividing k iff f = g o x^p
(exhaustive, degree <= 6 resp. 4); x^2 + 1 = (x + 1) o x^2 over F_2; x^6 + 2x^3 + 1 =
(x^2 + 2x + 1) o x^3 over F_3 with derivative 0 (6 * 1 = 0); warning: (x^p)' = 0,
(x^p - x)' = -1; quick check (x^5 + x)' = 1 over F_5."""
QUOTED = {"F2": "x^2 + 1 = (x + 1) \\circ x^2", "F3": "x^6 + 2x^3 + 1 = (x^2 + 2x + 1) \\circ x^3"}
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

for p in [2, 3, 5, 7]:
    for k in range(0, 60):
        assert ((k * 1) % p == 0) == (k % p == 0)
# char 0
for _ in range(300):
    f = rnd(random.randint(1, 7))
    if deg(f) is None or deg(f) < 1:
        continue
    assert deg(deriv(f)) == deg(f) - 1
for d in range(0, 4):
    for t in itertools.product(range(-2, 3), repeat=d + 1):
        f = trim(list(t))
        assert (deriv(f) == []) == (deg(f) is None or deg(f) == 0)
# char p
for p, D in [(2, 6), (3, 5), (5, 4)]:
    pow_cache = {}
    for f in allpolys(p, D):
        z = deriv(f, p) == []
        cond = all(c == 0 for k, c in enumerate(f) if k % p)
        assert z == cond
        if cond:
            g = trim([f[p * j] for j in range(len(f)) if p * j < len(f)])
            assert comp(g, [0] * p + [1], p) == f
        # if f = g o x^p for some g of small degree, then cond holds
    for g in allpolys(p, 2):
        h = comp(g, [0] * p + [1], p)
        assert deriv(h, p) == []
assert comp([1, 1], [0, 0, 1], 2) == [1, 0, 1]
h = comp([1, 2, 1], [0, 0, 0, 1], 3)
assert h == [1, 0, 0, 2, 0, 0, 1] and deriv(h, 3) == [] and (6 * 1) % 3 == 0
for p in [2, 3, 5, 7]:
    assert deriv([0] * p + [1], p) == []
    assert deriv(red([0, -1] + [0] * (p - 2) + [1], p), p) == red([-1], p)
assert deriv([0, 1, 0, 0, 0, 1], 5) == [1]
print("ok")
