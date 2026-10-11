"""exr-polar-form-c1: (c + is)^3 = (c^3 - 3cs^2) + (3c^2 s - s^3) i, and with c^2 + s^2 = 1:
cos 3t = 4c^3 - 3c, sin 3t = 3s - 4s^3 (exact on random rationals; numeric on angles)."""
from fractions import Fraction as Fr
import math, random

QUOTED = {"re": "c^3 - 3cs^2", "im": "3c^2 s - s^3", "cos3": "4c^3 - 3c", "sin3": "3s - 4s^3"}

# --- exact arithmetic in Q(sqrt2, sqrt3)(i) ---


class Q:
    """a + b*sqrt2 + c*sqrt3 + d*sqrt6 with rational a, b, c, d (exact)."""
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(Fr(x) for x in (a, b, c, d))
    def __add__(s, o):
        o = q(o); return Q(*(x + y for x, y in zip(s.v, o.v)))
    __radd__ = __add__
    def __neg__(s): return Q(*(-x for x in s.v))
    def __sub__(s, o): return s + (-q(o))
    def __rsub__(s, o): return q(o) - s
    def __mul__(s, o):
        o = q(o); a, b, c, d = s.v; e, f, g, h = o.v
        return Q(a*e + 2*b*f + 3*c*g + 6*d*h,
                 a*f + b*e + 3*c*h + 3*d*g,
                 a*g + c*e + 2*b*h + 2*d*f,
                 a*h + d*e + b*g + c*f)
    __rmul__ = __mul__
    def __eq__(s, o): return s.v == q(o).v
    def __hash__(s): return hash(s.v)
    def f(s): return float(s.v[0]) + float(s.v[1])*2**0.5 + float(s.v[2])*3**0.5 + float(s.v[3])*6**0.5
    def __repr__(s): return "Q%s" % (s.v,)


def q(x): return x if isinstance(x, Q) else Q(x)


class C:
    """complex number re + im*i with Q parts."""
    def __init__(s, re=0, im=0): s.re, s.im = q(re), q(im)
    def __add__(s, o): o = c(o); return C(s.re + o.re, s.im + o.im)
    __radd__ = __add__
    def __neg__(s): return C(-s.re, -s.im)
    def __sub__(s, o): return s + (-c(o))
    def __rsub__(s, o): return c(o) - s
    def __mul__(s, o):
        o = c(o); return C(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    __rmul__ = __mul__
    def __pow__(s, n):
        r = C(1)
        for _ in range(n): r = r * s
        return r
    def conj(s): return C(s.re, -s.im)
    def __eq__(s, o): o = c(o); return s.re == o.re and s.im == o.im
    def z(s): return complex(s.re.f(), s.im.f())
    def __repr__(s): return "C(%r, %r)" % (s.re, s.im)


def c(x): return x if isinstance(x, C) else C(x)


I = C(0, 1)
S2 = Q(0, 1)       # sqrt 2
S3 = Q(0, 0, 1)    # sqrt 3

# --- checks ---
random.seed(1)
for _ in range(500):
    cc, ss = Fr(random.randint(-99, 99), 37), Fr(random.randint(-99, 99), 41)
    z = C(cc, ss) ** 3
    assert z.re == cc**3 - 3*cc*ss**2 and z.im == 3*cc**2*ss - ss**3
    sq = C(cc, ss) ** 2
    assert sq == C(cc**2 - ss**2, 2*cc*ss)
    # substitution identities as polynomial identities
    assert cc**3 - 3*cc*(1 - cc**2) == 4*cc**3 - 3*cc
    assert 3*(1 - ss**2)*ss - ss**3 == 3*ss - 4*ss**3
for k in range(100):
    t = k * 0.0731 - 3
    assert abs(math.cos(3*t) - (4*math.cos(t)**3 - 3*math.cos(t))) < 1e-12
    assert abs(math.sin(3*t) - (3*math.sin(t) - 4*math.sin(t)**3)) < 1e-12
print("ok")
