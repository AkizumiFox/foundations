"""exr-triangle-inequality-b3: |z| <= |Re z| + |Im z| <= sqrt 2 |z| (via squares), the identity 2(x^2 + y^2) - (|x| + |y|)^2 = (|x| - |y|)^2, and the equality cases z = 1, z = 1 + i."""
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
QUOTED = {"eq1": (1, 1), "eq2": (2, 2)}
random.seed(6)
for _ in range(3000):
    x, y = Fr(random.randint(-99, 99), random.randint(1, 9)), Fr(random.randint(-99, 99), random.randint(1, 9))
    s = abs(x) + abs(y)
    assert x * x + y * y <= s * s <= 2 * (x * x + y * y)
    assert 2 * (x * x + y * y) - s * s == (abs(x) - abs(y)) ** 2
assert (1, abs(1) + abs(0)) == QUOTED["eq1"]
assert (1 + 1, 2 * (1 + 1) // 2) == QUOTED["eq2"] and (1 + 1) ** 2 == 2 * (1 * 1 + 1 * 1)
print("ok")
