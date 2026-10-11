"""exr-addition-c2: A = {r <= 1}: A + D_0 = D_1 (a <= 1, q < 0 give a + q < 1; x = 1 + (x - 1));
the repair witness 1/2 = 3/4 + (-1/4)."""
from fractions import Fraction as Fr
import random

QUOTED = {"split": ("3/4", "-1/4")}
a, b = (Fr(v) for v in QUOTED["split"])
assert a + b == Fr(1, 2) and a < 1 and b < 0
random.seed(11)
for _ in range(5000):
    x = Fr(random.randint(-10**4, 10**4), random.randint(1, 500))
    if x < 1:
        assert Fr(1) <= 1 and x - 1 < 0 and 1 + (x - 1) == x
    av = Fr(random.randint(-10**4, 1000), 1000)
    qv = -Fr(random.randint(1, 10**4), random.randint(1, 500))
    if av <= 1:
        assert av + qv < 1
print("ok")
