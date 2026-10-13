"""exr-reading-proofs-b2: y^3 - x^3 = (y - x)(y^2 + xy + x^2);
y^2 + xy + x^2 = (y + x/2)^2 + 3x^2/4, which is 0 only at x = y = 0; so x < y gives
y^2 + xy + x^2 > 0 and x^3 < y^3. Identities of degree <= 3 in two variables, checked on
a 25 x 25 rational grid."""
from fractions import Fraction as Fr
QUOTED = {}
pts = [Fr(n, 2) for n in range(-12, 13)]
for x in pts:
    for y in pts:
        q = y * y + x * y + x * x
        assert y ** 3 - x ** 3 == (y - x) * q
        assert q == (y + x / 2) ** 2 + 3 * x * x / 4 >= 0
        if q == 0:
            assert x == 0 and y == 0
        if x < y:
            assert q > 0 and x ** 3 < y ** 3
print("exr-reading-proofs-b2: all quoted values check")
