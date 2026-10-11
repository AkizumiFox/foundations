"""prp-naturals-embed-integers: iota(m)+iota(n) = iota(m+n), iota(m)iota(n) = iota(mn),
neutral elements, [(a, b)] = iota(a) + (-iota(b)), and 5 + x = 3 solved by [(0, 2)]."""
QUOTED = {"solution": (0, 2), "sum": (5, 2), "normal": (3, 0)}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
add = lambda p, q: (p[0] + q[0], p[1] + q[1])
mul = lambda p, q: (p[0] * q[0] + p[1] * q[1], p[0] * q[1] + p[1] * q[0])
iota = lambda n: (n, 0)
neg = lambda p: (p[1], p[0])
for m in range(8):
    for n in range(8):
        assert add(iota(m), iota(n)) == iota(m + n)
        assert mul(iota(m), iota(n)) == iota(m * n)
        assert add(iota(m), neg(iota(n))) == (m, n)
        x = (m, n)
        assert add(x, iota(0)) == x and mul(iota(1), x) == x
s = add((5, 0), QUOTED["solution"])
assert s == QUOTED["sum"] and rel(s, QUOTED["normal"]) and rel(QUOTED["normal"], (3, 0))
print("prp-naturals-embed-integers: OK")
