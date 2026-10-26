"""exm-cut-with-largest-element: E_1 = {r <= 1}; E_1 + D_1 = D_2 = D_1 + D_1 checked on a grid:
s < 2 is 1 + (s - 1) with s - 1 < 1, and s/2 + s/2 with s/2 < 1; a <= 1, b < 1 give a + b < 2."""
from fractions import Fraction as F
QUOTED = {"largest": 1, "sum_bound": 2}
assert QUOTED["largest"] == 1 and QUOTED["sum_bound"] == 1 + 1

grid = [F(n, 13) for n in range(-60, 60)]
E1 = [r for r in grid if r <= 1]
D1 = [r for r in grid if r < 1]
for a in E1:
    for b in D1:
        assert a + b < 2
for s in grid:
    if s < 2:
        assert s - 1 < 1 and s == 1 + (s - 1)
        assert s / 2 < 1 and s == s / 2 + s / 2
assert 1 in E1 and 1 not in D1
print("ok")
