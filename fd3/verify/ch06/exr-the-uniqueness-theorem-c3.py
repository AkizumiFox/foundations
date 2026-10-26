"""exr-the-uniqueness-theorem-c3 (b): the Newton sequence x_0 = 2, x_{n+1} = (x_n^2 + 2)/(2 x_n)
has x_n > 1 and x_m <= x_n for m >= n (checked on the first terms, exact rationals), so
(-x_n) is increasing and bounded above by -1; and x_n^2 > 2, so no term is a rational root.
(a)(3): the squeeze s - eps < a_N <= a_n <= s < s + eps gives |a_n - s| < eps, checked on a
sample increasing sequence a_n = 1 - 1/(n + 1) with s = 1."""
from fractions import Fraction as F

QUOTED = {"x0": F(2), "upper_bound_of_minus_x": F(-1), "c": -1}

xs = [QUOTED["x0"]]
for _ in range(7):
    s = xs[-1]
    xs.append((s * s + 2) / (2 * s))
for n, x in enumerate(xs):
    assert x > 1 and x * x > 2
    for m in range(n, len(xs)):
        assert xs[m] <= x
ys = [QUOTED["c"] * x for x in xs]
for n in range(len(ys) - 1):
    assert ys[n] <= ys[n + 1]
    assert ys[n] < QUOTED["upper_bound_of_minus_x"]

# (a)(3) on a sample: a_n = 1 - 1/(n + 1), s = sup = 1
a = [1 - F(1, n + 1) for n in range(200)]
s = F(1)
for eps in [F(1, 2), F(1, 10), F(1, 97)]:
    N = next(n for n in range(200) if a[n] > s - eps)
    for n in range(N, 200):
        assert a[N] <= a[n] <= s
        assert abs(a[n] - s) < eps
print("ok")
