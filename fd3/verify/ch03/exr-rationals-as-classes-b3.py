"""exr-rationals-as-classes-b3 (Section 3.1): Prove or disprove.
(a) [(p,q)] -> [(p+2q, 2q)] respects ~ (cross-products 2pq'+4qq', 2p'q+4qq'; brute force);
(b) [(p,q)] -> [(p,q^2)] fails at [(1,1)] = [(2,2)];
(c) xy = 0 => x = 0 or y = 0 (brute force on pairs);
(d) 2 = [(2,1)] has no representative (1, s)."""
from fractions import Fraction
from itertools import product

rel = lambda x, y: x[0] * y[1] == y[0] * x[1]
W = [(p, q) for p in range(-12, 13) for q in range(1, 13)]

QUOTED = {"b_witness": ((1, 1), (2, 2), (2, 4))}

# (a) true: the rule respects ~ on a window, and the identity behind it
fa = lambda x: (x[0] + 2 * x[1], 2 * x[1])
for x, y in product(W, repeat=2):
    if rel(x, y):
        assert rel(fa(x), fa(y))
        p, q = x; p2, q2 = y
        assert (p + 2*q) * (2*q2) == 2*p*q2 + 4*q*q2
        assert (p2 + 2*q2) * (2*q) == 2*p2*q + 4*q*q2
    # value is x/2 + 1
    assert Fraction(*fa(x)) == Fraction(*x) / 2 + 1

# (b) false
x1, x2, img2 = QUOTED["b_witness"]
fb = lambda x: (x[0], x[1] ** 2)
assert rel(x1, x2) and fb(x1) == (1, 1) and fb(x2) == img2 and not rel(fb(x1), fb(x2))
assert 1 * 4 != 2 * 1

# (c) true
for x, y in product(W, repeat=2):
    if x[0] * y[0] == 0:   # xy = [(pr, qs)] is zero iff pr = 0
        assert x[0] == 0 or y[0] == 0

# (d) false: no s > 0 with (1, s) ~ (2, 1), i.e. 1 = 2s
assert not any(rel((1, s), (2, 1)) for s in range(1, 1000))
assert all(2 * s != 1 for s in range(-1000, 1000))
print("exr-rationals-as-classes-b3: all quoted values check")
