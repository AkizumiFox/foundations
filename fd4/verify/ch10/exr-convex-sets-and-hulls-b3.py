"""exr-convex-sets-and-hulls-b3 aftermath: max-distance; (1,1) at max-distance 1 from (0,0) and (2,0), which are at
distance 2, yet (1,1) is not on [(0,0),(2,0)]; [(1,-1),(1,1)] lies on max-sphere of radius 1; Euclidean strictness check."""
from fractions import Fraction as F
import random, math
QUOTED = {"pt": (1, 1), "ends": ((0, 0), (2, 0))}
dm = lambda u, v: max(abs(u[0] - v[0]), abs(u[1] - v[1]))
assert dm((0, 0), (1, 1)) == 1 and dm((1, 1), (2, 0)) == 1 and dm((0, 0), (2, 0)) == 2
assert (1, 1)[1] != 0  # not on the segment (second coordinate 0 there)
for k in range(11):
    t = F(k, 10); pt = (1, -1 + 2 * t); assert dm(pt, (0, 0)) == 1
random.seed(4)
for _ in range(2000):
    a, b = random.uniform(0, 6.283), random.uniform(0, 6.283)
    p, q = (math.cos(a), math.sin(a)), (math.cos(b), math.sin(b))
    if math.dist(p, q) < 1e-3: continue
    t = random.uniform(0.01, 0.99)
    assert math.hypot((1 - t) * p[0] + t * q[0], (1 - t) * p[1] + t * q[1]) < 1
print("ok")
