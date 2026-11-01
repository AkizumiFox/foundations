"""prp-weierstrass-product (03): prod (1 - a_k) >= 1 - sum a_k for a_k in [0,1]; Quick check
0.99*0.98*0.97*0.96 >= 0.90, actual about 0.9035."""
from fractions import Fraction as Fr
import random
QUOTED = {"sum": Fr(10, 100), "bound": Fr(90, 100), "actual_approx": 0.9035}
a = [Fr(1, 100), Fr(2, 100), Fr(3, 100), Fr(4, 100)]
assert sum(a) == QUOTED["sum"] and 1 - sum(a) == QUOTED["bound"]
p = Fr(1)
for ak in a:
    p *= 1 - ak
assert p == Fr(99 * 98 * 97 * 96, 100 ** 4)
assert p >= QUOTED["bound"]
assert abs(float(p) - QUOTED["actual_approx"]) < 5e-5, float(p)
random.seed(1)
for _ in range(3000):
    n = random.randint(0, 8)
    xs = [Fr(random.randint(0, 20), 20) for _ in range(n)]
    q = Fr(1)
    for x in xs:
        q *= 1 - x
    assert q >= 1 - sum(xs)
# identity in the step
for s in [Fr(0), Fr(1, 3), Fr(5, 2)]:
    for t in [Fr(0), Fr(1, 2), Fr(1)]:
        assert (1 - s) * (1 - t) == 1 - s - t + s * t
print("ok")
