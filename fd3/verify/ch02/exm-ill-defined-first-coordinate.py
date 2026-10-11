"""exm-ill-defined-first-coordinate: (0, 2) ~ (1, 3) with first coordinates 0, 1;
[(a, b)] -> [(a + 1, b)] respects ~ and equals x + [(1, 0)]; h([(1, 3)]) = 0."""
import itertools

QUOTED = {"pair1": (0, 2), "pair2": (1, 3), "h_of_class": 0}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
assert rel(QUOTED["pair1"], QUOTED["pair2"]) and QUOTED["pair1"][0] != QUOTED["pair2"][0]
P = [(a, b) for a in range(6) for b in range(6)]
for p, q in itertools.product(P, repeat=2):
    if rel(p, q):
        assert rel((p[0] + 1, p[1]), (q[0] + 1, q[1]))
    assert (p[0] + 1, p[1] + 0) == (p[0] + 1, p[1])
cls = [(x, y) for x in range(40) for y in range(40) if rel((x, y), (1, 3))]
assert min(x for x, _ in cls) == QUOTED["h_of_class"]
print("exm-ill-defined-first-coordinate: OK")
