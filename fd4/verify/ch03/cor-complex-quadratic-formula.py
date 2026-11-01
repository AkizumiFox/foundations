"""cor-complex-quadratic-formula: the completing-the-square identity on random values, and the worked example z^2 - (3 + i)z + (2 + 2i) = 0: discriminant -2i, d = 1 - i from the formula, solutions 2 and 1 + i."""
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
QUOTED = {"disc": (0, -2), "d": (1, -1), "sols": [(2, 0), (1, 1)]}
random.seed(9)
for _ in range(2000):
    a, b, c, z = (G(random.randint(-9, 9), random.randint(-9, 9)) for _ in range(4))
    assert 4 * a * (a * z * z + b * z + c) == (2 * a * z + b) * (2 * a * z + b) - (b * b - 4 * a * c)
b, c = -G(3, 1), G(2, 2)
disc = b * b - 4 * c
assert disc == G(*QUOTED["disc"])
# formula of prp-complex-square-roots on -2i: a = 0, b = -2, r = 2
assert (math.sqrt((2 + 0) / 2), -math.sqrt((2 - 0) / 2)) == QUOTED["d"]
d = G(*QUOTED["d"]); assert d * d == disc
sols = [(-b + d) / 2, (-b - d) / 2]
assert sols == [G(*s) for s in QUOTED["sols"]]
for s in sols: assert s * s + b * s + c == 0
assert sols[0] + sols[1] == G(3, 1) and sols[0] * sols[1] == G(2, 2)
print("ok")
