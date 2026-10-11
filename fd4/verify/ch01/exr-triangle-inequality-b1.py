"""exr-triangle-inequality-b1: the equality case on random values (equality iff z conj w is a non-negative real), and the example z = 1 + i, w = 2 + 2i: z conj w = 4, |3 + 3i| = 3 sqrt 2 = sqrt 2 + 2 sqrt 2."""
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
QUOTED = {"zwbar": 4, "lhs_sq": 18}
z, w = G(1, 1), G(2, 2)
assert z * w.conj() == G(QUOTED["zwbar"])
assert (z + w).abs2() == QUOTED["lhs_sq"] and z.abs2() == 2 and w.abs2() == 8
assert abs(math.sqrt(18) - 3 * math.sqrt(2)) < 1e-12 and abs(math.sqrt(8) - 2 * math.sqrt(2)) < 1e-12
random.seed(4)
for _ in range(3000):
    z = G(random.randint(-6, 6), random.randint(-6, 6)); w = G(random.randint(-6, 6), random.randint(-6, 6))
    u = z * w.conj()
    # equality |z+w| = |z|+|w|  iff  (z+w).abs2() = z.abs2() + w.abs2() + 2 sqrt(z.abs2() w.abs2())  iff  u.a = |u|
    eq = (u.a >= 0 and u.a * u.a == u.abs2())
    nonneg_real = (u.b == 0 and u.a >= 0)
    assert eq == nonneg_real
    lhs = math.sqrt((z + w).abs2()); rhs = math.sqrt(z.abs2()) + math.sqrt(w.abs2())
    assert (abs(lhs - rhs) < 1e-9) == nonneg_real
print("ok")
