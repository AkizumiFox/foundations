"""exr-well-defined-operations-b1: both rules respect ~; (b) is the constant 0."""
import itertools
QUOTED = {}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
P = [(a, b) for a in range(6) for b in range(6)]
for p, q in itertools.product(P, repeat=2):
    if rel(p, q):
        assert rel((p[1], p[0]), (q[1], q[0]))
    s = p[0] + p[1]
    assert rel((s, s), (0, 0))
print("exr-well-defined-operations-b1: OK")
