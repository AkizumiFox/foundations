"""exr-rules-and-absolute-value-a1: the counterexamples of (b), (c) and samples for (d)."""
from fractions import Fraction as Fr

QUOTED = {"b": (-2, 1, 4, 1), "c": (1, -2)}
a, b, sa, sb = QUOTED["b"]
assert a < b and a * a == sa and b * b == sb and not (sa < sb)
a, b = QUOTED["c"]
assert abs(a) < abs(b) and not (a < b)
for k in range(-50, 51):
    x = Fr(k, 7)
    assert x * x + 1 > 0
assert Fr(0) < Fr(1, 2) < 1
print("ok")
