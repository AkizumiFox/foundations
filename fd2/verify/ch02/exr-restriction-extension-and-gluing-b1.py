"""exr-restriction-extension-and-gluing-b1: agreement at -1 and 1 (value 1); ranges [1, inf),
[0, 1], [1, inf) of the pieces, witnesses x = -t, sqrt t, t; range [0, inf); f(x) = 1/4 exactly
at -1/2, 1/2."""
from fractions import Fraction as F

QUOTED = {"agree": {-1: 1, 1: 1}, "solutions": {F(-1, 2), F(1, 2)}}
f1 = lambda x: -x; f2 = lambda x: x * x; f3 = lambda x: x
assert f1(-1) == f2(-1) == QUOTED["agree"][-1]
assert f2(1) == f3(1) == QUOTED["agree"][1]
def f(x):
    if x <= -1: return f1(x)
    if x <= 1: return f2(x)
    return f3(x)
grid = [F(k, 100) for k in range(-500, 501)]
assert all(f(x) >= 0 for x in grid)
assert all(f(x) >= 1 for x in grid if x <= -1 or x >= 1)
assert {x for x in grid if f(x) == F(1, 4)} == QUOTED["solutions"]
for x in grid:
    assert (x - F(1, 2)) * (x + F(1, 2)) == x * x - F(1, 4)
# witnesses: t >= 1 is f1(-t) and f3(t); t in [0, 1] is f2(sqrt t) (perfect squares here)
for k in range(100, 500):
    t = F(k, 100); assert f1(-t) == t and f3(t) == t
for k in range(0, 11):
    s = F(k, 10); t = s * s; assert 0 <= s <= 1 and f2(s) == t
sub = [x for x in grid if -1 <= x <= 1]
assert min(f2(x) for x in sub) == 0 and max(f2(x) for x in sub) == 1
print("exr-restriction-extension-and-gluing-b1: all quoted values check")
