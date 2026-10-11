"""exr-the-least-upper-bound-property-r4: recursion q_0 = p - 1 (p the integer part of x),
L = max(q, x - 1/(k+1)), n = (integer part of 2/(x - L)) + 1, m = integer part of n x, q' = (m - 1)/n;
then L < x - 2/n < q' <= x - 1/n < x; strictly increasing; x - 1/(k+1) < q_{k+1} < x.
Run exactly in Q(sqrt 2) for x = sqrt 2, -sqrt 2, 7/3, 0, 3 - 2 sqrt 2."""
from fractions import Fraction as F
from math import floor
QUOTED = {"chain": "L < x - 2/n < (m-1)/n <= x - 1/n < x"}

class Q2:
    """a + b sqrt 2 with rational a, b; exact order."""
    def __init__(s, a, b=0): s.a, s.b = F(a), F(b)
    def __add__(s, o): o = c(o); return Q2(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q2(-s.a, -s.b)
    def __sub__(s, o): return s + (-c(o))
    def __rsub__(s, o): return c(o) - s
    def __mul__(s, o): o = c(o); return Q2(s.a*o.a + 2*s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def inv(s):
        d = s.a*s.a - 2*s.b*s.b; assert d != 0
        return Q2(s.a/d, -s.b/d)
    def __truediv__(s, o): return s * c(o).inv()
    def __rtruediv__(s, o): return c(o) * s.inv()
    def sign(s):
        a, b = s.a, s.b
        if b == 0: return (a > 0) - (a < 0)
        if a == 0: return (b > 0) - (b < 0)
        if (a > 0) == (b > 0): return 1 if a > 0 else -1
        # opposite signs: compare a^2 with 2 b^2
        t = a*a - 2*b*b
        return (1 if a > 0 else -1) if t > 0 else (1 if b > 0 else -1)
    def __lt__(s, o): return (s - o).sign() < 0
    def __le__(s, o): return (s - o).sign() <= 0
    def __gt__(s, o): return (s - o).sign() > 0
    def __eq__(s, o): return (s - o).sign() == 0
def c(o): return o if isinstance(o, Q2) else Q2(o)
def ipart(y):
    m = floor(float(y.a) + float(y.b) * 2 ** 0.5)
    while c(m) > y: m -= 1
    while c(m + 1) <= y: m += 1
    assert c(m) <= y < c(m + 1)
    return m
def mx(u, v): return u if u >= v else v

for x in [Q2(0, 1), Q2(0, -1), Q2(F(7, 3)), Q2(0), Q2(3, -2)]:
    q = c(ipart(x) - 1)
    assert q < x
    seq = [q]
    for k in range(15):
        L = mx(q, x - F(1, k + 1))
        assert L < x
        n = ipart(2 / (x - L)) + 1
        assert n > 0 and c(F(2, n)) < x - L
        m = ipart(n * x)
        qn = c(F(m - 1, n))
        assert L < x - F(2, n) < qn <= x - F(1, n) < x
        assert qn > q and x - F(1, k + 1) < qn < x
        q = qn
        seq.append(q)
    assert all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
print("ok")
