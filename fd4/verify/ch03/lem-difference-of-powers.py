"""lem-difference-of-powers: z^n - w^n = (z - w) sum_{k=0}^{n-1} z^k w^(n-1-k) for n = 1..12,
and the induction step (z^n - w^n) w + z^n (z - w) = z^(n+1) - w^(n+1)."""

from fractions import Fraction as Fr

QUOTED = {"the identity, checked for n = 1, ..., 12 on random Gaussian rationals": True}

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


random.seed(5)
for _ in range(150):
    z, w = rc(), rc()
    for n in range(1, 13):
        S = C(0)
        for k in range(n):
            S = S + z ** k * w ** (n - 1 - k)
        assert z ** n - w ** n == (z - w) * S
        assert (z ** n - w ** n) * w + z ** n * (z - w) == z ** (n + 1) - w ** (n + 1)
        G = C(0)
        for k in range(n):
            G = G + z ** k
        assert z ** n - 1 == (z - 1) * G
print("lem-difference-of-powers: ok")
