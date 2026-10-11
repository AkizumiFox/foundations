"""exr-sets-and-subsets-a1 (c): {n in Z : 0 < n^2 <= 9} = {-3,-2,-1,1,2,3}."""
QUOTED = {"(c)": (-3, -2, -1, 1, 2, 3), "bound": 16}
S = tuple(sorted(n for n in range(-100, 101) if 0 < n * n <= 9))
assert S == QUOTED["(c)"]
assert min(n * n for n in range(-100, 101) if abs(n) >= 4) == QUOTED["bound"]
print("exr-sets-and-subsets-a1: all quoted values check")
