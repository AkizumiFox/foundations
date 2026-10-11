"""prp-ordered-field-halves: halves, midpoint, (c), (d) on samples; the warning's counterexample."""
from fractions import Fraction as Fr
import itertools

QUOTED = {"warning": {"a": -2, "b": 0, "c": -2, "d": 0, "ac": 4, "bd": 0}}
w = QUOTED["warning"]
assert w["a"] <= w["b"] and w["c"] <= w["d"]
assert w["a"] * w["c"] == w["ac"] and w["b"] * w["d"] == w["bd"] and not (w["ac"] <= w["bd"])

vals = [Fr(-5, 2), Fr(-1, 3), Fr(0), Fr(1, 7), Fr(1), Fr(9, 4)]
for e in [v for v in vals if v > 0]:
    assert 0 < e / 2 < e and e / 2 + e / 2 == e
for x, y in itertools.product(vals, repeat=2):
    if x < y:
        assert x < (x + y) / 2 < y
    if 0 < x <= y:
        assert 1 / y <= 1 / x
nn = [v for v in vals if v >= 0]
for a, b, c, d in itertools.product(nn, repeat=4):
    if a <= b and c <= d:
        assert a * c <= b * d
print("ok")
