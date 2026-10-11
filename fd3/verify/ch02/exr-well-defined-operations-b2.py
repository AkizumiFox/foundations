"""exr-well-defined-operations-b2: (a) [(0,0)] = [(1,1)] with values 0, 2;
(b) doubling respects ~; (c) [(0,1)] = [(1,2)] but (0,1) not ~ (1,4): 4 vs 2."""
import itertools
QUOTED = {"a_values": (0, 2), "c_cross": (4, 2)}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
assert rel((0, 0), (1, 1)) and (0 + 0, 1 + 1) == QUOTED["a_values"]
P = [(a, b) for a in range(6) for b in range(6)]
for p, q in itertools.product(P, repeat=2):
    if rel(p, q):
        assert rel((2 * p[0], 2 * p[1]), (2 * q[0], 2 * q[1]))
assert rel((0, 1), (1, 2))
assert (0 + 4, 1 + 1) == QUOTED["c_cross"] and not rel((0, 1), (1 ** 2, 2 ** 2))
for n in range(20):
    assert 2 * n == n + n
print("exr-well-defined-operations-b2: OK")
