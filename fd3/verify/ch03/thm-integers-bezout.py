"""thm-integers-bezout: the Try-it-first data and the coin paragraph after the proof.
The positive combinations listed in the Idea, 12, 42, 30, 18, 6, are combinations of 12 and 42,
and the least positive combination is 6 = 12*(-3) + 42*1 = gcd(12, 42)."""
import math
QUOTED = {"listed": {12: (1, 0), 42: (0, 1), 30: (-1, 1), 18: (5, -1), 6: (-3, 1)}, "d": 6}
for v, (x, y) in QUOTED["listed"].items():
    assert 12 * x + 42 * y == v > 0
S = {12 * x + 42 * y for x in range(-40, 41) for y in range(-40, 41)}
assert min(v for v in S if v > 0) == QUOTED["d"] == math.gcd(12, 42)
print("ok")
