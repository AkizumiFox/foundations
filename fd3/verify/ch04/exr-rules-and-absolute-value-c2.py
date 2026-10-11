"""exr-rules-and-absolute-value-c2: max and min through the absolute value, on samples."""
from fractions import Fraction as Fr
import itertools

QUOTED = {"max": "{a + b + \\abs{a - b}}{2}", "min": "{a + b - \\abs{a - b}}{2}"}
vals = [Fr(-3), Fr(-1, 2), Fr(0), Fr(2, 3), Fr(5)]
for a, b in itertools.product(vals, repeat=2):
    assert max(a, b) == (a + b + abs(a - b)) / 2
    assert min(a, b) == (a + b - abs(a - b)) / 2
for x in vals:
    assert abs(x) == max(x, -x)
print("ok")
