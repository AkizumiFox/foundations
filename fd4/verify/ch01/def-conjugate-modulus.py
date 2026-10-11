"""def-conjugate-modulus examples and the first Quick check of Section 1.2:
conj(3 + 4i) = 3 - 4i, |3 + 4i| = 5 (5 >= 0, 5^2 = 25); conj i = -i, |i| = 1; |0| = 0;
-2i: conj 2i, |.| = 2; 1 - i: conj 1 + i, |.|^2 = 2; N(2) = 4, N(1 + 1) = 4 > N(1) + N(1) = 2;
|1 + i|^2 = 2 has no rational square root (checked: no p/q with small q squares to 2)."""

from fractions import Fraction as Fr

QUOTED = {"|3+4i|": 5, "|i|": 1, "|-2i|": 2, "|1-i|^2": 2, "N(2)": 4, "N(1)+N(1)": 2}

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


def sqrt_exact(x):
    """the non-negative rational square root of x if it exists (by uniqueness: y >= 0, y^2 = x)"""
    from math import isqrt
    x = Fr(x)
    p, q = x.numerator, x.denominator
    if p < 0:
        return None
    sp, sq = isqrt(p), isqrt(q)
    return Fr(sp, sq) if sp * sp == p and sq * sq == q else None


z = C(3, 4)
assert z.conj() == C(3, -4) and sqrt_exact(z.norm2()) == QUOTED["|3+4i|"] and 5 ** 2 == 25
assert I.conj() == C(0, -1) and sqrt_exact(I.norm2()) == QUOTED["|i|"]
assert sqrt_exact(C(0).norm2()) == 0
assert C(0, -2).conj() == C(0, 2) and sqrt_exact(C(0, -2).norm2()) == QUOTED["|-2i|"]
assert C(1, -1).conj() == C(1, 1) and C(1, -1).norm2() == QUOTED["|1-i|^2"]
assert sqrt_exact(2) is None
N = lambda t: C(t).norm2()
assert N(2) == QUOTED["N(2)"] and N(1 + 1) == 4 > N(1) + N(1) == QUOTED["N(1)+N(1)"]
print("def-conjugate-modulus: ok")
