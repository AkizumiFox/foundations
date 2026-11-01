"""exr-projection-and-angle-b3 (a): t0 = 1/9, p, squared distance 26/9 = 234/81, error orthogonal."""
from fractions import Fraction as Fr
QUOTED = {"t0": Fr(1, 9), "p": (Fr(2, 9), Fr(1, 9), Fr(-2, 9)), "dist2": Fr(26, 9), "err": (Fr(7, 9), Fr(8, 9), Fr(11, 9)), "sum81": 234}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
x, y = (1, 1, 1), (2, 1, -2)
t0 = dot(x, y) / dot(y, y); assert t0 == QUOTED["t0"]
p = tuple(t0 * b for b in y); assert p == QUOTED["p"]
e = tuple(a - b for a, b in zip(x, p)); assert e == QUOTED["err"]
assert dot(e, y) == 0 and dot(e, e) == QUOTED["dist2"] == 3 - Fr(1, 9)
assert sum((81 * c) ** 2 for c in e) / 81 == QUOTED["sum81"]
print("ok")
