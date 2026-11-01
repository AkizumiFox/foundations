"""exr-length-and-distance-c1: the counterexample to line (3): sqrt((-3)^2) = sqrt 9 = 3 != -3 (3 >= 0, 3^2 = 9); and on samples
|a| is the non-negative number with square a^2, and |a| >= a."""
QUOTED = {"a": "-3", "root": "\\sqrt 9 = 3"}
from fractions import Fraction as Fr
a = -3
assert a * a == 9 and 3 >= 0 and 3 * 3 == 9 and 3 != a
for k in range(-50, 51):
    a = Fr(k, 7)
    assert abs(a) >= 0 and abs(a) * abs(a) == a * a and abs(a) >= a
print("ok")
