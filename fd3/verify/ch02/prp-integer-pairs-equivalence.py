"""prp-integer-pairs-equivalence: the rearrangement in the transitivity step,
(a + d) + (c + f) = (a + f) + (c + d) and (b + c) + (d + e) = (b + e) + (c + d),
an exhaustive check that ~ is an equivalence relation on {0..5}^2, and the
Quick check after the proposition: (4, 4) ~ (0, 0), and the classes of (4, 0),
(0, 4), (0, 0) are pairwise distinct (cross sums quoted)."""
import itertools
import random

QUOTED = {
    # (p, q, cross sum p0 + q1, cross sum p1 + q0, related?)
    "check": [((4, 4), (0, 0), 4, 4, True),
              ((4, 0), (0, 4), 8, 0, False),
              ((4, 0), (0, 0), 4, 0, False),
              ((0, 4), (0, 0), 0, 4, False)],
}

# linear identities: checking on {0,1}^6 plus random points proves them
pts = list(itertools.product(range(2), repeat=6)) + [
    tuple(random.randint(0, 10**6) for _ in range(6)) for _ in range(200)]
for a, b, c, d, e, f in pts:
    assert (a + d) + (c + f) == (a + f) + (c + d)
    assert (b + c) + (d + e) == (b + e) + (c + d)


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


R = range(6)
P = [(a, b) for a in R for b in R]
assert all(rel(p, p) for p in P)
assert all(rel(q, p) for p in P for q in P if rel(p, q))
assert all(rel(p, r) for p in P for q in P for r in P if rel(p, q) and rel(q, r))
for p, q, s1, s2, related in QUOTED["check"]:
    assert p[0] + q[1] == s1 and p[1] + q[0] == s2, (p, q)
    assert rel(p, q) == related, (p, q)
# distinct classes are disjoint: no pair on a grid is related to two of them
reps = [(4, 0), (0, 4), (0, 0)]
G = [(a, b) for a in range(30) for b in range(30)]
assert all(sum(rel(g, r) for r in reps) <= 1 for g in G)
print("prp-integer-pairs-equivalence: OK")
