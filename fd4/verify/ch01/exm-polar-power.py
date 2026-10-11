"""exm-polar-power: (sqrt3 + i)^6 = -64, by hand (sqrt3 + i)^2 = 2(1 + sqrt3 i),
(1 + sqrt3 i)^3 = -8; Check: (1 + i)^8 = 16, (sqrt2)^8 = 16, (1 + i)^2 = 2i, (2i)^4 = 16."""
from fractions import Fraction as Fr

QUOTED = {"power": -64, "check": 16}

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
z = C(S3, 1)
assert z ** 6 == QUOTED["power"]
assert z ** 2 == 2 * C(1, S3) and C(1, S3) ** 3 == -8 and C(1, S3) * C(-2, 2 * S3) == -8
assert C(2) ** 6 * -1 == -64                                 # 2^6 e^{i pi}
assert C(1, 1) ** 8 == QUOTED["check"] and C(1, 1) ** 2 == C(0, 2) and C(0, 2) ** 4 == 16
assert S2 * S2 * S2 * S2 * S2 * S2 * S2 * S2 == 16
assert C(S2) * C(Fr(1, 2) * S2, Fr(1, 2) * S2) == C(1, 1)    # 1 + i = sqrt2 e^{i pi/4}
print("ok")
