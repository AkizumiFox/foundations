"""exr-gcd-and-bezout-a1 (b): d = 6 = 12*(-3) + 42*1; 12 = 2*6 + 0, 42 = 7*6 + 0."""
QUOTED = {"d": 6, "x0": -3, "y0": 1, "q12": 2, "q42": 7}
assert 12 * QUOTED["x0"] + 42 * QUOTED["y0"] == QUOTED["d"]
assert 12 == QUOTED["q12"] * 6 and 42 == QUOTED["q42"] * 6
S = {12 * x + 42 * y for x in range(-30, 31) for y in range(-30, 31)}
assert min(v for v in S if v > 0) == 6
print("ok")
