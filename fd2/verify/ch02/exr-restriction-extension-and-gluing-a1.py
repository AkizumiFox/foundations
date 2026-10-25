"""exr-restriction-extension-and-gluing-a1: (a) x^2 is injective on (-inf, 0], not on [-1, 2]
(f(-1) = 1 = f(1)); (b) g: {1,2} -> {a,b,c} has three extensions to {1,2,3}, one injective
(3 -> c); (d) ind_{1,3} = (1,0,1,0), (0,1,1,0) is the indicator of {2,3}."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"collision": (-1, 1, 1), "extensions": 3, "injective": ["c"],
          "ind13": (1, 0, 1, 0), "subset0110": {2, 3}}
neg = [F(-k, 50) for k in range(0, 301)]
sq = [x * x for x in neg]
assert len(set(sq)) == len(neg)  # injective on a grid of (-inf, 0]
for x1 in neg[:60]:
    for x2 in neg[:60]:
        assert ((-x1) ** 2 == x1 ** 2) and (x1 * x1 != x2 * x2 or x1 == x2)
a, b, v = QUOTED["collision"]
assert -1 <= a <= 2 and -1 <= b <= 2 and a * a == v == b * b and a != b
g = {1: "a", 2: "b"}
exts = [{**g, 3: z} for z in "abc"]
assert len(exts) == QUOTED["extensions"]
# every function {1,2,3} -> {a,b,c} agreeing with g is one of these
allf = [dict(zip((1, 2, 3), vals)) for vals in product("abc", repeat=3)]
assert sorted(map(str, [h for h in allf if h[1] == "a" and h[2] == "b"])) == sorted(map(str, exts))
assert [e[3] for e in exts if len(set(e.values())) == 3] == QUOTED["injective"]
X = (1, 2, 3, 4)
assert tuple(1 if x in {1, 3} else 0 for x in X) == QUOTED["ind13"]
assert {x for x, val in zip(X, (0, 1, 1, 0)) if val == 1} == QUOTED["subset0110"]
print("exr-restriction-extension-and-gluing-a1: all quoted values check")
