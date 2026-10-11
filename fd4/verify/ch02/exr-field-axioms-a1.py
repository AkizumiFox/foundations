"""exr-field-axioms-a1: (d) in Z/6Z, [2][1] = [2], [2][4] = [8] = [2], [1] != [4] (6 does not
divide 4 - 1 = 3); [2][3] = [0]. (e) 3x + 2y = 1, x - y = 2 in Q: ad - bc = -5, x = 1, y = -1."""
from fractions import Fraction as Fr
QUOTED = {"d": (2, 8, 3), "det": -5, "x": 1, "y": -1}
assert 2 * 1 % 6 == 2 and 2 * 4 == QUOTED["d"][1] and 8 % 6 == 2
assert (4 - 1) == QUOTED["d"][2] and 3 % 6 != 0
assert 2 * 3 % 6 == 0
a, b, c, d, e, f = 3, 2, 1, -1, 1, 2
D = a * d - b * c
assert D == QUOTED["det"] == -3 - 2
x, y = Fr(e * d - b * f, D), Fr(a * f - c * e, D)
assert e * d - b * f == -5 and a * f - c * e == 5
assert (x, y) == (QUOTED["x"], QUOTED["y"])
assert 3 * x + 2 * y == 1 and x - y == 2
print("ok")
