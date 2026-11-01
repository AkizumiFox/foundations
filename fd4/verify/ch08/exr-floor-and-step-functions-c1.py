"""C1 (Hermite): sum_{k<n} floor(x + k/n) = floor(nx); both sides grow by 1 under x -> x + 1/n;
both vanish on [0, 1/n)."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, rationals
lhs = lambda x, n: sum(floor(x + F(k, n)) for k in range(n))
for x in rationals(1500):
    for n in (1, 2, 3, 5, 8):
        assert lhs(x, n) == floor(n * x)
        assert lhs(x + F(1, n), n) == lhs(x, n) + 1
for n in (1, 2, 3, 5, 8):
    for i in range(30):
        x = F(i, 30 * n)
        assert lhs(x, n) == 0 == floor(n * x)
print("exr-floor-and-step-functions-c1: OK")
