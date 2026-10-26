"""exr-ordered-field-of-rationals-a1 (c): -2/3 < -3/5 since -10 < -9; (e): eps = 1/n refutes 1/n < eps."""
from fractions import Fraction as F
QUOTED = {"lhs": -10, "rhs": -9}
assert (-2) * 5 == QUOTED["lhs"] and (-3) * 3 == QUOTED["rhs"] and -10 < -9
assert F(-2, 3) < F(-3, 5)
for n in range(1, 50):
    assert not (F(1, n) < F(1, n))
print("ok")
