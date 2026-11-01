"""exr-bounds-and-suprema-b2: (c) x and 1 - x on (0, 1); (b) on samples."""
from fractions import Fraction as Fr

QUOTED = {"sup_fg": Fr(1, 4), "sup_f_times_sup_g": 1}
pts = [Fr(k, 100) for k in range(1, 100)]      # (0, 1)
fg = [x * (1 - x) for x in pts]
assert max(fg) == QUOTED["sup_fg"] == Fr(1, 2) * Fr(1, 2)
assert all(0 < x < 1 and 0 < 1 - x for x in pts)
assert QUOTED["sup_fg"] != QUOTED["sup_f_times_sup_g"]
# (b) sup max(f, g) = max(sup f, sup g) on samples
f = lambda x: x * x; g = lambda x: 1 - x
assert max(max(f(x), g(x)) for x in pts) == max(max(map(f, pts)), max(map(g, pts)))
print("ok")
