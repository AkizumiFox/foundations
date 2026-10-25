"""exr-countable-sets-b3: s(2q + r) = (q, r); s(0..3) = (0,0),(0,1),(1,0),(1,1); bijection onto N x {0,1}."""
QUOTED = {"first": [(0, 0), (0, 1), (1, 0), (1, 1)]}
s = lambda a: divmod(a, 2)
assert [s(a) for a in range(4)] == QUOTED["first"]
N = 2000
assert sorted(s(a) for a in range(2 * N)) == sorted((q, r) for q in range(N) for r in (0, 1))
s2 = lambda a: (a // 2, 1 - a % 2)
assert sorted(s2(a) for a in range(2 * N)) == sorted((q, r) for q in range(N) for r in (0, 1))
print("ok")
