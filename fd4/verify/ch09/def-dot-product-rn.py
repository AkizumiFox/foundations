"""def-dot-product-rn: the examples after the definition and the minimal-change bracket x1y1 - x2y2."""
from fractions import Fraction as Fr
import random


def dot(x, y):
    assert len(x) == len(y)
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"(1,2).(3,4)": 11, "(3,4).(3,4)": 25, "|3+4i|": 5, "(1,2).(-2,1)": 0, "(1,0).(-1,0)": -1,
          "[e2,e2]": -1, "[(1,1),(1,1)]": 0,
          "(2,1).(1,4)": 6, "(2,1).(2,1)": 5, "(3,4).(1,2)": 11, "(2,4).(3,4)": 22, "(1,2).(1,2)": 5}
# instances before the definition and before prp-dot-product-laws-rn
assert dot((2, 1), (1, 4)) == QUOTED["(2,1).(1,4)"]
assert dot((2, 1), (2, 1)) == QUOTED["(2,1).(2,1)"]
assert dot((3, 4), (1, 2)) == QUOTED["(3,4).(1,2)"] == QUOTED["(1,2).(3,4)"]
assert dot((2, 4), (3, 4)) == QUOTED["(2,4).(3,4)"] == 2 * QUOTED["(1,2).(3,4)"]
assert dot((1, 2), (1, 2)) == QUOTED["(1,2).(1,2)"]
assert dot((1, 2), (3, 4)) == QUOTED["(1,2).(3,4)"]
assert dot((3, 4), (3, 4)) == QUOTED["(3,4).(3,4)"] == QUOTED["|3+4i|"] ** 2
assert dot((1, 2), (-2, 1)) == QUOTED["(1,2).(-2,1)"]
assert dot((1, 0), (-1, 0)) == QUOTED["(1,0).(-1,0)"]


def br(x, y):
    return Fr(x[0]) * y[0] - Fr(x[1]) * y[1]


assert br((0, 1), (0, 1)) == QUOTED["[e2,e2]"]
assert br((1, 1), (1, 1)) == QUOTED["[(1,1),(1,1)]"]
random.seed(3)
R = lambda: tuple(Fr(random.randint(-9, 9), random.randint(1, 5)) for _ in range(2))
for _ in range(500):
    x, y, z, c = R(), R(), R(), Fr(random.randint(-9, 9), random.randint(1, 5))
    assert br(x, y) == br(y, x)
    assert br(tuple(a + b for a, b in zip(x, y)), z) == br(x, z) + br(y, z)
    assert br(tuple(c * a for a in x), z) == c * br(x, z)
    # n = 1: dot product is the ordinary product
    assert dot((x[0],), (y[0],)) == x[0] * y[0]
print("ok")
