"""exr-ordering-the-reals-b3: a_n = 1 - 1/(n+2) satisfies 0 < a_n < 1; first term 1/2."""
from fractions import Fraction as F
QUOTED = {"a0": F(1, 2)}
a = lambda n: 1 - F(1, n + 2)
assert a(0) == QUOTED["a0"]
assert all(0 < a(n) < 1 for n in range(5000))
print("ok")
