"""exm-complex-square-root: w^2 = 5 - 12i; |5 - 12i| = 13, x^2 = 9, y^2 = 4, w = +-(3 - 2i); the formula gives x = 3, y = -2."""
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
QUOTED = {"r": 13, "x2": 9, "y2": 4, "w": (3, -2)}
z = G(5, -12)
assert z.abs2() == QUOTED["r"] ** 2
assert (QUOTED["r"] + 5) / 2 == QUOTED["x2"] and (QUOTED["r"] - 5) / 2 == QUOTED["y2"]
w = G(*QUOTED["w"])
assert w * w == z and (-w) * (-w) == z and w.a * w.b == -6
assert (math.sqrt((13 + 5) / 2), -math.sqrt((13 - 5) / 2)) == QUOTED["w"]
print("ok")
