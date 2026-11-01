"""exr-conjugate-and-modulus-b1: (3 - 2i)(4 + i) = 14 - 5i; (1 + 2i)/(2 - i) = i;
|(3 + 4i)(5 - 12i)| = 5 * 13 = 65; 1/(1 + i) = 1/2 - (1/2) i."""

from fractions import Fraction
from fractions import Fraction as Fr

QUOTED = {"(a)": (14, -5), "(b)": (0, 1), "|5-12i|": 13, "(c)": 65, "Re": Fraction(1, 2), "Im": Fraction(-1, 2)}

import random


class C:
    """Exact complex numbers a + bi with rational parts (pairs, as in def-complex-numbers)."""

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.a, -self.b)

    def __sub__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self + (-o)

    def __rsub__(self, o):
        return C(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        r = C(1)
        for _ in range(n):
            r = r * self
        return r

    def conj(self):
        return C(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + self.b * self.b

    def inv(self):
        n = self.norm2()
        assert n != 0
        return C(self.a / n, -self.b / n)

    def __truediv__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self * o.inv()

    def __eq__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"({self.a}) + ({self.b})i"


I = C(0, 1)


def rq():
    return Fr(random.randint(-60, 60), random.randint(1, 12))


def rc():
    return C(rq(), rq())


assert C(3, -2) * C(4, 1) == C(*QUOTED["(a)"])
assert C(1, 2) * C(2, 1) == C(0, 5) and C(1, 2) / C(2, -1) == C(*QUOTED["(b)"])
assert C(5, -12).norm2() == QUOTED["|5-12i|"] ** 2 == 169
p = C(3, 4) * C(5, -12)
assert p.norm2() == QUOTED["(c)"] ** 2 and 5 * 13 == QUOTED["(c)"]
q = C(1) / C(1, 1)
assert q.a == QUOTED["Re"] and q.b == QUOTED["Im"]
print("exr-conjugate-and-modulus-b1: ok")
