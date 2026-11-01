"""def-step-function: floor constant on the open pieces cut at the integers; Quick check 4:
the midpoint c of 1/(n+1), 1/n is not 1/k; prp-step-function-algebra example cut points."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor
# floor on [a, b] is constant between consecutive cut points
for a, b in ((F(-7, 3), F(5, 2)), (F(0), F(3)), (F(1, 3), F(2, 3))):
    cuts = sorted({a, b} | {F(j) for j in range(floor(a) + 1, floor(b) + 1) if a < j < b})
    for lo, hi in zip(cuts, cuts[1:]):
        vals = {floor(lo + (hi - lo) * F(i, 50)) for i in range(1, 50)}
        assert len(vals) == 1
for n in range(1, 200):
    c = (F(1, n + 1) + F(1, n)) / 2
    assert F(1, n + 1) < c < F(1, n) and all(c != F(1, k) for k in range(1, 3 * n + 3))
# indicator of [0,1/2] + indicator of [0,1/3]: values on (0,1/3), (1/3,1/2), (1/2,1)
f = lambda x: (1 if x <= F(1, 2) else 0) + (1 if x <= F(1, 3) else 0)
assert [f(F(1, 6)), f(F(5, 12)), f(F(3, 4))] == [2, 1, 0]
print("def-step-function: OK")
