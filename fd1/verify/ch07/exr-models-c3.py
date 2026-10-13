"""exr-models-c3 (Section 4.11, exit check): (a) with N > 1/eps (N = floor(1/eps) + 1) works for
sample eps; (b)'s negation with eps = 1/N, n = N for N = 1..500; the bounds are n, N in Z_{>0}."""
from fractions import Fraction as F
import math

QUOTED = {}
for eps in [F(1), F(1, 2), F(3, 7), F(1, 100), F(2, 1000), F(5, 3), F(1, 10**6)]:
    N = math.floor(1 / eps) + 1
    assert N > 1 / eps and N >= 1   # a natural number above 1/eps > 0 lies in Z_{>0}
    assert all(F(1, n) < eps for n in range(N, N + 200))
for N in range(1, 501):
    eps, n = F(1, N), N
    assert eps > 0 and n >= N and F(1, n) >= eps
print("exr-models-c3: all quoted values check")
