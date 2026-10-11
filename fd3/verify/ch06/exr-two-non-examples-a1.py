"""exr-two-non-examples-a1: (a) t^2 - 100t = t(t - 100) > 0 for t > 100; (c) 0 < 1/t^2 < 1/t < 1/10^6
for t > 10^6, with 1/t - 1/t^2 = (t - 1)/t^2."""
from fractions import Fraction as F
QUOTED = {"a_threshold": 100, "c_threshold": "10^6"}
for t in [F(100) + F(1, k) for k in range(1, 30)] + [F(10 ** 6 + 1), F(5 * 10 ** 6)]:
    assert t * t - 100 * t == t * (t - 100) > 0
for t in [F(10 ** 6) + F(1, k) for k in range(1, 30)] + [F(10 ** 7)]:
    assert 0 < 1 / t ** 2 < 1 / t < F(1, 10 ** 6)
    assert 1 / t - 1 / t ** 2 == (t - 1) / t ** 2
print("ok")
