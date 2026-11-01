"""exr-the-fundamental-theorem-a1: (c) for p = x^2 + 1: rho = 2, S_0 = S(-2, -2, 4), m = 0,
-i in S_1 = S(-2, -2, 2) and in S_2 = S(-1, -2, 1); |p| >= |2ab| >= 2 on S(-2, -2, 1) (exact on a rational grid)."""
from fractions import Fraction as F

QUOTED = {"rho": 2, "S_0": (-2, -2, 4), "S_1": (-2, -2, 2), "S_2": (-1, -2, 1), "bound": 2}

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

coef = [1, 0, 1]
A, an = 1, 1
R = max(1, F(2 * A, an)); rho = max(R, F(2 * abs(ev(coef, 0)), an))
assert rho == QUOTED["rho"] and (-rho, -rho, 2 * rho) == QUOTED["S_0"]
inside = lambda z, sq: sq[0] <= z.a <= sq[0] + sq[2] and sq[1] <= z.b <= sq[1] + sq[2]
mi = G(0, -1)
assert gev(coef, mi) == 0
assert inside(mi, QUOTED["S_0"]) and inside(mi, QUOTED["S_1"]) and inside(mi, QUOTED["S_2"])
assert QUOTED["S_1"] == (-2, -2, 2) and QUOTED["S_2"] == (-2 + 1, -2, 1)
N = 40
for i in range(N + 1):
    for j in range(N + 1):
        z = G(F(-2) + F(i, N), F(-2) + F(j, N))
        v = gev(coef, z)
        assert v.abs2() >= QUOTED["bound"] ** 2 and abs(v.b) == abs(2 * z.a * z.b)
print("ok")
