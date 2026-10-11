"""thm-bernoulli: the counterexample x = -4, n = 3, and checks on a grid."""
from fractions import Fraction as Fr

QUOTED = {"lhs": -27, "rhs": -11}
assert (1 - 4) ** 3 == QUOTED["lhs"] and 1 + 3 * (-4) == QUOTED["rhs"] and -27 < -11
for num in range(-4, 41):
    x = Fr(num, 4)  # x >= -1
    assert all((1 + x) ** n >= 1 + n * x for n in range(60))
# step algebra: (1 + nx)(1 + x) = 1 + (n + 1)x + n x^2
for n in range(10):
    for x in [Fr(-1), Fr(-1, 2), Fr(3)]:
        assert (1 + n * x) * (1 + x) == 1 + (n + 1) * x + n * x * x
print("ok")
