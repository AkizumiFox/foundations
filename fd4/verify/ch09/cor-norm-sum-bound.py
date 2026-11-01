"""cor-norm-sum-bound: ||x|| <= sum |x_k| <= sqrt(n) ||x|| (on squares), equality at e1 and (1,...,1)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
random.seed(4)
for _ in range(20000):
    n = random.randint(1, 6); x = rvec(n, -5, 5)
    S = sum(abs(t) for t in x)
    assert n2(x) <= S * S <= n * n2(x)
for n in range(1, 8):
    e = (1,) + (0,) * (n - 1); w = (1,) * n
    assert n2(e) == sum(abs(t) for t in e) ** 2
    assert sum(w) ** 2 == n * n2(w)
# instance before the statement: x = (3,4): ||x|| = 5, sum 7, 49 <= 50 = 2 * 25
x = (3, 4)
assert n2(x) == 25 and abs(3) + abs(4) == 7 and 25 <= 49 and 49 <= 2 * 25 == 50
print("ok")
