"""exr-...-b2 (03): (a) x/y + y/x - 2 = (x-y)^2/(xy); (b) a = (1/2, 1/2): 1/4 > 0;
(c) x = -1: 0 < 1, and (1+x)^3 - (1+3x+3x^2) = x^3; (d) AM-GM n = 4 spot checks."""
from fractions import Fraction as Fr
import itertools
vals = [Fr(1, 4), Fr(1, 2), Fr(1), Fr(3), Fr(9, 2)]
for x, y in itertools.product(vals, repeat=2):
    assert x / y + y / x - 2 == (x - y) ** 2 / (x * y) >= 0
assert (1 - Fr(1, 2)) ** 2 == Fr(1, 4) and 1 - (Fr(1, 2) + Fr(1, 2)) == 0
x = Fr(-1)
assert (1 + x) ** 3 == 0 and 1 + 3 * x + 3 * x * x == 1
for k in range(-20, 21):
    x = Fr(k, 4)
    assert (1 + x) ** 3 - (1 + 3 * x + 3 * x * x) == x ** 3
for a, b, c, d in itertools.product([Fr(0)] + vals, repeat=4):
    assert a * b * c * d <= ((a + b + c + d) / 4) ** 4
print("ok")
