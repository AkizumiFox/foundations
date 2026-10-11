"""thm-squares-order (Ch 2, Section 2.4): x, y >= 0 gives x <= y iff x^2 <= y^2; the remark's
witnesses (-2, 1) and (1, -2); C2(a)'s surviving direction checked in exr-...-c2;
the Quick check after it: x^2 = 1 iff x = 1 or x = -1; the square-root payoff (checked on squares of a grid)."""
from fractions import Fraction as F

QUOTED = {"(=>) fails": (-2, 1, 4, 1), "(<=) fails": (1, -2, 1, 4)}

pts = [F(k, 8) for k in range(0, 161)]
for x in pts:
    for y in pts:
        assert (x <= y) == (x * x <= y * y)
x, y, x2, y2 = QUOTED["(=>) fails"]
assert x <= y and x * x == x2 > y2 == y * y and y >= 0 and x < 0
x, y, x2, y2 = QUOTED["(<=) fails"]
assert x * x == x2 <= y2 == y * y and x > y and x >= 0 and y < 0
ext = [F(k, 64) for k in range(-256, 257)]
for x in ext:
    assert (x * x == 1) == (x in (1, -1))
    assert (x - 1) * (x + 1) == x * x - 1
# the payoff: for s, t >= 0 (think s = sqrt(a), t = sqrt(b)), s <= t iff s^2 <= t^2
for s_ in [F(k, 4) for k in range(0, 41)]:
    for t_ in [F(k, 4) for k in range(0, 41)]:
        assert (s_ <= t_) == (s_ * s_ <= t_ * t_)
print("thm-squares-order: all quoted values check")
