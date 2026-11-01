"""exr-homomorphisms-b2: every x in Z/2Z x Z/2Z has x + x = 0; no isomorphism Z/4Z -> Z/2Z x Z/2Z."""
QUOTED = {"sum": (0, 0)}

from itertools import permutations
V = [(a, b) for a in range(2) for b in range(2)]
assert all(((a + a) % 2, (b + b) % 2) == (0, 0) for a, b in V)
add = lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)
assert not any(all(dict(zip(range(4), img))[(a + b) % 4] == add(img[a], img[b])
                   for a in range(4) for b in range(4)) for img in permutations(V))
assert (1 + 1) % 4 == 2
assert all(((a + a) % 2, (b + b) % 2) == QUOTED["sum"] for a, b in V)
print("ok")
