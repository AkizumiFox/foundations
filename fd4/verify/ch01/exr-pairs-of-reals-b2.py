"""exr-pairs-of-reals-b2: z^3 - 1 = (z - 1)(1 + z + z^2), z^4 - 1 = (z - 1)(1 + z + z^2 + z^3), zero at i;
(1 + i)^2 = 2i, (1 + i)^3 = -2 + 2i, (1 + i)^4 = -4;
z^4 + 4 = (z - (1 + i))(z^3 + (1 + i) z^2 + 2i z + (-2 + 2i))."""

from fractions import Fraction as Fr

QUOTED = {"w^2": (0, 2), "w^3": (-2, 2), "w^4": (-4, 0)}

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


random.seed(7)
w = C(1, 1)
assert w ** 2 == C(*QUOTED["w^2"]) and w ** 3 == C(*QUOTED["w^3"]) and w ** 4 == C(*QUOTED["w^4"])
assert 1 + I + I ** 2 + I ** 3 == C(0) and I ** 4 - 1 == C(0)
for _ in range(500):
    z = rc()
    assert z ** 3 - 1 == (z - 1) * (1 + z + z ** 2)
    assert z ** 4 - 1 == (z - 1) * (1 + z + z ** 2 + z ** 3)
    assert z ** 4 + 4 == (z - w) * (z ** 3 + w * z ** 2 + C(0, 2) * z + C(-2, 2))
print("exr-pairs-of-reals-b2: ok")
