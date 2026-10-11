"""thm-complex-triangle-inequality (Section 1.3): the identity |z + w|^2 = |z|^2 + 2 Re(z conj w) + |w|^2, the squared inequality on random values, the quick check (|3 + 4i| + |-3 + 4i| = 10 >= 8 = |8i|), the warning (z = w = i) and the strictness witness (z = 1, w = -1)."""
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
QUOTED = {"check": (5, 5, 8), "warning": (-4, 4), "witness": (0, 2)}
random.seed(2)
def rnd(): return G(Fr(random.randint(-50, 50), random.randint(1, 7)), Fr(random.randint(-50, 50), random.randint(1, 7)))
for _ in range(3000):
    z, w = rnd(), rnd()
    u = z * w.conj()
    assert (z + w).abs2() == z.abs2() + 2 * u.a + w.abs2()
    assert w * z.conj() == u.conj() and u + u.conj() == G(2 * u.a)
    assert u.abs2() == z.abs2() * w.abs2()
    # |z+w| <= |z| + |w| via squares: need 2 Re u <= 2|u|
    assert u.a <= 0 or u.a * u.a <= u.abs2()
    assert math.sqrt((z + w).abs2()) <= math.sqrt(z.abs2()) + math.sqrt(w.abs2()) + 1e-9
a, b, s = G(3, 4), G(-3, 4), G(3, 4) + G(-3, 4)
assert (math.isqrt(int(a.abs2())), math.isqrt(int(b.abs2())), math.isqrt(int(s.abs2()))) == QUOTED["check"]
assert s == G(0, 8) and a.abs2() == 25 and s.abs2() == 64
z = w = I
assert ((z + w) * (z + w)).a == QUOTED["warning"][0] and ((z + w) * (z + w)).b == 0
assert (z + w).abs2() == QUOTED["warning"][1]
z, w = G(1), G(-1)
assert ((z + w).abs2(), 1 + 1) == (QUOTED["witness"][0], QUOTED["witness"][1])
print("ok")
