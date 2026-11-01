"""exr-roots-and-rational-powers-b1 (05): 32^(3/5) = 8; (a^(1/2) b^(-1/3))^6 = a^3 b^-2 (exponent arithmetic); 4^(3/2)/8^(2/3) = 2."""
from fractions import Fraction as F

QUOTED = {"a": 8, "b": (3, -2), "c": 2}
assert 2 ** 5 == 32 and 2 ** 3 == QUOTED["a"]
assert (F(1, 2) * 6, F(-1, 3) * 6) == QUOTED["b"]
# numeric spot check with a = x^6, b = y^6 (so all roots rational)
for x in [F(2), F(3, 5)]:
    for y in [F(5), F(1, 7)]:
        a, b = x ** 6, y ** 6
        assert (x ** 3 * y ** -2) ** 6 == a ** 3 * b ** -2
assert 2 ** 2 == 4 and F(2 ** 3, 2 ** 2) == QUOTED["c"]
print("ok")
