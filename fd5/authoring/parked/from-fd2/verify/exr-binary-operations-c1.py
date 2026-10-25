"""exr-binary-operations-c1: the five bracketings of abcd agree for associative operations
(sampled on composition of maps {0,1,2} -> {0,1,2}); and they need not agree for a
non-associative one (exm-two-inverses' table), showing associativity is used."""
from itertools import product

maps = list(product(range(3), repeat=3))
comp = lambda u, v: tuple(u[v[i]] for i in range(3))
def five(op, a, b, c, d):
    return [op(op(op(a, b), c), d), op(op(a, op(b, c)), d), op(op(a, b), op(c, d)),
            op(a, op(op(b, c), d)), op(a, op(b, op(c, d)))]
import random
QUOTED = {"bracketings": 5}

random.seed(1)
for _ in range(3000):
    a, b, c, d = (random.choice(maps) for _ in range(4))
    assert len(set(five(comp, a, b, c, d))) == 1
T = {}
for u in "eab":
    T[("e", u)] = u; T[(u, "e")] = u
for u, v in product("ab", repeat=2):
    T[(u, v)] = "e"
assert any(len(set(five(lambda x, y: T[(x, y)], *q))) > 1 for q in product("eab", repeat=4))
assert len(five(comp, *maps[:4])) == QUOTED["bracketings"]
print("exr-binary-operations-c1: all quoted values check")
