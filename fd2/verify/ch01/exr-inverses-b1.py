"""exr-inverses-b1 (Ch 6, Section 6.5): count left inverses of f(k)=k and right inverses of g."""
from itertools import product
QUOTED = {"left inverses of f": 2, "right inverses of g": 2}
f = {1: 1, 2: 2}
lefts = [v for v in product([1, 2], repeat=3) if all(v[f[x] - 1] == x for x in f)]
g = {1: 1, 2: 1, 3: 2}
rights = [v for v in product([1, 2, 3], repeat=2) if g[v[0]] == 1 and g[v[1]] == 2]
assert len(lefts) == 2 and sorted(l[2] for l in lefts) == [1, 2]
assert len(rights) == 2 and all(v[1] == 3 for v in rights)
print("exr-inverses-b1: all quoted values check")
