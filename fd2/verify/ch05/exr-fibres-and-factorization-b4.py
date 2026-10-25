"""exr-fibres-and-factorization-b4 (d): [a]_4 -> [3a]_12 is well defined and
injective, misses [1]_12; image has 4 elements. (e) id and 2x differ at 1."""

QUOTED = {"missed": 1, "image_size": 4}
R = range(-120, 121)
g = lambda a: (3 * a) % 12
assert all(g(a) == g(b) for a in R for b in R if (a - b) % 4 == 0)
assert all((a - b) % 4 == 0 for a in R for b in R if g(a) == g(b))
img = {g(a) for a in range(4)}
assert len(img) == QUOTED["image_size"] and QUOTED["missed"] not in img
assert img == {0, 3, 6, 9}
assert 1 % 3 == 1 and 1 // 3 == 0
assert 1 != 2 * 1
print("exr-fibres-and-factorization-b4: all quoted values check")
