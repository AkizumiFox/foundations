"""exm-piecewise-as-gluing: (a) values 0 and -0 = 0 at the overlap; (b) values 0 and 1 at 0;
(c) k(1/2) = 1/2 = k(-1/2) for x on [0, inf), x + 1 on (-inf, 0)."""
from fractions import Fraction as F

QUOTED = {"a": (0, 0), "b": (0, 1), "c": F(1, 2)}
assert (0, -0) == QUOTED["a"]
assert (0, 0 + 1) == QUOTED["b"]
k = lambda x: x if x >= 0 else x + 1
assert k(F(1, 2)) == QUOTED["c"] == k(F(-1, 2))
print("exm-piecewise-as-gluing: all quoted values check")
