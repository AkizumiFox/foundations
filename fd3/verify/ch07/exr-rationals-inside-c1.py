"""exr-rationals-inside-c1 (Section 7.5): 3/2 > 0 and (3/2)^2 = 9/4 > 2, so 3/2 is not in sigma;
and the affine solve: gamma = D_q + D_{q'-q}(sigma - D_1) = D_r forces sigma = D_{1 + (r - q)/(q' - q)}
(checked as an identity in a field, with s standing for sigma)."""
from fractions import Fraction as F

QUOTED = {"bound": F(3, 2), "square": F(9, 4)}
b = QUOTED["bound"]
assert b > 0 and b * b == QUOTED["square"] and b * b > 2 and b < 2

import random
random.seed(19)
for _ in range(3000):
    q = F(random.randint(-300, 300), random.randint(1, 30))
    qp = q + F(random.randint(1, 300), random.randint(1, 30))
    s = F(random.randint(-300, 300), random.randint(1, 30))
    r = q + (qp - q) * (s - 1)                         # gamma = r
    assert s == 1 + (r - q) / (qp - q)                 # the solve for sigma
# and 0 < s - 1 < 1 with qp > q gives q < gamma < qp
for (qq, qqp, ss) in [(0, 1, F(7, 5)), (F(-3, 2), F(2, 7), F(141, 100)), (5, 6, F(3, 2) - F(1, 1000))]:
    g = qq + (qqp - qq) * (ss - 1)
    assert qq < g < qqp
print("ok")
