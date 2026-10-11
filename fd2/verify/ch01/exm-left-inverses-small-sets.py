"""exm-left-inverses-small-sets (Ch 6, Section 6.5): inclusion e: {1,2} -> {1,2,3}, g, constant c."""
from itertools import product
QUOTED = {"e(g(3))": 2, "g(3)": 2}
e = {1: 1, 2: 2}
g = {1: 1, 2: 2, 3: 2}
assert all(g[e[x]] == x for x in e)                 # g o e = id
assert e[g[3]] == QUOTED["e(g(3))"] != 3               # e o g != id at 3
c = {1: 3, 2: 3}
assert not any(all(dict(zip([1, 2, 3], v))[c[x]] == x for x in c)
               for v in product([1, 2], repeat=3))    # c has no left inverse
print("exm-left-inverses-small-sets: all quoted values check")
