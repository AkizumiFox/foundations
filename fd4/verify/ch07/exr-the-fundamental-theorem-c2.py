"""exr-the-fundamental-theorem-c2: for non-real alpha = a + bi, q = x^2 - 2(Re alpha)x + |alpha|^2
vanishes at alpha; no real polynomial of degree 1 does; f = g q + r with deg r < 2 vanishes at
alpha exactly when r = 0 (so J = <q>); and q has no real root (discriminant -4b^2), so a
factorization into two real linear factors is impossible: q is irreducible over R."""
from fractions import Fraction
import random

QUOTED = {"deg q": 2, "q": r"x^2 - 2(\operatorname{Re} \alpha)x + \abs{\alpha}^2"}


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
    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.a == o.a and s.b == o.b


def pmul(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] += x * y
    return out


def padd(f, g):
    n = max(len(f), len(g))
    return [(f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(n)]


def ev(f, z):
    v = G(0)
    for c in reversed(f):
        v = v * z + c
    return v


random.seed(12)
for _ in range(300):
    a = Fraction(random.randint(-9, 9), random.randint(1, 4))
    b = Fraction(random.choice([-1, 1]) * random.randint(1, 9), random.randint(1, 4))
    alpha = G(a, b)
    q = [a * a + b * b, -2 * a, Fraction(1)]
    assert len(q) - 1 == QUOTED["deg q"] and ev(q, alpha) == 0
    for c in range(-10, 11):                       # x - c, c real, does not vanish at alpha
        assert not ev([Fraction(-c), Fraction(1)], alpha) == 0
    g = [Fraction(random.randint(-5, 5)) for _ in range(random.randint(1, 4))]
    r = [Fraction(random.randint(-3, 3)), Fraction(random.randint(-3, 3))]
    f = padd(pmul(g, q), r)
    assert (ev(f, alpha) == 0) == (r == [0, 0])
    assert q[1] ** 2 - 4 * q[0] * q[2] == -4 * b * b < 0
print("ok")
