"""exr-pairs-of-reals-c1 (c): in any commutative ring with j^2 = -1,
(a + bj)(c + dj) = (ac - bd) + (ad + bc) j. Checked in C (j = i) and in the 2x2 rational matrices
with J = [[0,-1],[1,0]] (a different field-like model containing a square root of -1)."""

from fractions import Fraction as Fr

QUOTED = {"product": "(ac - bd) + (ad + bc) j"}

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


def mm(X, Y):
    return [[sum(X[r][k] * Y[k][s] for k in range(2)) for s in range(2)] for r in range(2)]


def lin(a, b, J):
    return [[a + b * J[0][0], b * J[0][1]], [b * J[1][0], a + b * J[1][1]]]


J = [[0, -1], [1, 0]]
assert mm(J, J) == [[-1, 0], [0, -1]]
random.seed(9)
for _ in range(500):
    a, b, c, d = (rq() for _ in range(4))
    assert C(a, b) * C(c, d) == C(a * c - b * d, a * d + b * c)
    assert mm(lin(a, b, J), lin(c, d, J)) == lin(a * c - b * d, a * d + b * c, J)
print("exr-pairs-of-reals-c1: ok")
