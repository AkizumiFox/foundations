"""exr-universal-elimination-b3 (Ch 4, Section 4.3): (a - b)^2 = a^2 - 2ab + b^2, hence
a^2 + b^2 >= 2ab; and (a + b)^2 >= 0 gives a^2 + b^2 >= -2ab. Identities of degree 2 in two
variables are checked on a 30 x 30 grid of exact rationals (enough to force them)."""
from fractions import Fraction as Fr

QUOTED = {"(a-b)^2 expanded": "(a - b)^2 = a^2 - 2ab + b^2"}
minus = lambda a, b: a * a - 2 * a * b + b * b   # the expansion QUOTED above
plus = lambda a, b: a * a + 2 * a * b + b * b
grid = [Fr(k, 7) for k in range(-15, 15)]
for a in grid:
    for b in grid:
        assert (a - b) ** 2 == minus(a, b)
        assert (a + b) ** 2 == plus(a, b)
        assert a * a + b * b >= 2 * a * b          # from (a - b)^2 >= 0
        assert a * a + b * b >= -2 * a * b         # from (a + b)^2 >= 0
print("exr-universal-elimination-b3: all quoted values check")
