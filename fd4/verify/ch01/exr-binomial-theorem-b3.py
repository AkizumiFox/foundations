"""exr-binomial-theorem-b3: (1.01)^10 >= 1 + 0.1 + 45 * 0.0001 = 1.1045, exactly in fractions."""
from fractions import Fraction as Fr
from math import comb
QUOTED = {"c": 45, "bound": Fr(11045, 10000)}
x = Fr(1, 100)
assert comb(10, 2) == QUOTED["c"] == 10 * 9 // 2
assert 1 + 10 * x + 45 * x ** 2 == QUOTED["bound"] == 1 + Fr(1, 10) + Fr(45, 10000)
assert (1 + x) ** 10 >= QUOTED["bound"]
print("ok")
