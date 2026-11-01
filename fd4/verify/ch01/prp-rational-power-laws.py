"""prp-rational-power-laws (05): (a)-(f) checked exactly on bases c^60 (all roots with denominators | 60 rational)."""
from fractions import Fraction as F

QUOTED = {}
L = 60
rs = [F(p, q) for p in range(-6, 7) for q in (1, 2, 3, 4, 5) ]


def rp(c, r):
    """(c^L)^r for r with denominator dividing L: equals c^(L r)."""
    e = r * L
    assert e.denominator == 1
    return c ** int(e)


for ca in [F(1, 2), F(3, 2), F(2)]:
    for cb in [F(2, 3), F(5, 4), F(3)]:
        for r in rs:
            for s in rs:
                # (b) by the definition (root, then integer power), base a = ca^3600
                M = 3600
                ar = (ca ** (M // r.denominator)) ** r.numerator          # a^r = (n-th root of a)^m
                # q-th root of a^r: ar = (ca^(M r / q))^q, exponent integral since r.denominator*q | 3600
                lhs = (ca ** int(F(M) * r / s.denominator)) ** s.numerator  # (a^r)^s
                assert (ca ** int(F(M) * r / s.denominator)) ** s.denominator == ar
                rs_ = r * s
                rhs = (ca ** (M // rs_.denominator)) ** rs_.numerator      # a^(rs)
                assert lhs == rhs
                assert rp(ca, r + s) == rp(ca, r) * rp(ca, s)
                if ca ** L > 1 and r < s:
                    assert rp(ca, r) < rp(ca, s)
            assert rp(ca * cb, r) == rp(ca, r) * rp(cb, r)
            assert rp(ca, r) > 0
            if ca < cb and r > 0:
                assert rp(ca, r) < rp(cb, r)
print("ok")
