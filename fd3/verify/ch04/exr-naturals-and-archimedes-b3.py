"""exr-naturals-and-archimedes-b3: 2^k >= k + 1; the construction for a = 1/3, b = 1/2."""
from fractions import Fraction as F
import math

QUOTED = {"gap": F(1, 6), "k": 6, "two_k": 64, "m": 21, "q": F(11, 32), "smaller": F(3, 8)}
assert all(2 ** k >= k + 1 for k in range(200))
a, b = F(1, 3), F(1, 2)
assert b - a == QUOTED["gap"]
k = min(k for k in range(100) if F(1, k + 1) < b - a)
assert k == QUOTED["k"] and 2 ** k == QUOTED["two_k"]
m = math.floor(2 ** k * a)
assert m == QUOTED["m"] and 21 * 3 == 63 <= 64 < 66 == 22 * 3
q = F(m + 1, 2 ** k)
assert q == QUOTED["q"] and a < q < b and 32 < 33 and 22 < 32
assert q <= a + F(1, 2 ** k) < b
assert a < QUOTED["smaller"] < b
print("ok")
