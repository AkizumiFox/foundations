"""exr-formal-derivative-b2: (x^n)^(k) = (P(n, k) * 1) x^(n - k) for k <= n and 0 for k > n;
(f^(k))_j = P(j + k, k) f_(j + k); over F_p (p = 2, 3, 5) f^(p) = 0 for all f of degree <= 7
(p = 2, 3) resp. <= 6 (p = 5); P(4, 3) = 24, so (x^4)''' = 0 over F_3."""
QUOTED = {"P(4,3)": 24}
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

def P(n, k):
    r = 1
    for i in range(k):
        r *= (n - i)
    return r


def dk(f, k, n=0):
    for _ in range(k):
        f = deriv(f, n)
    return f


for n in range(0, 10):
    x = [0] * n + [1]
    for k in range(0, 13):
        if k <= n:
            assert dk(x, k) == [0] * (n - k) + [P(n, k)]
        else:
            assert dk(x, k) == []
for _ in range(100):
    f = rnd(random.randint(0, 8))
    for k in range(0, 5):
        d = dk(f, k)
        for j in range(0, 10):
            v = (f[j + k] if j + k < len(f) else 0) * P(j + k, k)
            assert (d[j] if j < len(d) else 0) == v
for p, D in [(2, 7), (3, 7), (5, 6)]:
    for f in allpolys(p, D):
        assert dk(f, p, p) == []
    for j in range(0, 40):
        assert P(j + p, p) % p == 0
assert P(4, 3) == 24 and dk([0, 0, 0, 0, 1], 3, 3) == []
print("ok")
