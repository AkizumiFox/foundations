"""exm-two-sided-inverses (Ch 6, Section 6.5): 3x - 2, 1/x, x|x| and their inverses."""
from fractions import Fraction as F
import math
QUOTED = {"a(x)": "3x - 2", "a inverse": "(y + 2)/3"}
pts = [F(k, 7) for k in range(-70, 71)]
a = lambda x: 3 * x - 2
b = lambda y: (y + 2) / 3
assert all(b(a(x)) == x and a(b(y)) == y for x in pts for y in pts)
r = lambda x: 1 / x
assert all(r(r(x)) == x for x in pts if x > 0)
s = lambda x: x * abs(x)
t = lambda y: math.sqrt(y) if y >= 0 else -math.sqrt(-y)
fl = [float(p) for p in pts]
assert all(abs(t(s(x)) - x) < 1e-12 and abs(s(t(x)) - x) < 1e-12 for x in fl)
print("exm-two-sided-inverses: all quoted values check")
