"""exr-inverses-a1 (c) (Ch 6, Section 6.5): f(k) = k + 1 on {1,2,3} -> {1,2,3,4}, x_0 = 3."""
QUOTED = {"g(2)": 1, "g(3)": 2, "g(4)": 3, "g(1)": 3}
X, Y, x0 = [1, 2, 3], [1, 2, 3, 4], 3
f = {k: k + 1 for k in X}
rng = set(f.values())
g = {y: (next(x for x in X if f[x] == y) if y in rng else x0) for y in Y}
assert g == {2: 1, 3: 2, 4: 3, 1: 3}
assert all(g[f[x]] == x for x in X)
print("exr-inverses-a1: all quoted values check")
