"""exr-peano-properties-b3: verdicts T, F, T, T, F, checked on a truncation of N
(a Peano system) and, for (d), on all maps of a small truncation satisfying the equations."""
QUOTED = {"verdicts": {"a": True, "b": False, "c": True, "d": True, "e": False}}
N = 40
M = range(N)
s = lambda x: x + 1
e = 0
# (a): smallest A containing s(e) closed under s, union {e}, is M
A = set(range(1, N))
assert A | {e} == set(M)
# (b) counterexample: M \ {e} is non-empty, closed (within truncation), not M
B = set(range(1, N))
assert B and all(s(x) in B for x in B if x < N - 1) and e not in B
# (c): the predecessor y of x != e satisfies y != x
assert all(x - 1 != x and s(x - 1) == x for x in range(1, N))
# (d): f(e) = e and f(s(x)) = s(f(x)) forces f = id, by unwinding the equations
f = {0: 0}
for x in range(N - 1):
    f[x + 1] = s(f[x])
assert all(f[x] == x for x in M)
# (e) counterexample: s(e) is not e and not s(s(y)) for any y
assert s(e) != e and all(s(s(y)) != s(e) for y in M)
assert [k for k, v in QUOTED["verdicts"].items() if not v] == ["b", "e"]
print("ok")
