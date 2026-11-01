"""exr-real-functions-and-graphs-b2: 2|x - 1| - 3 has vertex (1, -3) and zeros -1/2, 5/2."""
from fractions import Fraction as Fr

QUOTED = {"vertex": (Fr(1), Fr(-3)), "zeros": [Fr(-1, 2), Fr(5, 2)]}
h = lambda x: 2 * abs(x - 1) - 3
grid = [Fr(k, 4) for k in range(-40, 41)]
m = min(h(x) for x in grid)
assert [x for x in grid if h(x) == m] == [QUOTED["vertex"][0]] and m == QUOTED["vertex"][1]
assert [x for x in grid if h(x) == 0] == QUOTED["zeros"]
# h(x) <= 0 exactly between the zeros, so there are no other zeros: h is 2|x - 1| - 3, piecewise linear
for x in grid:
    assert (h(x) == 0) == (abs(x - 1) == Fr(3, 2))
print("exr-real-functions-and-graphs-b2: ok")
