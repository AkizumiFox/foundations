"""exm-sqrt2-class: Newton x_0 = 2, x_{n+1} = x_n/2 + 1/x_n; e_n = x_n^2 - 2:
e_0..e_4 = 2, 1/4, 1/144, 1/166464, 1/221682772224; 0 < e_n <= 1/(4n) <= 1/(n+1) for n >= 1;
x_n > 1; fold: x_n - 2/x_n = e_n/x_n and 0 < e_n/x_n <= e_n."""
from fractions import Fraction as F
QUOTED = {"e": [F(2), F(1, 4), F(1, 144), F(1, 166464), F(1, 221682772224)]}
x = [F(2)]
for _ in range(7):
    x.append(x[-1] / 2 + 1 / x[-1])
e = [t * t - 2 for t in x]
assert e[:5] == QUOTED["e"]
for n in range(1, len(x)):
    assert 0 < e[n] <= F(1, 4 * n) <= F(1, n + 1)
    assert 4 * n - (n + 1) == 3 * n - 1 > 0
for n in range(len(x)):
    assert x[n] > 1
    assert x[n] - 2 / x[n] == e[n] / x[n]
    assert 0 < e[n] / x[n] <= e[n]
print("ok")
