"""exr-cauchy-sequences-of-rationals-b2 (b): x_n - 2/x_n = e_n/x_n, with 0 <= e_n/x_n <= 1/(n+1) for n >= 1."""
from fractions import Fraction as F

QUOTED = {"upper": "1/(n+1)"}
x = [F(2)]
for _ in range(10):
    x.append((x[-1] ** 2 + 2) / (2 * x[-1]))
for n, t in enumerate(x):
    e = t * t - 2
    assert t - 2 / t == e / t and 0 < e / t < e
    assert (2 / t) ** 2 < 2
    if n >= 1:
        assert e / t <= F(1, n + 1)
print("ok")
