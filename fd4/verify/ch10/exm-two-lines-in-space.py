"""exm-two-lines-in-space: L1, L2 skew; L1, L3 meet at (2,1,1) with s = 1, u = 0 (exact, no CAS)."""
from fractions import Fraction as Fr

QUOTED = {"meet": (2, 1, 1), "s": 1, "u": 0, "forced_s": 2, "forced_t": 1}
L1 = lambda s: (1 + s, s, 1)
L2 = lambda t: (t, 2, t)
L3 = lambda u: (2, 1 + u, 1 + u)
# L1 = L2: coordinates 2 and 3 force s = 2, t = 1; coordinate 1 then fails
s, t = Fr(2), Fr(1)
assert (s, t) == (QUOTED["forced_s"], QUOTED["forced_t"])
assert L1(s)[1:] == L2(t)[1:] and L1(s)[0] == 3 != L2(t)[0] == 1
# directions not multiples either way
a, b = (1, 1, 0), (1, 0, 1)
assert not (a[0] == b[0] * 1 and a[2] == b[2] * 1)  # lambda = 1 from coord 1 fails coord 3
assert not all(b[i] * Fr(a[0], 1) == b[i] * 0 for i in range(3))
lam1 = Fr(a[0], b[0]); assert tuple(lam1 * c for c in b) != a
mu = Fr(b[0], a[0]); assert tuple(mu * c for c in a) != b
# L1 = L3: coord 3 gives u = 0, coord 2 gives s = 1, coord 1 checks
u = Fr(0); s = 1 + u
assert (s, u) == (QUOTED["s"], QUOTED["u"]) and L1(s) == L3(u) == QUOTED["meet"]
print("ok")
