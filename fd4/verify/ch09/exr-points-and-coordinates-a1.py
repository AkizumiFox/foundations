"""exr-points-and-coordinates-a1:
(a) (s+t, s-t) = (4, 2) iff s = 3, t = 1; (b) box membership; (c) the single point (1/2, 1/2);
(d) (0, 2) not in the open box (0,1) x (1,3); (e) [-1,1] x [0,1] x [2,2] has 6 integer points."""

from fractions import Fraction as Fr
from itertools import product


QUOTED = {
    "a": (3, 1),
    "b": (True, False),
    "c": (Fr(1, 2), Fr(1, 2)),
    "d": False,
    "e_box": ((-1, 1), (0, 1), (2, 2)),
    "e_count": 6,
}

# s + t = 4, s - t = 2: add and subtract (exact), then check back
sv, tv = Fr(4 + 2, 2), Fr(4 - 2, 2)
assert (sv, tv) == QUOTED["a"] and (sv + tv, sv - tv) == (4, 2)


def in_closed(x, box):
    return all(lo <= xk <= hi for xk, (lo, hi) in zip(x, box))


def in_open(x, box):
    return all(lo < xk < hi for xk, (lo, hi) in zip(x, box))


sq = [(0, 1), (Fr(1, 2), 1)]
assert (in_closed((1, Fr(1, 2)), sq), in_closed((Fr(1, 2), 0), sq)) == QUOTED["b"]

# x1 = x2 and x1 + x2 = 1 give 2 x1 = 1
x1 = Fr(1, 2); x2 = x1
assert (x1, x2) == QUOTED["c"] and x1 == x2 and x1 + x2 == 1

assert in_open((0, 2), [(0, 1), (1, 3)]) == QUOTED["d"]
assert in_open((Fr(1, 2), 2), [(0, 1), (1, 3)])  # second coordinate alone passes

a, b = (-1, 0, 2), (1, 1, 2)
assert all(ak <= bk for ak, bk in zip(a, b))
box = tuple(zip(a, b))
assert box == QUOTED["e_box"]
pts = [p for p in product(range(-5, 6), repeat=3) if in_closed(p, box)]
assert len(pts) == QUOTED["e_count"] == 3 * 2 * 1
print("exr-points-and-coordinates-a1: OK")
