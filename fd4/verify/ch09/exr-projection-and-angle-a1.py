"""exr-projection-and-angle-a1 (c), (d)."""
from fractions import Fraction as Fr
QUOTED = {"c": {"t=0": (14, 14), "t=1": (5, 5)}, "d": {"p": (Fr(1, 3), Fr(2, 3), Fr(2, 3)), "err": (Fr(8, 3), Fr(-2, 3), Fr(-2, 3))}}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
x, y = (1, 2, 3), (1, 1, 1)
t0 = dot(x, y) / dot(y, y); p = tuple(t0 * b for b in y); e = tuple(a - b for a, b in zip(x, p))
for t in (0, 1):
    v = tuple(a - t * b for a, b in zip(x, y))
    assert (dot(v, v), dot(e, e) + (t - t0) ** 2 * dot(y, y)) == QUOTED["c"][f"t={t}"]
x, y = (3, 0, 0), (1, 2, 2)
t0 = dot(x, y) / dot(y, y); p = tuple(t0 * b for b in y)
assert p == QUOTED["d"]["p"]
e = tuple(Fr(a) - b for a, b in zip(x, p)); assert e == QUOTED["d"]["err"] and dot(e, y) == 0
print("ok")
