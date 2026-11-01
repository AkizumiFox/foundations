"""exr-length-and-distance-a1: (a) ||(2,-3,6)|| = 7, unit vector (2/7,-3/7,6/7); (b) d((1,-1,0),(3,1,1)) = 3 with difference (-2,-2,-1);
(c) x = (2,-1,2,0): M = 2, ||x|| = 3, sqrt4 * 2 = 4; (e) for n >= 2, r/sqrt n < r, any c in [r/sqrt n, r) gives |x_k - a_k| = c < r and
||x - a|| = c sqrt n >= r; c = r/2 works exactly for n >= 4 (n = 4 gives exactly r)."""
from fractions import Fraction as Fr

def dot(x, y): return sum(Fr(a) * Fr(b) for a, b in zip(x, y))
def tup(t): return tuple(Fr(v) for v in t.strip("()").split(", "))
QUOTED = {"a_norm": 7, "a_unit": "(2/7, -3/7, 6/7)", "b_diff": (-2, -2, -1), "b_d": 3, "c": (2, 3, 4)}
assert dot((2, -3, 6), (2, -3, 6)) == 49 == QUOTED["a_norm"] ** 2
assert tuple(Fr(c, 7) for c in (2, -3, 6)) == tup(QUOTED["a_unit"]) and dot(tup(QUOTED["a_unit"]), tup(QUOTED["a_unit"])) == 1
diff = tuple(p - q for p, q in zip((1, -1, 0), (3, 1, 1)))
assert diff == QUOTED["b_diff"] and dot(diff, diff) == QUOTED["b_d"] ** 2
x = (2, -1, 2, 0); M = max(map(abs, x))
assert (M, dot(x, x), 2 * M) == (2, 9, 4) and QUOTED["c"] == (M, 3, 2 * M) and 2 <= 3 <= 4
# (e), on squares (r > 0 scales out; take r = 1): sqrt n > 1 iff n > 1; c = 1/sqrt n gives c^2 n = 1 (exactly r);
# c = 1/2 satisfies c >= 1/sqrt n iff c^2 n >= 1 iff n >= 4, and n = 4 gives c sqrt n = 1 exactly.
for n in range(2, 60):
    assert n > 1                                   # (sqrt n)^2 > 1^2
    assert (Fr(1, 4) * n >= 1) == (n >= 4)
    for c2 in (Fr(1, n), Fr(1, 4), Fr(n + 1, n * n + 1)):  # squares of choices of c
        if Fr(1, n) <= c2 < 1:                     # r/sqrt n <= c < r
            assert c2 * n >= 1                     # ||x - a||^2 = c^2 n >= r^2
assert Fr(1, 4) * 4 == 1
print("ok")
