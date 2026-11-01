"""lem-real-part-at-most-modulus (Section 1.3): the examples after the lemma (3 - 4i, 2, -1) and the quick check (2i); and the three inequalities on random Gaussian rationals, compared through squares."""
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
QUOTED = {"3-4i": (3, 4, 5, 7), "2": (2, 0, 2, 2), "-1": (-1, 1), "2i": (0, 2, 2)}
def mod(z): return math.sqrt(z.abs2())
z = G(3, -4)
assert (abs(z.a), abs(z.b), mod(z), abs(z.a) + abs(z.b)) == QUOTED["3-4i"]
z = G(2)
assert (abs(z.a), abs(z.b), mod(z), abs(z.a) + abs(z.b)) == QUOTED["2"]
z = G(-1); assert (z.a, mod(z)) == QUOTED["-1"] and z.a < mod(z)
z = G(0, 2); assert (z.a, z.b, mod(z)) == QUOTED["2i"]
random.seed(1)
for _ in range(5000):
    u = G(Fr(random.randint(-99, 99), random.randint(1, 9)), Fr(random.randint(-99, 99), random.randint(1, 9)))
    x, y, m2 = u.a, u.b, u.abs2()
    assert x * x <= m2 and y * y <= m2            # |x|^2 <= |u|^2, |y|^2 <= |u|^2
    assert (abs(x) + abs(y)) ** 2 >= m2            # (|x| + |y|)^2 >= |u|^2
    assert x <= 0 or x * x <= m2                   # Re u <= |u|
print("ok")
