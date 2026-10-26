"""lem-complex-polynomial-lipschitz: the quick check (A = 1, R = 2 for x^2 + 1, L = 8 for M = 4);
the growth and Lipschitz bounds on random points (floats, with a margin)."""
from fractions import Fraction as F

QUOTED = {"A": 1, "R": 2, "L": 8}

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

class G:
    """a + b i with a, b in a field of Fractions (or any ring supporting + - *)."""
    def __init__(self, a, b=0):
        self.a, self.b = a, b
    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s):
        return G(-s.a, -s.b)
    def __sub__(s, o):
        return s + (-(o if isinstance(o, G) else G(o)))
    def __rsub__(s, o):
        return G(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.a == o.a and s.b == o.b
    def conj(s):
        return G(s.a, -s.b)
    def abs2(s):
        return s.a * s.a + s.b * s.b
    def __pow__(s, k):
        out = G(1)
        for _ in range(k):
            out = out * s
        return out
    def __repr__(s):
        return f"({s.a} + {s.b} i)"

I = G(0, 1)


def gev(coeffs, z):
    v = G(0)
    for c in reversed(coeffs):
        v = v * z + c
    return v

import random, math
coef = [1, 0, 1]
A = sum(abs(c) for c in coef[:-1]); R = max(1, 2 * A / abs(coef[-1]))
L = sum(j * abs(coef[j]) * 4 ** (j - 1) for j in range(1, 3))
assert (A, R, L) == (QUOTED["A"], QUOTED["R"], QUOTED["L"])
random.seed(7)
ev_c = lambda cs, z: sum(c * z ** j for j, c in enumerate(cs))
for _ in range(300):
    n = random.randint(1, 5)
    cs = [complex(random.randint(-5, 5), random.randint(-5, 5)) for _ in range(n)] + [complex(random.choice([-3, -1, 1, 2]), random.randint(-2, 2))]
    A = sum(abs(c) for c in cs[:-1]); R = max(1, 2 * A / abs(cs[-1]))
    r = R * (1 + 3 * random.random()); th = 2 * math.pi * random.random()
    z = r * complex(math.cos(th), math.sin(th))
    assert abs(ev_c(cs, z)) >= 0.5 * abs(cs[-1]) * abs(z) ** n * (1 - 1e-9)
    M = 3 * random.random()
    L = sum(j * abs(cs[j]) * M ** (j - 1) for j in range(1, n + 1))
    z = M * random.random() * complex(math.cos(th), math.sin(th)); w = M * random.random() * complex(math.sin(th), math.cos(th))
    assert abs(ev_c(cs, z) - ev_c(cs, w)) <= L * abs(z - w) * (1 + 1e-9) + 1e-12
print("ok")
