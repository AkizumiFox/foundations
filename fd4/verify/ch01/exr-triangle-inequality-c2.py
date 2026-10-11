"""exr-triangle-inequality-c2: |1 - conj(z) w|^2 - |z - w|^2 = (1 - |z|^2)(1 - |w|^2), and the strict inequality inside the unit disc on random Gaussian rationals."""
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
random.seed(7)
for _ in range(5000):
    z = G(Fr(random.randint(-99, 99), 100), Fr(random.randint(-99, 99), 100))
    w = G(Fr(random.randint(-99, 99), 100), Fr(random.randint(-99, 99), 100))
    d = (1 - z.conj() * w).abs2() - (z - w).abs2()
    assert d == (1 - z.abs2()) * (1 - w.abs2())
    if z.abs2() < 1 and w.abs2() < 1:
        assert d > 0
print("ok")
