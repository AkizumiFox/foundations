"""exr-integers-as-classes-b1: which of (Eq1)-(Eq3) hold for the three relations,
with the quoted witnesses, checked exhaustively on {0..4}^2."""
import itertools

QUOTED = {
    "r1": {"refl": False, "sym": True, "trans": False},
    "r2": {"refl": True, "sym": True, "trans": True},
    "r3": {"refl": True, "sym": False, "trans": True},
}
r1 = lambda p, q: p[0] + q[0] == p[1] + q[1]
r2 = lambda p, q: p[0] + 2 * q[1] == 2 * p[1] + q[0]
r3 = lambda p, q: p[0] + q[1] <= p[1] + q[0]

R = range(5)
P = [(a, b) for a in R for b in R]


def props(r):
    return {
        "refl": all(r(p, p) for p in P),
        "sym": all(r(q, p) for p in P for q in P if r(p, q)),
        "trans": all(r(p, s) for p in P for q in P for s in P if r(p, q) and r(q, s)),
    }


for name, r in (("r1", r1), ("r2", r2), ("r3", r3)):
    assert props(r) == QUOTED[name], (name, props(r))

# witnesses quoted in the solution
assert not r1((0, 1), (0, 1)) and r1((0, 1), (1, 0)) and r1((1, 0), (0, 1))
assert all(r1((a, b), (b, a)) for a, b in P)
assert r3((0, 1), (0, 0)) and not r3((0, 0), (0, 1))
# rearrangement identities in (b) and (c)
for a, b, c, d, e, f in itertools.product(range(3), repeat=6):
    assert (a + 2 * d) + (c + 2 * f) == (a + 2 * f) + (2 * d + c)
    assert (2 * b + c) + (2 * d + e) == (2 * b + e) + (2 * d + c)
    assert (a + d) + (c + f) == (a + f) + (c + d)
    assert (b + c) + (d + e) == (b + e) + (c + d)
print("exr-integers-as-classes-b1: OK")
