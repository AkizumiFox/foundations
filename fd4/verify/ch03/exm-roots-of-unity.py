"""exm-roots-of-unity: n = 6 values (omega = 1/2 + sqrt3/2 i), omega^2 = -1/2 + sqrt3/2 i,
omega^3 = -1, omega^4 = -omega, omega^5 = -omega^2, all sixth powers 1, sum 0; numeric match
with e^{2 pi i k/6}. Check (cube roots of unity): 1, -1/2 +- sqrt3/2 i, z^3 - 1 = (z - 1)(z^2 + z + 1),
quadratic formula with d = sqrt3 i."""
from fractions import Fraction as Fr
import cmath, math

QUOTED = {"six": [r"1, \quad \tfrac12 + \tfrac{\sqrt3}{2}i, \quad -\tfrac12 + \tfrac{\sqrt3}{2}i, \quad -1,",
                  r"\quad -\tfrac12 - \tfrac{\sqrt3}{2}i, \quad \tfrac12 - \tfrac{\sqrt3}{2}i"],
          "omega^2": r"\omega^2 = \bigl(\tfrac12 + \tfrac{\sqrt 3}{2} i\bigr)^2 = \tfrac14 - \tfrac34 + \tfrac{\sqrt 3}{2} i = -\tfrac12 + \tfrac{\sqrt 3}{2} i",
          "cube": r"\( 1 \) and \( -\tfrac12 \pm \tfrac{\sqrt 3}{2} i \)"}

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
w = C(h, h * S3)
six = [C(1), w, C(-h, h * S3), C(-1), C(-h, -h * S3), C(h, -h * S3)]
for k, v in enumerate(six):
    assert w ** k == v and v ** 6 == 1
    assert abs(v.z() - cmath.exp(2j * math.pi * k / 6)) < 1e-12
assert w ** 4 == -w and w ** 5 == -(w ** 2)
total = C(0)
for v in six: total = total + v
assert total == 0
cube = [C(1), C(-h, h * S3), C(-h, -h * S3)]
for v in cube:
    assert v ** 3 == 1 and (v - 1) * (v * v + v + 1) == v ** 3 - 1
assert (w ** 2) == cube[1] and cube[1].conj() == cube[2] and cube[1] * cube[2] == 1
d = C(0, S3)
assert d * d == -3 and (C(-1) + d) * C(h) == cube[1] and (C(-1) - d) * C(h) == cube[2]
print("ok")
