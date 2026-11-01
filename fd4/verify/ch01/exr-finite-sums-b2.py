"""exr-finite-sums-b2: (a) true; (b) n = 2, a = (1, 1): 4 vs 2; (c) true (reversal); (d) false: n = 1 both 1/3; n = 2: 11/24 vs 3/8 = 9/24; correct value (1/2)(3/2 - 1/(n+1) - 1/(n+2)), at n = 2 (1/2)(11/12) = 11/24."""
import random
from fractions import Fraction as Fr
QUOTED = {"b": (4, 2), "d_n1": Fr(1, 3), "d_left_n2": Fr(11, 24), "d_right_n2": Fr(3, 8), "d_inner_n2": Fr(11, 12)}
random.seed(8)
for _ in range(300):
    n = random.randint(1, 8)
    a = [random.randint(-9, 9) for _ in range(n + 1)]
    bb = [random.randint(-9, 9) for _ in range(n + 1)]
    assert sum(x + 1 for x in a[1:]) == sum(a[1:]) + n
    assert sum(a[n - k] * bb[k] for k in range(n + 1)) == sum(a[k] * bb[n - k] for k in range(n + 1))
assert ((1 + 1) ** 2, 1 + 1) == QUOTED["b"]
L = lambda n: sum(Fr(1, k * (k + 2)) for k in range(1, n + 1))
R = lambda n: Fr(1, 2) * (1 - Fr(1, n + 2))
C = lambda n: Fr(1, 2) * (Fr(3, 2) - Fr(1, n + 1) - Fr(1, n + 2))
assert L(1) == R(1) == QUOTED["d_n1"]
assert L(2) == Fr(1, 3) + Fr(1, 8) == QUOTED["d_left_n2"] and R(2) == QUOTED["d_right_n2"] == Fr(9, 24)
assert Fr(3, 2) - Fr(1, 3) - Fr(1, 4) == QUOTED["d_inner_n2"] and C(2) == QUOTED["d_left_n2"]
for n in range(1, 100):
    assert L(n) == C(n)
    if n >= 2:
        assert L(n) != R(n)
for k in range(1, 100):
    assert Fr(1, k * (k + 2)) == Fr(1, 2) * (Fr(1, k) - Fr(1, k + 2))
print("ok")
