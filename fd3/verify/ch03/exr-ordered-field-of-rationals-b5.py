"""exr-ordered-field-of-rationals-b5 (printed B4): Prove or disprove (a)-(d)."""
from fractions import Fraction as F
import math
QUOTED = {"a_x": F(1, 2), "a_y": F(1), "a_lhs": F(1), "a_rhs": F(1, 2),
          "c_bound": F(1), "c_witness": F(2)}
# (a) counterexample
x, y = QUOTED["a_x"], QUOTED["a_y"]
assert 0 < x < y
assert 1 / x - 1 / y == QUOTED["a_lhs"] and y - x == QUOTED["a_rhs"]
assert QUOTED["a_lhs"] > QUOTED["a_rhs"]
rats = {F(p, q) for p in range(-40, 41) for q in range(1, 13)}
pos = sorted(r for r in rats if r > 0)
# (b) true: brute force over small positive rationals
for r in pos:
    n = next(k for k in range(1, 1000) if F(1, k) < r < k)
    assert F(1, n) < r < n
    # the proof's n = max(n1, n2) works
    n1 = next(k for k in range(0, 1000) if r < k)
    n2 = next(k for k in range(1, 1000) if F(1, k) < r)
    m = max(n1, n2)
    assert m > 0 and F(1, m) < r < m
# (c) false: S = {x > 1}; midpoint of 1 and x is in S and smaller
b = QUOTED["c_bound"]
assert QUOTED["c_witness"] > b > 0
for r in pos:
    if r > 1:
        mid = (1 + r) / 2
        assert 1 < mid < r
# (d) true: brute force
for r in rats:
    assert math.floor(r + 1) == math.floor(r) + 1
print("ok")
