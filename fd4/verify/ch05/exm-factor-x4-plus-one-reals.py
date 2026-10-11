"""exm-factor-x4-plus-one-reals: with s = sqrt 2 handled symbolically (s^2 = 2):
w_1 = (s/2)(1 + i) squares to i, w_2 = (s/2)(1 - i) to -i; (x - w_1)(x - conj w_1) = x^2 - s x + 1;
the product of the real quadratics is x^4 + 1; also the quick check x^3 - 1 = (x - 1)(x - z_+)(x - z_-) with sqrt 3."""
from fractions import Fraction as F

QUOTED = {"half": F(1, 2), "x^3 - 1 quadratic": "x^2 + x + 1", "3/4": F(3, 4)}

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

class Q2:
    """a + b r with r^2 = D."""
    D = 2
    def __init__(s, a, b=0):
        s.a, s.b = F(a), F(b)
    def __add__(s, o):
        o = o if isinstance(o, Q2) else Q2(o); return Q2(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q2(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, Q2) else Q2(o)))
    def __rsub__(s, o): return Q2(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, Q2) else Q2(o); return Q2(s.a * o.a + s.D * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __eq__(s, o):
        o = o if isinstance(o, Q2) else Q2(o); return s.a == o.a and s.b == o.b
r2 = Q2(0, 1)
half_r2 = Q2(0, F(1, 2))
assert half_r2 * half_r2 == Q2(QUOTED["half"])
w1 = G(half_r2, half_r2); w2 = G(half_r2, -half_r2)
assert w1 * w1 == G(Q2(0), Q2(1)) and w2 * w2 == G(Q2(0), Q2(-1))
assert w2 == w1.conj()
assert w1 + w1.conj() == G(r2, Q2(0)) and w1 * w1.conj() == G(Q2(1), Q2(0))
qm = [Q2(1), -r2, Q2(1)]; qp = [Q2(1), r2, Q2(1)]
assert mul(qm, qp) == [Q2(1), Q2(0), Q2(0), Q2(0), Q2(1)]
# x^4 + 1 = (x^2 - i)(x^2 + i)
assert [G(1)] == [I * I * (-1)]
# the quick check: z_pm = (-1 pm i r3)/2 with r3^2 = 3
Q2.D = 3
for sgn in (1, -1):
    z = G(Q2(F(-1, 2)), Q2(0, F(sgn, 2)))
    assert z * z + z + 1 == G(Q2(0), Q2(0))
assert mul([-1, 1], [1, 1, 1]) == [-1, 0, 0, 1]
assert F(1, 2) ** 2 + QUOTED["3/4"] == 1
print("ok")
