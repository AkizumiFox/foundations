"""exr-a-cauchy-sequence-without-a-limit-c1: y_1 = 7/4, y_2 = 97/56; d_0..d_2 = 1, 1/16, 1/3136;
d_{n+1} = d_n^2/(4 y_n^2) <= d_n^2/12; y_n - y_{n+1} = d_n/(2 y_n); d_n <= 1/(16 n) for n >= 1;
16n + 16 <= 3072 n; 0 <= y_n - y_m <= d_n/y_n <= d_n for m >= n >= 1; y_n > 1;
descent identity (3q - p)^2 - 3(p - q)^2 = 2(3q^2 - p^2)."""
from fractions import Fraction as F
import random
QUOTED = {"y": [F(2), F(7, 4), F(97, 56)], "d": [F(1), F(1, 16), F(1, 3136)]}
u = lambda s: (s*s + 3) / (2*s)
y = [F(2)]
for n in range(8):
    y.append(u(y[-1]))
d = [yi*yi - 3 for yi in y]
assert y[:3] == QUOTED["y"] and d[:3] == QUOTED["d"]
assert F(9409, 3136) - 3 == F(1, 3136) and 97**2 == 9409 and 56**2 == 3136
assert (F(1, 16))**2 / (4 * F(49, 16)) == F(1, 3136)
for n in range(len(y) - 1):
    assert y[n] > 1 and d[n] > 0
    assert d[n+1] == d[n]**2 / (4*y[n]**2) <= d[n]**2 / 12
    assert y[n] - y[n+1] == d[n] / (2*y[n]) > 0
for n in range(1, len(y)):
    assert d[n] <= F(1, 16*n)
    for m in range(n, len(y)):
        assert 0 <= y[n] - y[m] <= d[n]/y[n] <= d[n] <= F(1, 16*n)
for n in range(1, 10000):
    assert 16*n + 16 <= 3072*n
    assert F(1, 16*n) / 192 == F(1, 3072*n) <= F(1, 16*(n + 1))
    assert F(1, 16*n) <= F(1, n + 1)
random.seed(3)
for _ in range(3000):
    p, q = random.randint(-500, 500), random.randint(-500, 500)
    assert (3*q - p)**2 - 3*(p - q)**2 == 2*(3*q*q - p*p)
# identity for u(s)
for _ in range(2000):
    s = F(random.randint(1, 300), random.randint(1, 300))
    assert u(s)**2 - 3 == ((s*s + 3)**2 - 12*s*s) / (4*s*s) == (s*s - 3)**2 / (4*s*s)
    assert s - u(s) == (s*s - 3) / (2*s)
print("ok")
