"""exm-special-angles: each value satisfies its defining equation exactly, has positive
imaginary part where (T5) is used, matches cos/sin numerically, and pi/6 = pi/2 - pi/3."""
from fractions import Fraction as Fr
import math

QUOTED = {"e^{i pi}": r"e^{i\pi} = -1", "e^{i pi/2}": r"e^{i\pi/2} = i",
          "e^{i pi/3}": r"e^{i\pi/3} = \tfrac12 + \tfrac{\sqrt 3}{2} i",
          "e^{i pi/6}": r"e^{i\pi/6} = \tfrac{\sqrt 3}{2} + \tfrac12 i",
          "e^{i pi/4}": r"e^{i\pi/4} = \tfrac{1}{\sqrt 2} + \tfrac{1}{\sqrt 2} i"}

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
h = Fr(1, 2)
E = {  # e^{i theta} for theta = pi * key
    Fr(1): C(-1, 0), Fr(1, 2): C(0, 1), Fr(1, 3): C(h, h * S3),
    Fr(1, 6): C(h * S3, h), Fr(1, 4): C(h * S2, h * S2),   # 1/sqrt2 = sqrt2/2
}
assert E[Fr(1)] ** 2 == 1                     # (i) u^2 = e^{2 pi i} = 1
assert (C(1) - 1) * (C(1) + 1) == C(1) ** 2 - 1
assert E[Fr(1, 2)] ** 2 == -1                 # (ii) u^2 = e^{i pi}
u = E[Fr(1, 3)]
assert u ** 3 == -1                           # (iii) u^3 = e^{i pi}
assert u * u - u + 1 == C(0)
assert (C(0, 1) * C(S3)) ** 2 == -3           # d = sqrt3 i squares to b^2 - 4ac = -3
assert u == C(h, h * S3) and C(h, -h * S3) * C(h, -h * S3) - C(h, -h * S3) + 1 == C(0)
assert E[Fr(1, 6)] == E[Fr(1, 2)] * E[Fr(1, 3)].conj()   # (iv)
assert Fr(1, 6) == Fr(1, 2) - Fr(1, 3)
w = E[Fr(1, 4)]
assert w ** 2 == C(0, 1)                      # (v) square root of i
assert Q(h) == (h * S2) * (h * S2) * 1 and (h * S2) * S2 == 1   # sqrt(1/2) = 1/sqrt2 = sqrt2/2
for t, v in E.items():                        # numeric agreement with cos, sin
    z = v.z()
    assert abs(z - complex(math.cos(math.pi * t), math.sin(math.pi * t))) < 1e-12
    assert 0 < t < 1 and v.im.f() > 0 or t == 1
print("ok")
