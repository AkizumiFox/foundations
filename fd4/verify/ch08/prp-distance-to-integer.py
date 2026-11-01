"""prp-distance-to-integer (a)-(d) on many rationals against a brute-force distance;
Quick check 3: dist(0) = 0, dist(1/2) = 1/2, so 1/2 is not a period."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, dist, rationals
QUOTED = {"qc3": (0, F(1, 2))}
xs = rationals(); ys = rationals(seed=11)
for x, y in zip(xs, ys):
    m = floor(x); t = x - m
    d = dist(x)
    assert d == min(t, 1 - t) and d in (abs(x - m), abs(x - m - 1))     # (a)
    assert 0 <= d <= F(1, 2)
    assert (d == 0) == (x.denominator == 1)
    assert (d == F(1, 2)) == ((x - F(1, 2)).denominator == 1)          # (b)
    assert dist(x + 1) == d and dist(-x) == d                          # (c)
    assert d <= abs(x) and dist(x + y) <= d + dist(y)
    assert abs(d - dist(y)) <= abs(x - y)                              # (d)
assert (dist(0), dist(F(1, 2))) == QUOTED["qc3"]
print("prp-distance-to-integer: OK")
