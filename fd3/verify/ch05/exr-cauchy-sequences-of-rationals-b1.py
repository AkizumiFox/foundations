"""exr-cauchy-sequences-of-rationals-b1 (b): (3 + 1/(n+1)) - (c) tends to 3 - c, so only c = 3 works."""
from fractions import Fraction as F

QUOTED = {"c": 3}
# the difference minus (3 - c) is 1/(n + 1), which falls below 1/1000 from n = 1000 on
for c in [F(k, 4) for k in range(0, 25)]:
    diffs = [(3 + F(1, n + 1)) - c for n in range(2000)]
    assert all(dv - (3 - c) == F(1, n + 1) for n, dv in enumerate(diffs))
    small_tail = all(abs(dv) < F(1, 1000) for dv in diffs[1000:])
    assert small_tail == (c == QUOTED["c"])
print("ok")
