"""exr-triangle-inequality-b2: the two expansions, and |z - w| = |1 - conj(z) w| when |z| = 1 (checked on Gaussian rationals on the unit circle, from Pythagorean triples)."""
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
QUOTED = {}
random.seed(5)
for _ in range(2000):
    z = G(random.randint(-9, 9), random.randint(-9, 9)); w = G(random.randint(-9, 9), random.randint(-9, 9))
    zw, zbw = z * w.conj(), z.conj() * w
    assert (z - w).abs2() == (z.abs2() - zw - zbw + w.abs2()).a and (z.abs2() - zw - zbw + w.abs2()).b == 0
    one = 1 - z.conj() * w
    assert one.conj() == 1 - z * w.conj()
    assert G(one.abs2()) == 1 - zw - zbw + G(z.abs2() * w.abs2())
for (p, q, r) in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (1, 0, 1), (0, 1, 1)]:
    for sa in (1, -1):
        for sb in (1, -1):
            z = G(Fr(sa * p, r), Fr(sb * q, r))
            assert z.abs2() == 1
            for _ in range(50):
                w = G(Fr(random.randint(-30, 30), 7), Fr(random.randint(-30, 30), 3))
                assert (z - w).abs2() == (1 - z.conj() * w).abs2()
print("ok")
