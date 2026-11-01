"""exm-root-limits (05): thresholds N > (a-1)/eps (bound (a-1)/n) and N > 1 + 2/eps^2 (bound 2/(n-1) < eps^2) work."""
import math
from fractions import Fraction as F

QUOTED = {}
for eps in [F(1, 2), F(1, 10), F(1, 37)]:
    for a in [F(2), F(5), F(30)]:
        N = math.floor((a - 1) / eps) + 1
        assert N >= 1 and all((a - 1) / n < eps for n in range(N, N + 300))
    N = math.floor(1 + 2 / eps ** 2) + 1
    assert N >= 2 and all(F(2, n - 1) < eps ** 2 for n in range(N, N + 300))
print("ok")
