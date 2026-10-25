"""exr-restriction-extension-and-gluing-b3: (a) u(1 - (v + w - vw)) = u(1-v)(1-w) as polynomials,
and u(1-v)u(1-w) equals it on {0,1}^3 (u^2 = u); (b) u(v + w - 2vw) = uv + uw - 2uvw as
polynomials, and uv + uw - 2(uv)(uw) equals it on {0,1}^3. Set identities checked directly."""
from itertools import product, combinations

QUOTED = {"a": lambda u, v, w: u*(1 - v)*(1 - w), "b": lambda u, v, w: u*v + u*w - 2*u*v*w}
for u, v, w in product(range(-3, 4), repeat=3):
    assert u*(1 - (v + w - v*w)) == QUOTED["a"](u, v, w)
    assert u*(v + w - 2*v*w) == QUOTED["b"](u, v, w)
for u, v, w in product((0, 1), repeat=3):
    assert u*u == u
    assert u*(1 - v)*u*(1 - w) == QUOTED["a"](u, v, w)
    assert u*v + u*w - 2*(u*v)*(u*w) == QUOTED["b"](u, v, w)
X = (0, 1, 2)
subs = [frozenset(c) for r in range(4) for c in combinations(X, r)]
for A, B, C in product(subs, repeat=3):
    assert A - (B | C) == (A - B) & (A - C)
    assert A & (B ^ C) == (A & B) ^ (A & C)
print("exr-restriction-extension-and-gluing-b3: all quoted values check")
