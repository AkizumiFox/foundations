"""exr-lines-and-segments-b2: elimination sD = d1 v2' - d2 v1', tD = d1 v2 - d2 v1; back-substitution; (a) lambda (random exact)."""
import random
from fractions import Fraction as Fr

random.seed(11)
R = lambda: Fr(random.randint(-9, 9), random.randint(1, 5))
checked = 0
while checked < 500:
    v1, v2, w1, w2, d1, d2, s0, t0 = (R() for _ in range(8))
    D = v1 * w2 - v2 * w1
    # eliminations hold identically for any (s, t)
    e1 = s0 * v1 - t0 * w1 - d1; e2 = s0 * v2 - t0 * w2 - d2
    assert e1 * w2 - e2 * w1 == s0 * D - (d1 * w2 - d2 * w1)
    assert e1 * v2 - e2 * v1 == t0 * D - (d1 * v2 - d2 * v1)
    if D == 0:
        continue
    S = (d1 * w2 - d2 * w1) / D; T = (d1 * v2 - d2 * v1) / D
    assert S * v1 - T * w1 == d1 and S * v2 - T * w2 == d2
    checked += 1
# (a): D = 0 with v != 0 gives a multiple
for _ in range(500):
    v1, v2, L = R(), R(), R()
    if v1 == 0 and v2 == 0:
        continue
    w1, w2 = L * v1, L * v2
    assert v1 * w2 - v2 * w1 == 0
    lam = w1 / v1 if v1 != 0 else w2 / v2
    assert (lam * v1, lam * v2) == (w1, w2)
print("ok")
