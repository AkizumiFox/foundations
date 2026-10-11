"""thm-sqrt2-cauchy-no-rational-limit: x_0..x_3 = 2, 3/2, 17/12, 577/408; e_0..e_3 = 2, 1/4, 1/144, 1/166464;
e_n <= 1/(4n) for n >= 1 (checked exactly for n <= 9) with e_2 <= 1/8, e_3 <= 1/12; x_n > 1; decreasing;
(vi) 0 <= x_n - x_m <= e_n/x_n <= e_n <= 1/(4n) for m >= n >= 1; integer facts 4(n+1) <= 128n,
n + 1 <= 4n (n >= 1); e_n/32 <= 1/(128 n) chain; Cauchy threshold: 1/(4k) <= 1/(4N) <= 1/N."""
from fractions import Fraction as F
QUOTED = {"x": [F(2), F(3, 2), F(17, 12), F(577, 408)],
          "e": [F(2), F(1, 4), F(1, 144), F(1, 166464)],
          "bounds": {1: F(1, 4), 2: F(1, 8), 3: F(1, 12)},
          "upper": 2, "lower": 1, "lower_sharper": F(4, 3)}
t = lambda s: (s*s + 2) / (2*s)
x = [F(2)]
for n in range(9):
    x.append(t(x[-1]))
e = [xi*xi - 2 for xi in x]
assert x[:4] == QUOTED["x"] and e[:4] == QUOTED["e"]
for n, b in QUOTED["bounds"].items():
    assert b == F(1, 4*n) and e[n] <= b
for n in range(1, len(x)):
    assert e[n] <= F(1, 4*n)
for n in range(len(x)):
    assert x[n] > 1 and x[n] <= QUOTED["upper"] and x[n] > QUOTED["lower_sharper"]
    assert e[n] > 0
    if n + 1 < len(x):
        assert x[n+1] < x[n] and e[n+1] <= e[n]**2 / 8
for n in range(1, len(x)):
    for m in range(n, len(x)):
        assert 0 <= x[n] - x[m] <= e[n]/x[n] <= e[n] <= F(1, 4*n)
        assert x[m] > 2/x[m] >= 2/x[n]
assert QUOTED["lower_sharper"] == 2 / x[1]
for n in range(1, 10000):
    assert 4*(n + 1) <= 128*n and n + 1 <= 4*n
    # the step chain with e_n replaced by its bound 1/(4n)
    assert F(1, 4*n) / 32 == F(1, 128*n) <= F(1, 4*(n + 1))
for N in range(1, 200):
    for k in range(N, N + 50):
        assert F(1, 4*k) <= F(1, 4*N) <= F(1, N)
print("ok")
