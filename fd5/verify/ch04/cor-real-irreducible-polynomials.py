"""cor-real-irreducible-polynomials: the irreducible real polynomials have degree 1, or degree 2
with no real root. Checked: for non-real z = a + bi (Gaussian rationals), q = (x - z)(x - conj z)
= x^2 - 2(Re z)x + |z|^2 has real coefficients, no real root (discriminant -4b^2 < 0), and divides
every real multiple q h in R[x] with zero remainder; every monic integer cubic with coefficients
in [-4, 4] has a real root (sign change), so no real cubic in that range is irreducible."""
from fractions import Fraction
import random

QUOTED = {"degrees of the irreducibles": (1, 2),
          "q": r"x^2 - 2(\operatorname{Re} z)x + \abs{z}^2"}


class G:
    """a + b i with Fraction parts."""
    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __neg__(s):
        return G(-s.a, -s.b)
    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.a == o.a and s.b == o.b
    def conj(s):
        return G(s.a, -s.b)


def pmul(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] = out[i + j] + x * y
    return out


def pdivmod(f, g):
    """division in Q[x] (coefficients low degree first), g monic or not."""
    f, q = [Fraction(c) for c in f], [Fraction(0)] * max(len(f) - len(g) + 1, 1)
    while len(f) >= len(g) and any(f):
        k, c = len(f) - len(g), f[-1] / g[-1]
        q[k] = c
        f = [f[i] - (c * g[i - k] if i >= k else 0) for i in range(len(f))]
        while f and f[-1] == 0:
            f.pop()
    return q, f


def ev(f, z):
    v = G(0) if isinstance(z, G) else 0
    for c in reversed(f):
        v = v * z + c
    return v


random.seed(5)
for _ in range(300):
    a = Fraction(random.randint(-9, 9), random.randint(1, 4))
    b = Fraction(random.choice([-1, 1]) * random.randint(1, 9), random.randint(1, 4))
    z = G(a, b)
    q = pmul([-z, G(1)], [-z.conj(), G(1)])
    assert all(c.b == 0 for c in q)                       # real coefficients
    q = [c.a for c in q]
    assert q == [a * a + b * b, -2 * a, 1]                # x^2 - 2(Re z)x + |z|^2
    assert q[1] ** 2 - 4 * q[2] * q[0] == -4 * b * b < 0  # no real root
    h = [Fraction(random.randint(-5, 5)) for _ in range(random.randint(1, 4))] + [Fraction(1)]
    p = pmul(q, h)
    assert ev(p, z) == 0 and ev(p, z.conj()) == 0
    quo, rem = pdivmod(p, q)
    assert rem == [] and quo == h and len(p) - 1 == len(h) + 1   # deg p = 2 only if h constant
for c2 in range(-4, 5):
    for c1 in range(-4, 5):
        for c0 in range(-4, 5):
            f = [c0, c1, c2, 1]
            M = 1 + abs(c0) + abs(c1) + abs(c2)
            assert ev(f, -M) < 0 < ev(f, M)               # a real root, so a real linear factor
assert QUOTED["degrees of the irreducibles"] == (1, 2)
print("ok")
