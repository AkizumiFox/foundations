"""def-formal-derivative: formula (M) for (a x^n)' over several rings; f' is a polynomial
(vanishes from index N on); 2 * 1 = 0 in F_2 so (x^2)' = 0; the warning (coefficient of x in
(x^2)' over Q is 2, while 1 * f_1 = 0; sum (k f_k) x^k = x f'); the quick check
(x^3 + x^2 + x + 1)' = x^2 + 1 over F_2."""
QUOTED = {"check": "x^2 + 1", "warning coefficient": 2}
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

# (M): (a x^n)' = (n.a) x^(n-1), n >= 1; constants -> 0
for n in [0, 2, 3, 4, 5, 6, 12]:
    for a in range(n if n else 7):
        for e in range(0, 8):
            mono = red([0] * e + [a], n)
            expect = red([0] * (e - 1) + [e * a], n) if e >= 1 else []
            assert deriv(mono, n) == expect
# f' vanishes from index N on (N = deg f)
for _ in range(200):
    f = rnd(random.randint(0, 8))
    assert len(deriv(f)) <= max(len(f) - 1, 0)
assert deriv([0, 0, 1], 2) == []
# warning
f = [0, 0, 1]
assert deriv(f)[1] == 2 and 1 * f[1] == 0
for _ in range(200):
    f = rnd(random.randint(0, 7))
    assert trim([k * c for k, c in enumerate(f)]) == mul([0, 1], deriv(f))
# quick check over F_2
assert deriv([1, 1, 1, 1], 2) == [1, 0, 1]
print("ok")
