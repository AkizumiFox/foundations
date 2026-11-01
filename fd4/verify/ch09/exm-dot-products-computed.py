"""exm-dot-products-computed (a)-(d) and the Quick check after the warning."""
from fractions import Fraction as Fr
import itertools


def dot(x, y):
    assert len(x) == len(y)
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"a": -1, "b": 0, "check1": 0, "check2": 14}
assert dot((1, 2, -1), (3, 0, 4)) == QUOTED["a"]
assert dot((1, 1, 1, 1), (1, -1, 1, -1)) == QUOTED["b"]
assert dot((2, -1, 3), (1, 5, 1)) == QUOTED["check1"]
assert dot((1, -2, 0, 3), (1, -2, 0, 3)) == QUOTED["check2"]
grid = [Fr(p, q) for p in range(-6, 7) for q in (1, 2, 3)]
for x1, x2 in itertools.product(grid, repeat=2):
    # (c): x perp (1,1) iff x = t(1,-1) for some t (namely t = x1)
    assert (dot((x1, x2), (1, 1)) == 0) == ((x1, x2) == (x1 * 1, x1 * -1))
    for x3 in (Fr(0), Fr(2, 3), Fr(-5)):
        # (d): <x, e3> = x3
        assert dot((x1, x2, x3), (0, 0, 1)) == x3
print("ok")
