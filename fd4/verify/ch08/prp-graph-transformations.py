"""prp-graph-transformations: the figure (|x - 1| - 2: vertex, zeros) and Quick check 4 (|x + 1| + 2)."""
from fractions import Fraction as Fr

QUOTED = {
    "figure_vertex": (1, -2),
    "figure_zeros": [-1, 3],
    "check4_vertex": (-1, 2),
}

g = lambda x: abs(x - 1) - 2
grid = [Fr(k, 4) for k in range(-40, 41)]
# vertex: the minimum of g, attained only at x = 1
m = min(g(x) for x in grid)
assert (Fr(QUOTED["figure_vertex"][0]), m) == (1, -2) and [x for x in grid if g(x) == m] == [1]
assert [x for x in grid if g(x) == 0] == QUOTED["figure_zeros"]
# (a) with a = 1, b = -2: (x, y) on graph g iff (x - 1, y + 2) on graph |.|
for x in grid:
    assert g(x) + 2 == abs(x - 1)
# Quick check 4: graph |.| + (-1, 2) is the graph of |x + 1| + 2
h = lambda x: abs(x + 1) + 2
for u in grid:
    assert h(u - 1) == abs(u) + 2   # the point (u, |u|) moved by (-1, 2) lies on graph h
m2 = min(h(x) for x in grid)
assert [x for x in grid if h(x) == m2] == [QUOTED["check4_vertex"][0]] and m2 == QUOTED["check4_vertex"][1]
print("prp-graph-transformations: ok")
