"""exm-strictly-increasing-both-ways (Ch 2, Section 2.4): 3x - 5 strictly increasing on a grid;
h(-1) = 1, h(0) = 0 for h(x) = x^2; the warning after it: |h|/h is 1 for h > 0 and -1 for h < 0."""
from fractions import Fraction as F

QUOTED = {"h(-1)": 1, "h(0)": 0}

pts = [F(k, 4) for k in range(-40, 41)]
assert all(3 * x - 5 < 3 * y - 5 for x in pts for y in pts if x < y)
assert (-1) ** 2 == QUOTED["h(-1)"] and 0 ** 2 == QUOTED["h(0)"] and not QUOTED["h(-1)"] < QUOTED["h(0)"]
for h in [F(k, 7) for k in range(-50, 51) if k != 0]:
    assert abs(h) / h == (1 if h > 0 else -1)
print("exm-strictly-increasing-both-ways: all quoted values check")
