"""exm-naive-negative (Section 7.3) and the fold after def-cut-negative: for q > 0 with q^2 > 2,
q' = (q^2 + 2)/(2q) has q - q' = (q^2 - 2)/(2q) > 0 and q'^2 - 2 = (q^2 - 2)^2/(4q^2) > 0;
the recipe on D_1 gives {x <= -1}, largest element -1; {-p : p in D_1} contains 0, not -2."""
from fractions import Fraction as Fr
import random

QUOTED = {"largest_D1": -1, "in_mirror": 0, "not_in_mirror": -2, "witness": -2}

random.seed(3)
for _ in range(3000):  # the two identities, exactly, at many rational q > 0
    q = Fr(random.randint(1, 10**6), random.randint(1, 10**5))
    qp = (q * q + 2) / (2 * q)
    assert q - qp == (q * q - 2) / (2 * q)
    assert qp * qp - 2 == (q * q - 2) ** 2 / (4 * q * q)
for _ in range(5000):
    v = Fr(random.randint(1, 10**5), random.randint(1, 10**4))
    if v * v > 2:
        w = (v * v + 2) / (2 * v)
        assert 0 < w < v and w * w > 2
# recipe on D_1: {-q : q >= 1} = {x <= -1}; largest element -1
assert -Fr(1) == QUOTED["largest_D1"]
# mirror {-p : p < 1} = {x > -1}
assert QUOTED["in_mirror"] > -1 and not QUOTED["not_in_mirror"] > -1
# -2 in {x < 0, x^2 > 2}, 0 not
w = Fr(QUOTED["witness"])
assert w < 0 and w * w > 2
print("ok")
