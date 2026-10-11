"""exr-square-roots-and-order-c2 (c): in Z/3Z the squares are [0], [1], and -[1] = [2] is not a square; 3 * [1] = [0]. (b): the formula on -1 gives x = 0, y = 1."""
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
QUOTED = {"squares": {0, 1}, "minus_one": 2}
assert {(k * k) % 3 for k in range(3)} == QUOTED["squares"]
assert (-1) % 3 == QUOTED["minus_one"] and QUOTED["minus_one"] not in QUOTED["squares"]
assert (1 + 1 + 1) % 3 == 0
r = math.hypot(-1, 0)
assert (math.sqrt((r - 1) / 2), math.sqrt((r + 1) / 2)) == (0, 1)
print("ok")
