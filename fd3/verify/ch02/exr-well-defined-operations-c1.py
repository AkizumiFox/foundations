"""exr-well-defined-operations-c1: (a) S = {a = 0}: (0,0) in S, (1,1) ~ (0,0) not in S;
(b) x ~ y iff (x = 0 <=> y = 0), g(x, y) = x if y = 1 else 0: first hypothesis
holds on a grid, second fails at x = 5, y = 1, y' = 2."""
import itertools
QUOTED = {"g51": 5, "g52": 0}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
assert rel((1, 1), (0, 0)) and (0, 0)[0] == 0 and (1, 1)[0] != 0
eq = lambda x, y: (x == 0) == (y == 0)
g = lambda x, y: x if y == 1 else 0
R = range(12)
for x, x1, y in itertools.product(R, repeat=3):
    if eq(x, x1):
        assert eq(g(x, y), g(x1, y))
assert eq(1, 2) and g(5, 1) == QUOTED["g51"] and g(5, 2) == QUOTED["g52"] and not eq(5, 0)
print("exr-well-defined-operations-c1: OK")
