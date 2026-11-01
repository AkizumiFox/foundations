"""B3 witnesses: (a) on random vectors; (b) e1, -e1; (d) e1, 2e1; (e) x = y = e1: 1 <= 1/2 fails; (e) after normalizing, u = v."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
random.seed(6)
for _ in range(5000):
    n = random.randint(1, 4); x, y = rvec(n), rvec(n)
    assert dot(x, y) <= Fr(1, 2) * (n2(x) + n2(y))
e1 = (1, 0, 0)
assert n2(add(e1, sc(-1, e1))) == 0 < 1 == n2(e1)                      # (b)
y = sc(2, e1); assert dot(e1, y) ** 2 == n2(e1) * n2(y) and dot(e1, y) == 2 and y != e1   # (d)
assert not (dot(e1, e1) <= Fr(1, 2) * 1)                                # (e)
print("ok")
