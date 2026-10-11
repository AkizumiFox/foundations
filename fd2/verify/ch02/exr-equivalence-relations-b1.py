"""exr-equivalence-relations-b1: (a) ad = bc is an equivalence on Z x Z_{>0} (sampled), class of
(1, 2) is {(k, 2k)}; (b) on Z x N: (1,1) ~ (0,0) ~ (2,1) but (1,1) !~ (2,1)."""

QUOTED = {"witness": ((1, 1), (0, 0), (2, 1))}

rel = lambda p, q: p[0] * q[1] == p[1] * q[0]
S = [(a, b) for a in range(-6, 7) for b in range(1, 7)]
assert all(rel(p, p) for p in S)
assert all(rel(q, p) for p in S for q in S if rel(p, q))
assert all(rel(p, r) for p in S for q in S for r in S if rel(p, q) and rel(q, r))
assert {q for q in S if rel(q, (1, 2))} == {(k, 2 * k) for k in range(1, 4)}
x, y, z = QUOTED["witness"]
assert rel(x, y) and rel(y, z) and not rel(x, z)
print("exr-equivalence-relations-b1: all quoted values check")
