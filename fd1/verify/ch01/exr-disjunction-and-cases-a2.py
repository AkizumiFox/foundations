"""exr-disjunction-and-cases-a2 (Section 1.6 drill): (a) |x|^2 = x^2 in each case of
x >= 0 or x < 0; (b) n = 0 lies in neither n > 0 nor n < 0; (e) at x = 0 the split
(x >= 1) or (x <= -1) fails and x^2 >= 1 fails."""
from _grid import grid

QUOTED = {"(b) n": 0, "(e) x": 0}
for x in grid():
    assert x >= 0 or x < 0
    assert abs(x) ** 2 == x ** 2 and (-x) ** 2 == x ** 2
n = QUOTED["(b) n"]
assert not (n > 0 or n < 0)
x = QUOTED["(e) x"]
assert not (x >= 1 or x <= -1) and not x ** 2 >= 1
assert all(t ** 2 >= 1 for t in grid() if t >= 1 or t <= -1)
print("exr-disjunction-and-cases-a2: checks")
