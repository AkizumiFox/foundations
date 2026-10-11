"""exr-categoricity-r3: no f : {0, 1} -> omega with f(0) = 0 and f(s(x)) = S(f(x)),
s(0) = s(1) = 1 (checked for values below 50); and n != S(n) on numerals."""
E0 = frozenset()
def S(x): return x | frozenset([x])
QUOTED = {"f(1) from x = 0": 1}
BOUND = 50
s = {0: 1, 1: 1}
for f1 in range(BOUND):
    f = {0: 0, 1: f1}
    assert not all(f[s[x]] == f[x] + 1 for x in (0, 1))
assert (0 + 1) == QUOTED["f(1) from x = 0"]   # f(1) = f(s(0)) = S(f(0)) = S(0) = 1
x = E0
for _ in range(10):
    assert x != S(x) and x in S(x) and x not in x
    x = S(x)
print("ok")
