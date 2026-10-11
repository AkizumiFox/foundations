"""exr-ordered-field-of-rationals-b2 (b): a = 1/3, b = 1/2: b - a = 1/6, least n = 7, a + 1/7 = 10/21."""
from fractions import Fraction as F
QUOTED = {"diff": F(1, 6), "n": 7, "point": F(10, 21)}
a, b = F(1, 3), F(1, 2)
assert b - a == QUOTED["diff"]
n = next(k for k in range(1, 100) if a < a + F(1, k) < b)
assert n == QUOTED["n"] and a + F(1, n) == QUOTED["point"]
assert 21 < 30 and 20 < 21 and a + F(1, 6) == b
print("ok")
