"""exr-formal-derivative-r2: f(conj z) = conj f(z) for random real (rational) coefficients and
Gaussian-rational z; conjugation is additive, multiplicative, fixes 1 and the reals."""
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

class G:
    def __init__(s, a, b=0):
        s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o):
        return G(s.a + o.a, s.b + o.b)
    def __mul__(s, o):
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def conj(s):
        return G(s.a, -s.b)
    def __eq__(s, o):
        return s.a == o.a and s.b == o.b


def ev(f, z):
    r, pw = G(0), G(1)
    for c in f:
        r = r + G(c) * pw
        pw = pw * z
    return r


for _ in range(300):
    f = [Fr(random.randint(-9, 9), random.randint(1, 5)) for _ in range(random.randint(1, 7))]
    z = G(Fr(random.randint(-9, 9), random.randint(1, 4)), Fr(random.randint(-9, 9), random.randint(1, 4)))
    w = G(random.randint(-5, 5), random.randint(-5, 5))
    assert ev(f, z.conj()) == ev(f, z).conj()
    assert (z + w).conj() == z.conj() + w.conj() and (z * w).conj() == z.conj() * w.conj()
assert G(1).conj() == G(1) and G(Fr(3, 7)).conj() == G(Fr(3, 7))
print("ok")
