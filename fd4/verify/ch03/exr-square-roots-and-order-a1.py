"""exr-square-roots-and-order-a1 (b): the formula on z = -4: r = 4, s = 1, x = 0, y = 2; roots +-2i. (a): 1 and -1 have equal squares."""
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
QUOTED = {"r": 4, "s": 1, "x": 0, "y": 2}
a, b = -4, 0
r = math.hypot(a, b); s = 1 if b >= 0 else -1
assert (r, s, math.sqrt((r + a) / 2), s * math.sqrt((r - a) / 2)) == (QUOTED["r"], QUOTED["s"], QUOTED["x"], QUOTED["y"])
assert G(0, 2) * G(0, 2) == G(-4) and G(0, -2) * G(0, -2) == G(-4)
assert G(1) * G(1) == G(-1) * G(-1)
print("ok")
