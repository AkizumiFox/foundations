"""exr-length-and-distance-b2: a=(1,2), b=(4,6), c=(-3,5): b-a=(3,4), c-a=(-4,3), dot 0; squared sides 25, 25, 50; b-c=(7,1); sqrt50 = 5 sqrt2."""
def dot(x, y): return sum(p * q for p, q in zip(x, y))
def sub(x, y): return tuple(p - q for p, q in zip(x, y))
a, b, c = (1, 2), (4, 6), (-3, 5)
QUOTED = {"ba": (3, 4), "ca": (-4, 3), "sq": (25, 25, 50), "bc": (7, 1)}
assert sub(b, a) == QUOTED["ba"] and sub(c, a) == QUOTED["ca"] and dot(sub(b, a), sub(c, a)) == 0
assert sub(b, c) == QUOTED["bc"] == sub(sub(b, a), sub(c, a))
assert (dot(sub(b, a), sub(b, a)), dot(sub(c, a), sub(c, a)), dot(sub(b, c), sub(b, c))) == QUOTED["sq"]
assert (5 * 5) * 2 == 50 and 5 * 5 == 25  # (5 sqrt2)^2 = 50, 5 >= 0
print("ok")
