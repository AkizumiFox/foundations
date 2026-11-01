"""thm-cauchy-schwarz-rn: the inequality and its equality cases (b), (c), (c') on random integer vectors,
compared by squares; the hook's (1,...,1) example; the Quick check x = (1,2,2), y = (2,0,1)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *

QUOTED = {"qc_dot": 4, "qc_nx2": 9, "qc_ny2": 5, "qc_sq": (16, 45), "qc_parallel": False}
random.seed(5)
for _ in range(20000):
    n = random.randint(1, 4)
    x = rvec(n, -2, 2)
    y = rvec(n, -2, 2) if random.random() < .6 else sc(random.choice([-2, -1, 0, 1, 3]), x)
    d, A, B = dot(x, y), n2(x), n2(y)
    assert d * d <= A * B                              # (a), squared
    assert (d * d == A * B) == parallel(x, y)          # (b)
    xz = all(v == 0 for v in x)
    nonneg = xz or any(y == sc(c, x) for c in [0] + ([y[i] / x[i] for i in range(n) if x[i] != 0][:1]) if c >= 0)
    nonpos = xz or any(y == sc(c, x) for c in [0] + ([y[i] / x[i] for i in range(n) if x[i] != 0][:1]) if c <= 0)
    assert (d >= 0 and d * d == A * B) == nonneg       # (c)
    assert (d <= 0 and d * d == A * B) == nonpos       # (c')
# hook: x = y = (1,...,1): <x,y> = n = ||x|| ||y||, coordinatewise bound n^2
for n in range(1, 8):
    w = (1,) * n
    assert dot(w, w) == n and n2(w) == n
x, y = (1, 2, 2), (2, 0, 1)
assert dot(x, y) == QUOTED["qc_dot"] and n2(x) == QUOTED["qc_nx2"] and n2(y) == QUOTED["qc_ny2"]
assert (dot(x, y) ** 2, n2(x) * n2(y)) == QUOTED["qc_sq"]
assert parallel(x, y) == QUOTED["qc_parallel"]
# instance before the statement: (3,4), (4,3): 24 vs 25; y = 2x = (6,8): 50 = 5*10
x, y = (3, 4), (4, 3)
assert dot(x, y) == 24 == 12 + 12 and n2(x) == 25 == n2(y)
assert sc(2, x) == (6, 8) and dot(x, (6, 8)) == 50 == 18 + 32 and n2((6, 8)) == 100 and 5 * 10 == 50
print("ok")
