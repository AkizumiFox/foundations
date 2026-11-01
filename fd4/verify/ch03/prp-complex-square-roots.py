"""prp-complex-square-roots (Section 1.4): the formula w = x + yi squares to z on many random z (floating point), the try-it-first instance 3 + 4i (r = 5, x^2 = 4, y^2 = 1, w = 2 + i), the quartic x^4 - 3x^2 - 4 = 0 at x = 2, the quick check (roots of -4 and 2i), and the check after the not-orderable proof, ((1 + i)/sqrt 2)^2 = i."""
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
QUOTED = {"3+4i": (5, 4, 1, (2, 1)), "-4": (0, 2), "2i": (1, 1)}
def formula(a, b):
    r = math.hypot(a, b); s = 1 if b >= 0 else -1
    return math.sqrt((r + a) / 2), s * math.sqrt((r - a) / 2), r
random.seed(8)
for _ in range(20000):
    a, b = random.uniform(-50, 50), random.uniform(-50, 50)
    if random.random() < 0.1: b = 0.0
    if random.random() < 0.05: a = 0.0
    if a == 0 and b == 0: continue
    x, y, r = formula(a, b)
    assert abs((x * x - y * y) - a) < 1e-8 * (1 + abs(a)) and abs(2 * x * y - b) < 1e-8 * (1 + abs(b))
    assert x >= 0 and (x, y) != (0.0, 0.0)
x, y, r = formula(3, 4)
assert (r, x * x, y * y) == QUOTED["3+4i"][:3] and (x, y) == QUOTED["3+4i"][3]
w = G(2, 1); assert w * w == G(3, 4) and 2 ** 4 - 3 * 2 ** 2 - 4 == 0
x, y, r = formula(-4, 0); assert (x, y) == QUOTED["-4"] and G(0, 2) * G(0, 2) == G(-4)
x, y, r = formula(0, 2); assert (x, y) == QUOTED["2i"] and G(1, 1) * G(1, 1) == G(0, 2)
# ((1 + i)/sqrt 2)^2 = (1 + i)^2 / 2 = i
assert (G(1, 1) * G(1, 1)) / 2 == I
# exactly two roots: u^2 = z iff u = +-w, on a grid of Gaussian integers
for z in [G(3, 4), G(-4), G(0, 2), G(5, -12), G(-3, 4)]:
    roots = [G(p, q) for p in range(-5, 6) for q in range(-5, 6) if G(p, q) * G(p, q) == z]
    assert len(roots) == 2 and roots[0] == -roots[1]
print("ok")
