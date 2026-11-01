"""thm-triangle-inequality-rn: (a) with equality case on squares; warning x = e1, y = -e1 (0 vs 2);
Quick check x = (1,-2,3), y = -2x: <x,y> = -28, ||x|| ||y|| = 28, ||x+y||^2 = 14 vs (3 sqrt14)^2 = 126."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"qc_dot": -28, "qc_prod": 28, "qc_sum_norm2": 14, "warn": (0, 2)}
random.seed(3)
for _ in range(20000):
    n = random.randint(1, 4); x = rvec(n, -2, 2)
    y = rvec(n, -2, 2) if random.random() < .6 else sc(random.choice([-2, -1, 0, 1, 3]), x)
    L, A, B, d = n2(add(x, y)), n2(x), n2(y), dot(x, y)
    # ||x+y|| <= ||x|| + ||y||  iff  L <= A + B + 2 sqrt(AB); equality iff d = sqrt(AB) iff d >= 0 and d^2 = AB
    assert L == A + 2 * d + B and d * d <= A * B
    eq = d >= 0 and d * d == A * B
    xz = all(v == 0 for v in x)
    nonneg = xz or any(y == sc(c, x) for c in [0] + [y[i] / x[i] for i in range(n) if x[i] != 0][:1] if c >= 0)
    assert eq == nonneg
e1, m1 = (1, 0), (-1, 0)
assert (n2(add(e1, m1)), 1 + 1) == (0, 2) == QUOTED["warn"]
x = (1, -2, 3); y = sc(-2, x)
assert dot(x, y) == QUOTED["qc_dot"] and n2(x) * n2(y) == QUOTED["qc_prod"] ** 2
assert n2(add(x, y)) == QUOTED["qc_sum_norm2"] and (n2(x) ** 1 * 9) == 126   # (3 sqrt 14)^2
# instance before the statement: (3,4) + (4,3) = (7,7), ||x+y||^2 = 98 < 100 = (5+5)^2
x, y = (3, 4), (4, 3)
assert add(x, y) == (7, 7) and n2(add(x, y)) == 98 < 100 == (5 + 5) ** 2 and n2(x) == 25 == n2(y)
print("ok")
