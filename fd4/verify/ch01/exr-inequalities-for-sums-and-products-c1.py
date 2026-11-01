"""exr-...-c1 (03): (2,1): A1 = 2 > A2 = 3/2; (1,2): a2 = 2 > A2 = 3/2; A_{n+1} lies between A_n and a_{n+1}."""
from fractions import Fraction as Fr
import random
assert Fr(2) > Fr(3, 2) == Fr(2 + 1, 2)
assert Fr(2) > Fr(1 + 2, 2)
random.seed(3)
for _ in range(2000):
    n = random.randint(1, 6)
    xs = [Fr(random.randint(1, 9)) for _ in range(n + 1)]
    An, An1, new = sum(xs[:n]) / n, sum(xs) / (n + 1), xs[-1]
    assert min(An, new) <= An1 <= max(An, new)
    if An <= An1 and new <= An1:
        assert An == new == An1
print("ok")
