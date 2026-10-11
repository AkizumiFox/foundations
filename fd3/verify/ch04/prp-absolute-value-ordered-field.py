"""prp-absolute-value-ordered-field (a)-(f) on samples in Q; the quick check's counterexample a = 0, b = 1."""
from fractions import Fraction as Fr
import itertools

QUOTED = {"check_counterexample": {"a": 0, "b": 1, "lhs": 1, "rhs": -1}}
q = QUOTED["check_counterexample"]
assert abs(q["a"] - q["b"]) == q["lhs"] and abs(q["a"]) - abs(q["b"]) == q["rhs"] and not (q["lhs"] <= q["rhs"])

vals = [Fr(-7, 3), Fr(-1), Fr(-1, 4), Fr(0), Fr(1, 5), Fr(2), Fr(11, 3)]
for x in vals:
    assert abs(x) >= 0 and ((abs(x) == 0) == (x == 0))
    assert abs(-x) == abs(x) and abs(x) ** 2 == x * x and -abs(x) <= x <= abs(x)
    if x != 0:
        assert abs(1 / x) == 1 / abs(x)
for x, y, z in itertools.product(vals, repeat=3):
    assert abs(x * y) == abs(x) * abs(y)
    assert abs(x + y) <= abs(x) + abs(y)
    assert abs(x - z) <= abs(x - y) + abs(y - z)
    assert abs(abs(x) - abs(y)) <= abs(x - y)
    r = z
    assert (abs(x) <= r) == (-r <= x <= r)
    assert (abs(x) < r) == (-r < x < r)
print("ok")
