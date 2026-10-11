"""thm-reals-operations-well-defined: the identities behind the sum and the split eq-reals-product-split."""
from fractions import Fraction as F
import random

QUOTED = {"split_identity_holds": True}
random.seed(5)
for _ in range(2000):
    a, a2, b, b2 = (F(random.randint(-50, 50), random.randint(1, 30)) for _ in range(4))
    assert a * b - a2 * b2 == a * (b - b2) + (a - a2) * b2
    assert (a + b) - (a2 + b2) == (a - a2) + (b - b2)
    assert (-a) - (-a2) == -(a - a2)
print("ok")
