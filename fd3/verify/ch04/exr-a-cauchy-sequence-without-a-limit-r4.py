"""exr-a-cauchy-sequence-without-a-limit-r4: a^2 - b^2 = (a - b)(a + b); |a - b| <= |a^2 - b^2|/2 when a, b > 1."""
from fractions import Fraction as F
import random
QUOTED = {"lower": 1, "denominator_bound": 2}
random.seed(4)
for _ in range(5000):
    a = 1 + F(random.randint(1, 400), random.randint(1, 50))
    b = 1 + F(random.randint(1, 400), random.randint(1, 50))
    assert a*a - b*b == (a - b)*(a + b)
    assert abs(a - b) <= abs(a*a - b*b) / 2
assert QUOTED["lower"] + QUOTED["lower"] == QUOTED["denominator_bound"] and F(2, 2) == QUOTED["lower"]
print("ok")
