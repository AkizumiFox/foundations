"""exr-projection-and-angle-r1: g(t)^2 - g(s)^2 = (t - s)(t + s - 2 t0)||y||^2, and positivity for t0 <= s < t."""
from fractions import Fraction as Fr
import random
QUOTED = {"factor": True}
random.seed(5)
for _ in range(3000):
    D, t0 = Fr(random.randint(0, 20), 3), Fr(random.randint(-20, 20), 4)
    Y2 = Fr(random.randint(1, 20), 2)
    s = t0 + Fr(random.randint(0, 10), 3); t = s + Fr(random.randint(1, 10), 7)
    g2 = lambda u: D + (u - t0) ** 2 * Y2
    assert g2(t) - g2(s) == (t - s) * (t + s - 2 * t0) * Y2 > 0
print("ok")
