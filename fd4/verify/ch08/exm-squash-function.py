"""exm-squash-function: sigma(x) = x/(1 + |x|). Difference formulas on each half,
image (-1, 1) with preimage v/(1 - |v|) = v/(1 - v) (v >= 0), v/(1 + v) (v < 0)."""
from fractions import Fraction as F
import random

s = lambda x: x / (1 + abs(x))
random.seed(2)
for _ in range(4000):
    x, y = sorted(F(random.randint(-500, 500), random.randint(1, 50)) for _ in range(2))
    if x == y:
        continue
    if x >= 0:
        assert s(y) - s(x) == (y - x) / ((1 + x) * (1 + y))
    if y <= 0:
        assert s(y) - s(x) == (y - x) / ((1 - x) * (1 - y))
    assert s(x) < s(y) and abs(s(x)) < 1
    v = F(random.randint(-999, 999), 1000)
    pre = v / (1 - abs(v))
    assert pre == (v / (1 - v) if v >= 0 else v / (1 + v))
    assert s(pre) == v
print("ok")
