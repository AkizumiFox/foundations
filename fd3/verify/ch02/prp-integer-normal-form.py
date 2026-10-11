"""prp-integer-normal-form: on a grid, every pair is related to exactly one pair
with a coordinate 0, and the three cases of (a) give the stated normal form."""
QUOTED = {}


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
print("prp-integer-normal-form: OK")
