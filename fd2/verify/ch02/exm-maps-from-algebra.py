"""exm-maps-from-algebra (a)-(c) (F2.6 §02)."""
QUOTED = {"(1,2) and (2,1) go to": 2}

W = range(-40, 41)
for a in [x for x in range(-6, 7) if x != 0]:
    for b in range(-6, 7):
        img = {a * n + b for n in range(-400, 401)}
        # injective
        assert len(img) == len(range(-400, 401))
        if a in (1, -1):
            assert all(a * (a * (m - b)) + b == m for m in W)   # n := a(m - b)
        else:
            assert abs(a) >= 2
            assert all(a * n + b != b + 1 for n in range(-400, 401))  # b + 1 missed
# (b)
assert 1 * 2 == 2 * 1 == QUOTED["(1,2) and (2,1) go to"]
assert all(k * 1 == k for k in range(100))
# (c) phi bijective on a window
pairs = [(q, r) for q in range(-100, 101) for r in (0, 1)]
vals = [2 * q + r for (q, r) in pairs]
assert len(set(vals)) == len(vals)
assert all(n in set(vals) for n in range(-199, 200))
print("exm-maps-from-algebra: all quoted values check")
