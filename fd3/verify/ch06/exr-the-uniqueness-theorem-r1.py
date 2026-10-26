"""exr-the-uniqueness-theorem-r1: q_n = (n + 1)/(n + 2) has q_n - 1 = -1/(n + 2), so
|q_n - 1| = 1/(n + 2), and q_n < 1 for every n (checked exactly for n < 500)."""
from fractions import Fraction as F

QUOTED = {"difference": lambda n: F(-1, n + 2)}
for n in range(500):
    q = F(n + 1, n + 2)
    assert q - 1 == QUOTED["difference"](n)
    assert abs(q - 1) == F(1, n + 2)
    assert q < 1
print("ok")
