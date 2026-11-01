"""cor-triangle-finite-sums-rn: instance before the statement, e1 + e2 + e3 = (1,1,1), ||(1,1,1)||^2 = 3 <= 9 = 3^2;
random check of ||sum v_j|| <= sum ||v_j|| (floats, m = 0 included)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"sum": (1, 1, 1), "norm2": 3, "lengths": 3}
e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
s = add(add(e[0], e[1]), e[2])
assert s == QUOTED["sum"] and n2(s) == QUOTED["norm2"]
assert sum(n2(v) for v in e) == 3 and all(n2(v) == 1 for v in e)   # each length 1, so lengths add to 3
assert QUOTED["norm2"] <= QUOTED["lengths"] ** 2 == 9
random.seed(5)
for _ in range(5000):
    n, m = random.randint(1, 4), random.randint(0, 5)
    vs = [rvec(n) for _ in range(m)]
    tot = tuple(Fr(0) for _ in range(n))
    for v in vs: tot = add(tot, v)
    assert float(n2(tot)) ** .5 <= sum(float(n2(v)) ** .5 for v in vs) + 1e-9
print("ok")
