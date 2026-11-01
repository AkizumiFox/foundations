"""exm-distance-to-a-line-through-the-origin: t0, p, error, squared distances, and ||x - ty||^2 = 2 + 3(t-2)^2."""
from fractions import Fraction as Fr
QUOTED = {"a": {"t0": 2, "p": (2, 2), "err": (1, -1), "dist2": 2},
          "b": {"t0": 2, "p": (2, 2, 2), "err": (-1, 0, 1), "dist2": 2, "formula": (2, 3, 2), "at0": 14}}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
for key, x, y in (("a", (3, 1), (1, 1)), ("b", (1, 2, 3), (1, 1, 1))):
    q = QUOTED[key]
    t0 = dot(x, y) / dot(y, y); assert t0 == q["t0"]
    p = tuple(t0 * b for b in y); assert p == q["p"]
    e = tuple(a - b for a, b in zip(x, p)); assert e == q["err"]
    assert dot(e, y) == 0 and dot(e, e) == q["dist2"]
    if key == "b":
        c0, c1, c2 = q["formula"]
        for t in [Fr(k, 2) for k in range(-10, 11)]:
            v = tuple(a - t * b for a, b in zip(x, y))
            assert dot(v, v) == c0 + c1 * (t - c2) ** 2
        assert c0 + c1 * c2 ** 2 == q["at0"] == dot(x, x) == 1 + 4 + 9
print("ok")
