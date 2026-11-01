"""exr-square-roots-and-order-b1: square roots of -3 + 4i are +-(1 + 2i) (x^2 = 1, y^2 = 4); z^2 + 2z + 4 - 4i = 0 has discriminant -12 + 16i = 4(-3 + 4i), d = 2 + 4i, solutions 2i and -2 - 2i."""
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
QUOTED = {"root": (1, 2), "disc": (-12, 16), "d": (2, 4), "sols": [(0, 2), (-2, -2)]}
z = G(-3, 4)
assert z.abs2() == 25 and (5 - 3) / 2 == 1 and (5 + 3) / 2 == 4
w = G(*QUOTED["root"]); assert w * w == z
b, c = G(2), G(4, -4)
disc = b * b - 4 * c
assert disc == G(*QUOTED["disc"]) == 4 * z
d = G(*QUOTED["d"]); assert d * d == disc and d == 2 * w
sols = [(-b + d) / 2, (-b - d) / 2]
assert sols == [G(*s) for s in QUOTED["sols"]]
for s in sols: assert s * s + b * s + c == 0
print("ok")
