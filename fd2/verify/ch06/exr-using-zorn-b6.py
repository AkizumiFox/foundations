"""6.3 Exercise B4 (exr-using-zorn-b6): (d) the order x [= y iff y = 0, or
x != 0 and x <= y, is a total order on a window {0, ..., N} of N with greatest
element 0, and every non-empty subset has as least element its least positive
member, or 0 if the subset is {0}. (a) on small sets: every total order on a
finite set has least elements of its non-empty subsets."""
from itertools import combinations, permutations
import random

QUOTED = {"d_greatest": 0}

N = 15
W = list(range(N + 1))


def sq(x, y):
    return y == 0 or (x != 0 and x <= y)


for a in W:
    assert sq(a, a)
    for b in W:
        assert sq(a, b) or sq(b, a)
        if sq(a, b) and sq(b, a):
            assert a == b
        for c in W:
            if sq(a, b) and sq(b, c):
                assert sq(a, c)

assert all(sq(x, QUOTED["d_greatest"]) for x in W)

random.seed(2)
for _ in range(3000):
    S = set(random.sample(W, random.randint(1, 6)))
    ms = [m for m in S if all(sq(m, s) for s in S)]
    assert len(ms) == 1
    pos = [s for s in S if s > 0]
    assert ms[0] == (min(pos) if pos else 0)

# (a): total orders on {1, 2, 3, 4} given by listings; least elements exist
X = [1, 2, 3, 4]
for perm in permutations(X):
    pos = {x: i for i, x in enumerate(perm)}
    for r in range(1, 5):
        for S in combinations(X, r):
            ms = [m for m in S if all(pos[m] <= pos[s] for s in S)]
            assert len(ms) == 1

print("ok")
