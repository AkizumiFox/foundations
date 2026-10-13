"""exr-reading-proofs-b1: with x = 1/delta, y = 1/delta + delta/2: |x - y| = delta/2 < delta,
y > x > 0, |x^2 - y^2| = (y - x)(y + x) = (delta/2)(2/delta + delta/2) = 1 + delta^2/4 >= 1.
Both sides are rational functions of delta of low degree; exact agreement at 200 points."""
from fractions import Fraction as Fr
QUOTED = {"eps": 1}
for n in range(1, 41):
    for d in (1, 2, 3, 7, 10):
        delta = Fr(n, d)
        x, y = 1 / delta, 1 / delta + delta / 2
        assert abs(x - y) == delta / 2 < delta
        assert y > x > 0
        assert abs(x * x - y * y) == (y - x) * (y + x) == (delta / 2) * (2 / delta + delta / 2)
        assert (delta / 2) * (2 / delta + delta / 2) == 1 + delta ** 2 / 4 >= QUOTED["eps"]
print("exr-reading-proofs-b1: all quoted values check")
