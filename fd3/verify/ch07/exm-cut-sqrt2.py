"""exm-cut-sqrt2: for p in Q, p > 0, p^2 < 2: d = 2 - p^2 in (0, 2), h = d/(2p + 2) in (0, 1),
(p + h)^2 = p^2 + 2ph + h^2 < p^2 + 2ph + h < p^2 + h(2p + 2) = 2. Also 2 not in sigma (4 > 2), 1 in sigma."""
from fractions import Fraction as F

QUOTED = {"two_sq": 4, "one_sq": 1}
assert 2 * 2 == QUOTED["two_sq"] > 2 and 1 * 1 == QUOTED["one_sq"] < 2

samples = [F(n, 1000) for n in range(1, 1415)] + [F(99, 70), F(1393, 985), F(577, 408) - F(1, 10**6)]
count = 0
for p in samples:
    if not (p > 0 and p * p < 2):
        continue
    count += 1
    d = 2 - p * p
    h = d / (2 * p + 2)
    assert 0 < d < 2 and 2 * p + 2 > 2
    assert 0 < h < 1 and h * h < h
    assert (p + h) ** 2 == p * p + 2 * p * h + h * h
    assert p * p + 2 * p * h + h * h < p * p + 2 * p * h + h < p * p + h * (2 * p + 2)
    assert p * p + h * (2 * p + 2) == 2
    assert (p + h) ** 2 < 2 and p + h > p
assert count > 1000
print("ok")
