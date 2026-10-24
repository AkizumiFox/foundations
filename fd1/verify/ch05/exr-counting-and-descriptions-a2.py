"""exr-counting-and-descriptions-a2 (Section 5.8, drill): (i) on A = {2, 3, 4} ordered by
divisibility, the maximal elements are 3 and 4 and there is no maximum; (j) for m in (0, 1],
m/2 is in (0, 1] and smaller, so (0, 1] has no least element; (f) x + x = x only at x = 0 in N;
(k) 0 * y = 0, and x * y = 1 has the one solution 1/x for x != 0; (l) c + 3 = 5 gives c = 2;
(a) x + 1 = 3 only at x = 2."""
from fractions import Fraction as Fr

QUOTED = {"maximal": {3, 4}, "maximum": None, "c": 2}

A = {2, 3, 4}
div = lambda a, b: b % a == 0                                            # b is a multiple of a
maximal = {m for m in A if not any(div(m, a) and a != m for a in A)}
maximum = [m for m in A if all(div(a, m) for a in A)]
assert maximal == QUOTED["maximal"] and maximum == []

grid = [Fr(p, q) for q in range(1, 40) for p in range(1, q + 1)]        # points of (0, 1]
assert all(0 < m / 2 < m <= 1 for m in grid)
assert [x for x in range(0, 200) if x + x == x] == [0]
assert all(0 * y == 0 for y in range(-20, 21))
for x in [Fr(p, q) for p in range(-20, 21) if p for q in range(1, 6)]:
    ys = [Fr(1) / x]
    assert x * ys[0] == 1
assert [c for c in range(-50, 51) if c + 3 == 5] == [QUOTED["c"]]
assert [x for x in range(-50, 51) if x + 1 == 3] == [2]
print("exr-counting-and-descriptions-a2: all quoted values check")
