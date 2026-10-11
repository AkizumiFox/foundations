"""exm-first-sequences-ordered-field and the Quick check after it: |(n+1)/(n+2) - 1| = 1/(n+2);
|a_{n+1} - a_n| = 2 for a_n = (-1)^n; for 1/(n+1) and eps = 1/100 exactly the N >= 100 work."""
from fractions import Fraction as Q

QUOTED = {"gap": 2, "least_N": 100}
for k in range(1000):
    assert abs(Q(k + 1, k + 2) - 1) == Q(1, k + 2) < Q(1, k + 1)
    assert abs((-1) ** (k + 1) - (-1) ** k) == QUOTED["gap"]
    assert abs((-1) ** k) == 1
eps = Q(1, 100)
def works(N, horizon=2000):
    return all(Q(1, m + 1) < eps for m in range(N, horizon))
good = [N for N in range(0, 300) if works(N)]
assert good[0] == QUOTED["least_N"] and good == list(range(100, 300))
assert not (Q(1, 100) < eps)          # N = 99 fails at n = 99
# 1/(n+1) < 1/100 iff 100 < n + 1 (comparison formula)
for k in range(300):
    assert (Q(1, k + 1) < eps) == (100 < k + 1)
# the N of (b) from Archimedes works for several eps
for e in [Q(1, 3), Q(2, 7), Q(1, 100), Q(5, 1001)]:
    N = int(1 / e) + 1
    assert all(Q(1, m) < e for m in range(N, N + 500))
    assert all(Q(1, m + 1) < e and Q(1, m + 2) < e for m in range(N, N + 500))
print("ok")
