"""exr-the-least-upper-bound-property-b3 (Section 5.5).
(e): A = {0, 1}, Step 1's start for a_0 = 0, M = 1: l_0 = -1/2, u_0 = 3/2 (so -1 < l_0 < 0, 1 < u_0 < 2);
changed rule "(c, u) if c in A, (l, c) otherwise": c = 1/2 not in A, (l_1, u_1) = (-1/2, 1/2), every later
u_k <= 1/2 (new s <= 1/2 < 1); the original rule's u_k stay >= 1 = sup A.
(d): A = {0}: every l_k < 0 under the original rule, from several allowed starts."""
from fractions import Fraction as F
QUOTED = {"l0": F(-1, 2), "u0": F(3, 2), "pair1": (F(-1, 2), F(1, 2)), "bound": F(1, 2)}
A = [F(0), F(1)]
a0, M = F(0), F(1)
l, u = QUOTED["l0"], QUOTED["u0"]
assert a0 - 1 < l < a0 and M < u < M + 1
ends = [(l, u)]
for k in range(50):
    c = (l + u) / 2
    nl, nu = (c, u) if c in A else (l, c)
    assert l <= nl < nu <= u and nu - nl == (u - l) / 2
    l, u = nl, nu
    ends.append((l, u))
assert ends[1] == QUOTED["pair1"]
assert all(uk <= QUOTED["bound"] for _, uk in ends[1:])
# original rule converges to sup A = 1
ub = lambda c: all(a <= c for a in A)
l, u = QUOTED["l0"], QUOTED["u0"]
for k in range(50):
    assert ub(u) and not ub(l) and u >= 1
    c = (l + u) / 2
    l, u = (l, c) if ub(c) else (c, u)
# (d) A = {0}
for l0, u0 in [(F(-1, 2), F(1, 2)), (F(-3, 4), F(5, 3)), (F(-1, 100), F(1, 7))]:
    l, u = l0, u0
    for k in range(50):
        assert l < 0 <= u
        c = (l + u) / 2
        l, u = (l, c) if c >= 0 else (c, u)
print("ok")
