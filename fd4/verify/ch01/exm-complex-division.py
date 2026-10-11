"""exm-complex-division and the second Quick check of Section 1.2:
1/(3 + 4i) = 3/25 - (4/25)i; (5 + i)/(1 - i) = (5 + i)(1 + i)/2 = (4 + 6i)/2 = 2 + 3i;
|(1 + i)(1 - i)| = 2 (= sqrt2 * sqrt2); 1/i = -i."""

from fractions import Fraction
from fractions import Fraction as Fr

QUOTED = {"1/(3+4i)": (Fraction(3, 25), Fraction(-4, 25)), "(5+i)(1+i)": (4, 6), "(5+i)/(1-i)": (2, 3),
          "(1+i)(1-i)": 2, "1/i": (0, -1)}

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


assert C(1) / C(3, 4) == C(*QUOTED["1/(3+4i)"]) and C(3, 4) * C(3, -4) == C(25)
assert C(5, 1) * C(1, 1) == C(*QUOTED["(5+i)(1+i)"]) and C(1, -1).norm2() == 2
assert C(5, 1) / C(1, -1) == C(*QUOTED["(5+i)/(1-i)"]) and C(2, 3) * C(1, -1) == C(5, 1)
assert C(1, 1) * C(1, -1) == C(QUOTED["(1+i)(1-i)"])
assert C(1, 1).norm2() * C(1, -1).norm2() == 4  # (sqrt2 sqrt2)^2 = 4, so sqrt2 sqrt2 = 2
assert C(1) / I == C(*QUOTED["1/i"]) and I * C(0, -1) == C(1)
print("exm-complex-division: ok")
