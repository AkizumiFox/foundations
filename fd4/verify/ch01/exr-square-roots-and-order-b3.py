"""exr-square-roots-and-order-b3: d = i sqrt(4ac - b^2) squares to b^2 - 4ac (random real a, b, c with negative discriminant, floating point), and the example z^2 - 2z + 5: discriminant -16, q = 4, roots 1 +- 2i."""
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
QUOTED = {"disc": -16, "q": 4, "roots": [(1, 2), (1, -2)]}
random.seed(10)
for _ in range(5000):
    a, b, c = (random.uniform(-10, 10) for _ in range(3))
    D = b * b - 4 * a * c
    if D >= 0 or abs(a) < 1e-3: continue
    q = math.sqrt(-D)
    for sg in (1, -1):
        z = complex(-b, sg * q) / (2 * a)
        assert abs(a * z * z + b * z + c) < 1e-7 * (1 + abs(a) + abs(b) + abs(c)) * (1 + abs(z)) ** 2
    assert complex(-b, q) / (2 * a) == (complex(-b, -q) / (2 * a)).conjugate()
assert (-2) ** 2 - 4 * 1 * 5 == QUOTED["disc"] and math.sqrt(-QUOTED["disc"]) == QUOTED["q"]
for r in QUOTED["roots"]:
    z = G(*r); assert z * z - 2 * z + 5 == 0
print("ok")
