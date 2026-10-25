"""exr-restriction-extension-and-gluing-a1: (a) the image of x^2 on [-1, 2] is [0, 4];
(b) no injection from 3 to 2 elements, one into 3 elements; (d) ind_{1,3} = (1,0,1,0),
(0,1,1,0) is the indicator of {2,3}."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"image": (0, 4), "ind13": (1, 0, 1, 0), "subset0110": {2, 3}}
pts = [F(-1) + F(3 * k, 3000) for k in range(3001)]
vals = [x * x for x in pts]
assert min(vals) == QUOTED["image"][0] and max(vals) == QUOTED["image"][1]
# every t in [0, 4] is attained: t = s^2 with s = sqrt(t) in [0, 2]
for k in range(41):
    t = F(k, 10); s = t ** 0.5
    assert 0 <= s <= 2 and abs(s * s - float(t)) < 1e-12
assert not any(len(set(img)) == 3 for img in product("ab", repeat=3))
assert len({"a", "b", "c"}) == 3
X = (1, 2, 3, 4)
assert tuple(1 if x in {1, 3} else 0 for x in X) == QUOTED["ind13"]
assert {x for x, val in zip(X, (0, 1, 1, 0)) if val == 1} == QUOTED["subset0110"]
print("exr-restriction-extension-and-gluing-a1: all quoted values check")
