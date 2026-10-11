"""exr-diagonal-arguments-a1 (b): X = {1,2,3}, f(1) = {1,2}, f(2) = {}, f(3) = {1,3};
D = {x : x not in f(x)} = {2}, not a value of f."""

QUOTED = {"D": {2}}
f = {1: {1, 2}, 2: set(), 3: {1, 3}}
D = {x for x in f if x not in f[x]}
assert D == QUOTED["D"] and all(D != f[x] for x in f)
print("exr-diagonal-arguments-a1: all quoted values check")
