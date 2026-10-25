"""exr-cardinal-arithmetic-b4: the finite counterexamples of (b), (c), (e) and the maps of (a)."""
import itertools

QUOTED = {"b_left": 2, "b_right": 4, "c_left": 1, "c_right": 0}


def nfuncs(nX, nY):
    return len(list(itertools.product(range(nY), repeat=nX)))


# (b) X = {0,1}, Y = Z = {0}: |X^(Y u Z)| = 2, |X^Y x X^Z| = 4
assert nfuncs(1, 2) == QUOTED["b_left"]
assert nfuncs(1, 2) * nfuncs(1, 2) == QUOTED["b_right"]
# (c) X = empty, Y = empty, Y' = {0}
assert nfuncs(0, 0) == QUOTED["c_left"] and nfuncs(1, 0) == QUOTED["c_right"]
# (a) {0} u N -> N: (0,0) -> 0, (n,1) -> n+1, with the stated inverse, on a range
f = lambda t: 0 if t == (0, 0) else t[0] + 1
g = lambda m: (0, 0) if m == 0 else (m - 1, 1)
src = [(0, 0)] + [(n, 1) for n in range(300)]
assert all(g(f(t)) == t for t in src) and all(f(g(m)) == m for m in range(301))
# (e) {0,1} x N -> N u N -> N: (r, n) -> (n, r) -> 2n + r
h = lambda r, n: 2 * n + r
assert sorted(h(r, n) for r in (0, 1) for n in range(200)) == list(range(400))
print("ok")
