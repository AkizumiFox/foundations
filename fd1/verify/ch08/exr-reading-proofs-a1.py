"""exr-reading-proofs-a1: a^2 - b^2 = (a - b)(a + b); for a, b > 0 with a^2 = b^2, a + b > 0
and a = b."""
from fractions import Fraction as Fr
QUOTED = {}
pts = [Fr(n, d) for n in range(-12, 13) for d in (1, 2, 3)]
for a in pts:
    for b in pts:
        assert a * a - b * b == (a - b) * (a + b)
        if a > 0 and b > 0:
            assert a + b > 0
            if a * a == b * b:
                assert a == b
print("exr-reading-proofs-a1: all quoted values check")
