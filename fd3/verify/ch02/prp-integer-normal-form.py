"""prp-integer-normal-form: on a grid, every pair is related to exactly one pair
with a coordinate 0, and the three cases of (a) give the stated normal form; and the Quick check after
the normal-form paragraph: [(17, 9)] = [(8, 0)], [(9, 17)] = [(0, 8)], third
pairs (18, 10) and (10, 18)."""
QUOTED = {
    "normal_forms": {(17, 9): (8, 0), (9, 17): (0, 8)},
    "third_pairs": {(17, 9): (18, 10), (9, 17): (10, 18)},
    "cross_sum": (17 + 10, 9 + 18),
}


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


M = 25
zero_pairs = {(n, 0) for n in range(2 * M)} | {(0, n) for n in range(2 * M)}
for a in range(M):
    for b in range(M):
        hits = [z for z in zero_pairs if rel((a, b), z)]
        assert len(hits) == 1, (a, b, hits)
        if a > b:
            assert hits[0] == (a - b, 0)
        elif a == b:
            assert hits[0] == (0, 0)
        else:
            assert hits[0] == (0, b - a)
assert 17 == 9 + 8
for p, nf in QUOTED["normal_forms"].items():
    a, b = p
    assert nf == ((a - b, 0) if a >= b else (0, b - a))
    assert rel(p, nf)
for p, t in QUOTED["third_pairs"].items():
    assert rel(p, t) and t != p and t != QUOTED["normal_forms"][p]
s1, s2 = QUOTED["cross_sum"]
assert s1 == s2 == 27
print("prp-integer-normal-form: OK")
