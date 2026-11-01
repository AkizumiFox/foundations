"""C1 stem: circle through (0,0), (4,0), (0,2): centre (2,1), radius^2 = 5; determinant identity."""
import random
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from _hyperplanes_rn import Fr, vec, dot, sub, mul, nsq

QUOTED = {"c1": 8, "c2": -6, "centre": (2, 1), "radius_sq": 5}
p, q, s = vec(0, 0), vec(4, 0), vec(0, 2)
c1 = (nsq(q) - nsq(p)) / 2
c2 = (nsq(s) - nsq(q)) / 2
# non-collinear: s is off the line x2 = 0 through p and q
assert p[1] == q[1] == 0 and s[1] != 0
assert (c1, c2) == (QUOTED["c1"], QUOTED["c2"])
z = vec(*QUOTED["centre"])
assert dot(sub(q, p), z) == c1 and dot(sub(s, q), z) == c2
assert nsq(sub(z, p)) == nsq(sub(z, q)) == nsq(sub(z, s)) == QUOTED["radius_sq"]
# D for rotated directions equals D for normals
random.seed(4)
for _ in range(100):
    a = [random.randint(-9, 9) for _ in range(2)]
    b = [random.randint(-9, 9) for _ in range(2)]
    D = a[0] * b[1] - a[1] * b[0]
    ra, rb = (-a[1], a[0]), (-b[1], b[0])
    assert ra[0] * rb[1] - ra[1] * rb[0] == D
print("ok")
