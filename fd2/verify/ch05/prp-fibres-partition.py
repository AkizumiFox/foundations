"""prp-fibres-partition: its Quick check and the same-size payoff (fold "Same size, revisited").
(1) n^2 - 2n on {-1, ..., 3}: values 3, 0, -1, 0, 3; classes {-1,3}, {0,2}, {1}; image {-1, 0, 3}.
(2) sizes of subsets of {1,2,3}: four fibers, image {0,1,2,3}.
Also checks prp-fibres-partition (b) on these: number of classes = size of image."""
from itertools import combinations

QUOTED = {
    "values": {-1: 3, 0: 0, 1: -1, 2: 0, 3: 3},
    "classes": {frozenset({-1, 3}), frozenset({0, 2}), frozenset({1})},
    "image": {-1, 0, 3},
    "subset_fibers": 4,
    "subset_image": {0, 1, 2, 3},
}


def fibers(dom, f):
    return {frozenset(x for x in dom if f(x) == f(a)) for a in dom}


X = range(-1, 4)
f = lambda n: n * n - 2 * n
assert {n: f(n) for n in X} == QUOTED["values"]
assert fibers(X, f) == QUOTED["classes"]
assert {f(n) for n in X} == QUOTED["image"]
assert len(fibers(X, f)) == len(QUOTED["image"])

subs = [frozenset(c) for k in range(4) for c in combinations((1, 2, 3), k)]
assert len(subs) == 8
assert len(fibers(subs, len)) == QUOTED["subset_fibers"]
assert {len(s) for s in subs} == QUOTED["subset_image"]
print("prp-fibres-partition: all quoted values check")
