"""exr-points-and-coordinates-b2: (a) intersection formula on random boxes; (b) (3/2, 0) is in any box
containing (0,0) and (3,0) but in neither square; also the text's non-example T with (0,1)."""

import random
from fractions import Fraction as Fr

QUOTED = {"witness_b": (Fr(3, 2), 0), "witness_T": (0, 1)}


def in_closed(x, box):
    return all(lo <= xk <= hi for xk, (lo, hi) in zip(x, box))


random.seed(1)
for _ in range(2000):
    n = random.randint(1, 3)
    P = [tuple(sorted(random.sample(range(-4, 5), 2))) for _ in range(n)]
    Q = [tuple(sorted(random.sample(range(-4, 5), 2))) for _ in range(n)]
    M = [(max(p[0], q[0]), min(p[1], q[1])) for p, q in zip(P, Q)]
    for _ in range(30):
        x = tuple(Fr(random.randint(-10, 10), 2) for _ in range(n))
        assert (in_closed(x, P) and in_closed(x, Q)) == in_closed(x, M)
    if any(lo > hi for lo, hi in M):
        grid = [Fr(k, 2) for k in range(-10, 11)]
        from itertools import product
        assert not any(in_closed(x, P) and in_closed(x, Q) for x in product(grid, repeat=n))

w = QUOTED["witness_b"]
sq1, sq2 = [(0, 1), (0, 1)], [(2, 3), (0, 1)]
assert not in_closed(w, sq1) and not in_closed(w, sq2)
assert in_closed((0, 0), sq1) and in_closed((3, 0), sq2)
# smallest box containing (0,0) and (3,0) is [0,3] x [0,0]; w lies in it, hence in every larger one
assert in_closed(w, [(0, 3), (0, 0)])

T = lambda x: 0 <= x[1] <= x[0] <= 1
assert T((0, 0)) and T((1, 1)) and not T(QUOTED["witness_T"])
assert in_closed(QUOTED["witness_T"], [(0, 1), (0, 1)])
# open box containing (0,0) and (1,1): p_i < 0, q_i > 1, so (0,1) is inside it
in_open = lambda x, box: all(lo < xk < hi for xk, (lo, hi) in zip(x, box))
for pq in [[(Fr(-1, 10), Fr(11, 10))] * 2, [(-5, 2), (Fr(-1, 3), 7)]]:
    assert in_open((0, 0), pq) and in_open((1, 1), pq) and in_open(QUOTED["witness_T"], pq)
print("exr-points-and-coordinates-b2: OK")
