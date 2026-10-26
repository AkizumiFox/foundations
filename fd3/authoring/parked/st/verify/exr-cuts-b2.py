"""exr-cuts-b2: beta = {p < 0 or p^2 < 3}; 0 in, 2 out (4 > 3). For p >= 0, p^2 < 3:
d = 3 - p^2 in (0, 3], h = d/(2p + 4) in (0, 1), (p + h)^2 < p^2 + h(2p + 1) < p^2 + h(2p + 4) = 3."""
from fractions import Fraction as F
QUOTED = {"denominator_offset": 4, "two_sq": 4}
assert 2 * 2 == QUOTED["two_sq"]

assert 2 * 2 == 4 > 3
count = 0
for p in [F(n, 1000) for n in range(0, 1733)]:
    if p * p >= 3:
        continue
    count += 1
    d = 3 - p * p
    h = d / (2 * p + QUOTED["denominator_offset"])
    assert 0 < d <= 3 < 4 <= 2 * p + 4
    assert 0 < h < 1 and h * h < h
    assert (p + h) ** 2 < p * p + h * (2 * p + 1) < p * p + h * (2 * p + 4) == 3
assert count > 1700
print("ok")
