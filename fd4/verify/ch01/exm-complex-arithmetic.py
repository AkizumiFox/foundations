"""exm-complex-arithmetic and the two Quick checks of Section 1.1 (01-pairs-of-reals.md):
(2 + 3i)(1 - i) = 5 + i; i*i = -1, (i*i)*i = -i, ((i*i)*i)*i = 1; (a + bi)(a - bi) = a^2 + b^2;
check 1: (1 + i)(1 + i) = 2i, Im(3 - 4i) = -4; check 2: i^10 = -1, (1 + i)^4 = -4."""

from fractions import Fraction as Fr

QUOTED = {"(2+3i)(1-i)": (5, 1), "i*i": (-1, 0), "(i*i)*i": (0, -1), "((i*i)*i)*i": (1, 0),
          "(1+i)(1+i)": (0, 2), "Im(3-4i)": -4, "i^10": (-1, 0), "(1+i)^4": (-4, 0)}

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


random.seed(1)
assert (C(2, 3) * C(1, -1)) == C(*QUOTED["(2+3i)(1-i)"])
assert I * I == C(*QUOTED["i*i"])
assert (I * I) * I == C(*QUOTED["(i*i)*i"])
assert ((I * I) * I) * I == C(*QUOTED["((i*i)*i)*i"])
for _ in range(500):
    a, b = rq(), rq()
    p = C(a, b) * C(a, -b)
    assert p == C(a * a + b * b, 0) and a * a + b * b >= 0
assert C(1, 1) * C(1, 1) == C(*QUOTED["(1+i)(1+i)"])
assert C(3, -4).b == QUOTED["Im(3-4i)"]
assert I ** 10 == C(*QUOTED["i^10"])
assert C(1, 1) ** 4 == C(*QUOTED["(1+i)^4"])
# the check's route: i^10 = (i^4)^2 i^2, (1+i)^4 = (2i)^2
assert (I ** 4) ** 2 * I ** 2 == I ** 10 and C(0, 2) ** 2 == C(-4)
print("exm-complex-arithmetic: ok")
