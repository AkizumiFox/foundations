"""exr-subfields-b4: the claim of F3.4 is used for (n, k) = (3, 1) and (6, 2): k^2 < n < (k+1)^2;
(a + b sqrt 3)^2 = (a^2 + 3b^2) + 2ab sqrt 3; a = 0 and 3b^2 = 2 give (3b)^2 = 6.
Also a spot check that no small rational squares to 2, 3 or 6."""
from fractions import Fraction as F
import random

QUOTED = {"pairs": [(3, 1), (6, 2)]}
for n, k in QUOTED["pairs"]:
    assert k * k < n < (k + 1) ** 2


def mul3(u, v):
    (a, b), (c, d) = u, v
    return (a * c + 3 * b * d, a * d + b * c)


random.seed(11)
for _ in range(2000):
    a = F(random.randint(-30, 30), random.randint(1, 9))
    b = F(random.randint(-30, 30), random.randint(1, 9))
    assert mul3((a, b), (a, b)) == (a * a + 3 * b * b, 2 * a * b)
    # 3 b^2 = 2  <=>  (3b)^2 = 6
    assert (3 * b * b == 2) == ((3 * b) ** 2 == 6)
    # inverse formula in Q(sqrt 3)
    if (a, b) != (0, 0):
        N = a * a - 3 * b * b
        assert N != 0
        assert mul3((a, b), (a / N, -b / N)) == (1, 0)

for m in range(1, 200):
    for q in range(1, 60):
        x = F(m, q)
        assert x * x not in (2, 3, 6)
print("ok")
