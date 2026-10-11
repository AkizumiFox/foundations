"""exr-triangle-inequality-a1 (c): z = 3, w = 4i: z conj w = -12i, cross term 0, |z + w|^2 = 25 <= 49 = (3 + 4)^2."""
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
QUOTED = {"zwbar": (0, -12), "lhs": 25, "rhs": 49}
z, w = G(3), G(0, 4)
u = z * w.conj()
assert (u.a, u.b) == QUOTED["zwbar"]
assert (z + w).abs2() == z.abs2() + 2 * u.a + w.abs2() == QUOTED["lhs"]
assert (3 + 4) ** 2 == QUOTED["rhs"] and QUOTED["lhs"] <= QUOTED["rhs"]
print("ok")
