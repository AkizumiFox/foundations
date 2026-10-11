"""exr-a-cauchy-sequence-without-a-limit-b1: x_n - 2/x_n = e_n/x_n, 0 < e_n/x_n <= 1/(n+1) for n >= 1;
2/x_n < x_m for all m, n; (2/x_n)^2 < 2."""
from fractions import Fraction as F
QUOTED = {"upper_bound_from": 1}
t = lambda s: (s*s + 2) / (2*s)
x = [F(2)]
for n in range(8):
    x.append(t(x[-1]))
for n in range(len(x)):
    en = x[n]**2 - 2
    assert x[n] - 2/x[n] == en / x[n]
    if n >= 1:
        assert 0 < en/x[n] <= F(1, n + 1)
    assert (2/x[n])**2 < 2
    for m in range(len(x)):
        assert 2/x[n] < x[m]
assert QUOTED["upper_bound_from"] == 1
print("ok")
