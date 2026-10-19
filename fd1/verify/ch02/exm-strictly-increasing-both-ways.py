"""exm-strictly-increasing-both-ways (Ch 2, Section 2.4): 3x - 5 strictly increasing on a grid;
h(-1) = 1, h(0) = 0 for h(x) = x^2; the fold after the warning: |h|/h is 1 for h > 0 and -1 for h < 0;
the warning: 6 | n implies n even (n = 6k = 2(3k)), and the converse breaks at n = 4;
the Quick check after it: the converse of x > 2 => x^2 > 4 breaks at x = -3."""
from fractions import Fraction as F

QUOTED = {"h(-1)": 1, "h(0)": 0, "converse break n": 4, "quick check x": -3}

pts = [F(k, 4) for k in range(-40, 41)]
assert all(3 * x - 5 < 3 * y - 5 for x in pts for y in pts if x < y)
assert (-1) ** 2 == QUOTED["h(-1)"] and 0 ** 2 == QUOTED["h(0)"] and not QUOTED["h(-1)"] < QUOTED["h(0)"]
for h in [F(k, 7) for k in range(-50, 51) if k != 0]:
    assert abs(h) / h == (1 if h > 0 else -1)
# warning: 6 | n => n even, on a range, via n = 6k = 2(3k)
for k in range(-200, 201):
    n = 6 * k
    assert n == 2 * (3 * k) and n % 2 == 0
n = QUOTED["converse break n"]
assert n % 2 == 0 and n % 6 != 0
# Quick check
x = QUOTED["quick check x"]
assert x * x == 9 and x * x > 4 and not x > 2
assert all(x * x > 4 for x in pts if x > 2)
print("exm-strictly-increasing-both-ways: all quoted values check")
