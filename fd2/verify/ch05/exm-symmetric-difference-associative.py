"""exm-symmetric-difference-associative: both bracketings expand to
u + v + w - 2uv - 2uw - 2vw + 4uvw; the value is 1 exactly for an odd number of ones
(1 -> 1, 2 -> 2 - 2 = 0, 3 -> 3 - 6 + 4 = 1). Polynomial identities of degree <= 2 in each
variable are checked on a 7 x 7 x 7 integer grid, which proves them."""
from itertools import product, combinations

def expansion(u, v, w):
    return u + v + w - 2*u*v - 2*u*w - 2*v*w + 4*u*v*w

QUOTED = {"expansion": expansion, "coeff_pair": -2, "coeff_triple": 4, "two_ones": 0, "three_ones": 1}
d = lambda a, b: a + b - 2*a*b
G = range(-3, 4)
for u, v, w in product(G, repeat=3):
    e = QUOTED["expansion"](u, v, w)
    assert d(d(u, v), w) == e
    assert d(u, d(v, w)) == e
    assert e == expansion(v, u, w) == expansion(w, v, u) == expansion(u, w, v)
for a, b, c in product((0, 1), repeat=3):
    assert expansion(a, b, c) == (a + b + c) % 2
assert expansion(1, 1, 0) == QUOTED["two_ones"] == 2 - 2
assert expansion(1, 1, 1) == QUOTED["three_ones"] == 3 - 6 + 4
assert expansion(1, 1, 0) - expansion(1, 0, 0) - expansion(0, 1, 0) == QUOTED["coeff_pair"]
assert expansion(1, 1, 1) - 3 - 3 * QUOTED["coeff_pair"] == QUOTED["coeff_triple"]
X = (0, 1, 2)
subs = [frozenset(cc) for r in range(4) for cc in combinations(X, r)]
for A, B, C in product(subs, repeat=3):
    assert (A ^ B) ^ C == A ^ (B ^ C)
print("exm-symmetric-difference-associative: all quoted values check")
