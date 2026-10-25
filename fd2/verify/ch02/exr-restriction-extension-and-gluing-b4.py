"""exr-restriction-extension-and-gluing-b4: (b) f(1) = f(-1) = 1 for x^2; (e) the gluing of x and
2 - x agrees at 1 and has f(1/2) = 1/2 = f(3/2); (d) on rationals h is the identity and
h(x) = 2x elsewhere: halving and doubling keep rationals rational (exact fractions)."""
from fractions import Fraction as F

QUOTED = {"b": (1, 1), "e": (F(1, 2), F(1, 2))}
assert ((1) ** 2, (-1) ** 2) == QUOTED["b"]
g = lambda x: x if x <= 1 else 2 - x
assert 1 == 2 - 1
assert (g(F(1, 2)), g(F(3, 2))) == QUOTED["e"]
for x in [F(0), F(3, 7), F(-5, 2), F(22, 9)]:
    assert isinstance(x / 2, F) and isinstance(2 * x, F) and 2 * (x / 2) == x
print("exr-restriction-extension-and-gluing-b4: all quoted values check")
