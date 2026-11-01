"""exr-...-b1 (03): (a+b)(b+c)(c+a) >= 8abc for positive a, b, c, via (a+b)^2 >= 4ab."""
from fractions import Fraction as Fr
import itertools
vals = [Fr(1, 3), Fr(1, 2), Fr(1), Fr(2), Fr(7, 3), Fr(10)]
for a, b, c in itertools.product(vals, repeat=3):
    assert (a + b) ** 2 >= 4 * a * b
    P = (a + b) * (b + c) * (c + a)
    assert 64 * a * a * b * b * c * c <= P * P and P >= 8 * a * b * c
print("ok")
