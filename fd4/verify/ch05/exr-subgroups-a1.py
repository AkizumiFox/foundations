"""exr-subgroups-a1: 4Z + 6Z = 2Z (2 = 6 - 4; all combinations even); 6 = 3*2 + 0."""
QUOTED = {"n": 2, "div": (6, 3, 0)}
W = range(-40, 41)
comb = {4 * x + 6 * y for x in W for y in W}
assert 6 - 4 == QUOTED["n"] and min(c for c in comb if c > 0) == QUOTED["n"]
assert all(c % 2 == 0 for c in comb) and 1 not in comb
x, q, r = QUOTED["div"]
assert x == q * QUOTED["n"] + r
print("exr-subgroups-a1: ok")
