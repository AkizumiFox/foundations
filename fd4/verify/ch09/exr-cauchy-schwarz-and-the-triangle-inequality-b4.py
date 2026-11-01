"""B4: (a) (sum x)^2 <= n sum x^2, equality iff all equal; (b) min ||x||^2 = 9 on x1 + 2x2 + 2x3 = 9, only at (1,2,2)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"p_norm": 3, "min": 9, "argmin": (1, 2, 2)}
random.seed(7)
for _ in range(5000):
    n = random.randint(1, 5); x = rvec(n, -3, 3)
    l, r = sum(x) ** 2, n * n2(x)
    assert l <= r and ((l == r) == (len(set(x)) == 1))
p = (1, 2, 2)
assert n2(p) == QUOTED["p_norm"] ** 2
x0 = QUOTED["argmin"]
assert dot(p, x0) == 9 and n2(x0) == QUOTED["min"]
for _ in range(20000):   # random rational points on the plane: ||x||^2 >= 9, = 9 only at x0
    x2, x3 = Fr(random.randint(-40, 40), random.randint(1, 10)), Fr(random.randint(-40, 40), random.randint(1, 10))
    x = (9 - 2 * x2 - 2 * x3, x2, x3)
    assert dot(p, x) == 9 and n2(x) >= 9 and ((n2(x) == 9) == (x == tuple(map(Fr, x0))))
# exact: ||x||^2 - 9 = ||x - x0||^2 on the plane (x - x0 is orthogonal to p)
print("ok")
