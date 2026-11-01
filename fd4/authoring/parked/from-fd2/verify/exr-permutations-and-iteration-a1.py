"""exr-permutations-and-iteration-a1: tables for (1 4)(2 3 5), its inverse and square; m = 1, p = 3."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import compose, tail_and_period, orbits

QUOTED = {"sigma": [4, 3, 5, 1, 2], "inv": [4, 5, 2, 1, 3], "sq": [1, 5, 2, 4, 3],
          "inv_cycles": [[1, 4], [2, 5, 3]], "sq_cycles": [[2, 5, 3]], "m": 1, "p": 3}
X = [1, 2, 3, 4, 5]
def cyc(*c):
    d = {x: x for x in X}
    for i, x in enumerate(c):
        d[x] = c[(i + 1) % len(c)]
    return d
sigma = compose(cyc(1, 4), cyc(2, 3, 5))  # right factor first
inv = {v: k for k, v in sigma.items()}
sq = compose(sigma, sigma)
assert [sigma[x] for x in X] == QUOTED["sigma"]
assert [inv[x] for x in X] == QUOTED["inv"]
assert [sq[x] for x in X] == QUOTED["sq"]
assert inv == compose(cyc(1, 4), cyc(2, 5, 3))
assert [o for o in orbits(sq, X) if len(o) > 1] == QUOTED["sq_cycles"]
f = {1: 2, 2: 3, 3: 4, 4: 2, 5: 5}
m, p, seq = tail_and_period(f, 1, 5)
assert (m, p) == (QUOTED["m"], QUOTED["p"]) and seq[:5] == [1, 2, 3, 4, 2]
print("exr-permutations-and-iteration-a1: all quoted values check")
