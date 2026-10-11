"""lem-reals-nth-root: for sample a > 0 and n, the constants of the proof work.
m = min(1, a) in S; M = max(1, a) an upper bound; for s with s^n < a,
h = min(1, (a - s^n)/(2n(s + 1)^(n-1))) gives (s + h)^n - s^n <= h n (s + 1)^(n-1) and (s + h)^n < a;
for s with s^n > a, h = (s^n - a)/(n s^(n-1)) gives 0 < h < s and s^n - (s - h)^n <= h n s^(n-1),
so (s - h)^n >= a. Also cube root of 8 is 2, fourth root of 4 is sqrt 2 ((sqrt2)^4 = 4)."""
from fractions import Fraction as Fr
import random

QUOTED = {"h_low": r"h \coloneqq \min\Bigl\{ 1, \frac{a - s^n}{2n(s + 1)^{n-1}} \Bigr\}",
          "h_high": r"h \coloneqq \frac{s^n - a}{n s^{n-1}}",
          "cbrt8": r"\sqrt[3]{8} = 2", "root4_4": r"\sqrt[4]{4} = \sqrt 2"}

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
random.seed(7)

def rq(lo, hi):
    return Fr(random.randint(int(lo * 1000), int(hi * 1000)), 1000)

for _ in range(3000):
    n = random.randint(1, 7)
    a = rq(0.001, 20)
    m, M = min(Fr(1), a), max(Fr(1), a)
    assert m > 0 and m ** n <= m <= a
    y = M + rq(0.001, 3)
    assert y ** n >= y > M >= a
    s = rq(0.001, 4)
    if s ** n < a:
        h = min(Fr(1), (a - s ** n) / (2 * n * (s + 1) ** (n - 1)))
        assert h > 0
        assert (s + h) ** n - s ** n <= h * n * (s + 1) ** (n - 1)
        assert (s + h) ** n <= s ** n + (a - s ** n) / 2 < a
    elif s ** n > a:
        h = (s ** n - a) / (n * s ** (n - 1))
        assert 0 < h < s / n <= s
        assert s ** n - (s - h) ** n <= h * n * s ** (n - 1) == s ** n - a
        assert (s - h) ** n >= a
    t = s + rq(0.001, 2)
    assert s ** n < t ** n                       # part (a)
assert 2 ** 3 == 8 and (S2 * S2) * (S2 * S2) == 4
print("ok")
