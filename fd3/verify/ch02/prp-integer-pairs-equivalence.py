"""prp-integer-pairs-equivalence: the rearrangement in the transitivity step,
(a + d) + (c + f) = (a + f) + (c + d) and (b + c) + (d + e) = (b + e) + (c + d),
and an exhaustive check that ~ is an equivalence relation on {0..5}^2."""
import itertools
import random

QUOTED = {}

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
print("prp-integer-pairs-equivalence: OK")
