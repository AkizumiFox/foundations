"""exr-exponential-and-logarithm-b2: (a) binom(n,2)/n^2 = (1 - 1/n)/2 and the truncated binomial bound;
exp x >= 1 + x + x^2/2 for x >= 0 numerically; (b) log x <= x/e numerically; (c) 1^(-1) = 1 > 1/2 = 2^(-1);
(d) the bound |p(x)| <= (S + |a_d|) x^d for x >= 1 and the threshold M (d + 1)^(d + 1) on samples."""
from fractions import Fraction as Fr
from math import comb, exp, log, e
import random
for n in range(2, 200):
    assert Fr(comb(n, 2), n * n) == (1 - Fr(1, n)) / 2
    for x in [Fr(k, 3) for k in range(0, 30)]:
        if n > x:
            assert (1 + x / n) ** n >= 1 + x + x * x / 2 - x * x / (2 * n)
for k in range(0, 400):
    x = k / 20
    assert exp(x) >= 1 + x + x * x / 2
    if x > 0:
        assert log(x) <= x / e + 1e-15
assert 1 ** -1 == 1 and 2.0 ** -1 == 0.5
random.seed(3)
for _ in range(300):
    d = random.randint(0, 4)
    a = [random.randint(-9, 9) for _ in range(d + 1)]
    S = sum(abs(c) for c in a[:-1]); M = S + abs(a[-1]) + 1
    for x in [1, 1.5, 3, 10]:
        p = sum(c * x ** i for i, c in enumerate(a))
        assert abs(p) <= (S + abs(a[-1])) * x ** d + 1e-9
    x = M * (d + 1) ** (d + 1) * 1.0001
    if x < 700:
        p = sum(c * x ** i for i, c in enumerate(a))
        assert exp(x) > M * x ** d > abs(p)
print("ok")
