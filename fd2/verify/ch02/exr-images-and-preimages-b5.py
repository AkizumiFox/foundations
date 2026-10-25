"""exr-images-and-preimages-b5: (a) f|_A(B) = f(B) on random finite instances;
(b) the image of x^2 restricted to [-1, 2] is [0, 4]."""
import math
import random
from fractions import Fraction as F

QUOTED = {"image": (0, 4)}

# (a) brute force on small finite sets
random.seed(5)
for _ in range(2000):
    X = list(range(random.randint(1, 6)))
    Y = list(range(random.randint(1, 4)))
    f = {x: random.choice(Y) for x in X}
    A = [x for x in X if random.random() < 0.6]
    B = [a for a in A if random.random() < 0.6]
    f_A = {a: f[a] for a in A}
    assert {f_A[b] for b in B} == {f[b] for b in B}
    assert {f_A[a] for a in A} == {f[a] for a in A}

# (b) values on a fine exact grid of [-1, 2] lie in [0, 4] and reach both ends
pts = [F(-1) + F(3 * k, 3000) for k in range(3001)]
vals = [x * x for x in pts]
assert min(vals) == QUOTED["image"][0] and max(vals) == QUOTED["image"][1]
assert all(QUOTED["image"][0] <= v <= QUOTED["image"][1] for v in vals)
# every t in [0, 4] is (sqrt t)^2 with sqrt t in [0, 2] subset [-1, 2]
for k in range(401):
    t = k / 100
    s = math.sqrt(t)
    assert -1 <= 0 <= s <= 2 and abs(s * s - t) < 1e-12
print("exr-images-and-preimages-b5: all quoted values check")
