"""exr-integers-as-classes-c1: the rearrangement in (b),
(a + b') + (c + d') = (a + c) + (b' + d') and (b + a') + (d + c') = (b + d) + (a' + c'),
and an exhaustive check that coordinatewise addition respects ~."""
import itertools

QUOTED = {}

for a, b, a1, b1, c, d, c1, d1 in itertools.product(range(2), repeat=8):
    assert (a + b1) + (c + d1) == (a + c) + (b1 + d1)
    assert (b + a1) + (d + c1) == (b + d) + (a1 + c1)


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


R = range(4)
P = [(a, b) for a in R for b in R]
for p, p1, q, q1 in itertools.product(P, repeat=4):
    if rel(p, p1) and rel(q, q1):
        assert rel((p[0] + q[0], p[1] + q[1]), (p1[0] + q1[0], p1[1] + q1[1]))
print("exr-integers-as-classes-c1: OK")
