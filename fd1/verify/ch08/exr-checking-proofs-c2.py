"""exr-checking-proofs-c2 (Ch 5, Section 5.6): exact arithmetic in Q(sqrt2, sqrt3):
(sqrt2 + sqrt3)^2 = 5 + 2 sqrt6; sqrt2 * sqrt3 = sqrt6; sqrt2 * sqrt2 = 2;
with r = sqrt2 + sqrt3: (r - sqrt2)^2 = 3 = r^2 - 2 r sqrt2 + 2, and 2 r sqrt2 = r^2 - 1;
r > 0."""
from fractions import Fraction as F

class Q23:
    """a + b sqrt2 + c sqrt3 + d sqrt6 with rational coefficients."""
    def __init__(s, a=0, b=0, c=0, d=0):
        s.v = tuple(F(t) for t in (a, b, c, d))
    def __add__(s, o): return Q23(*[x + y for x, y in zip(s.v, o.v)])
    def __sub__(s, o): return Q23(*[x - y for x, y in zip(s.v, o.v)])
    def __mul__(s, o):
        a, b, c, d = s.v; e, f, g, h = o.v
        return Q23(a*e + 2*b*f + 3*c*g + 6*d*h,
                   a*f + b*e + 3*c*h + 3*d*g,
                   a*g + c*e + 2*b*h + 2*d*f,
                   a*h + d*e + b*g + c*f)
    def __eq__(s, o): return s.v == o.v

one, s2, s3, s6 = Q23(1), Q23(0, 1), Q23(0, 0, 1), Q23(0, 0, 0, 1)
QUOTED = {}
r = s2 + s3
assert r * r == Q23(5) + Q23(2) * s6
assert s2 * s3 == s6
assert s2 * s2 == Q23(2)
assert (r - s2) * (r - s2) == Q23(3)
assert r * r - Q23(2) * r * s2 + Q23(2) == Q23(3)
assert Q23(2) * r * s2 == r * r - one
assert 2 ** 0.5 + 3 ** 0.5 > 0
print("exr-checking-proofs-c2: all quoted values check")
