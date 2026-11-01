"""cor-complex-triangle-variants (Section 1.3): the quick check z = 5, w = 3i (|z| - |w| = 2, |z - w| = |z + w| = sqrt 34, 4 <= 34), and (a)-(c) on random values."""
from fractions import Fraction as Fr
import math, random


class G:
    """Exact complex numbers a + bi with rational a, b."""
    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, G) else G(o); return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return G(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, G) else G(o)))
    def __rsub__(s, o): return G(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def conj(s): return G(s.a, -s.b)
    def abs2(s): return s.a * s.a + s.b * s.b
    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        n = s * o.conj(); d = o.abs2(); return G(n.a / d, n.b / d)
    def __eq__(s, o): o = o if isinstance(o, G) else G(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"({s.a}+{s.b}i)"


I = G(0, 1)
QUOTED = {"diff": 2, "sq": 34}
z, w = G(5), G(0, 3)
assert math.isqrt(int(z.abs2())) - math.isqrt(int(w.abs2())) == QUOTED["diff"]
assert (z - w).abs2() == QUOTED["sq"] == (z + w).abs2() and 2 * 2 <= QUOTED["sq"]
random.seed(3)
m = lambda v: math.sqrt(v.abs2())
for _ in range(2000):
    zs = [G(random.randint(-20, 20), random.randint(-20, 20)) for _ in range(random.randint(1, 6))]
    z, w = zs[0], G(random.randint(-20, 20), random.randint(-20, 20))
    assert abs(m(z) - m(w)) <= m(z - w) + 1e-9
    assert m(z) - m(w) <= m(z + w) + 1e-9
    tot = G(0)
    for t in zs: tot = tot + t
    assert m(tot) <= sum(m(t) for t in zs) + 1e-9
print("ok")
