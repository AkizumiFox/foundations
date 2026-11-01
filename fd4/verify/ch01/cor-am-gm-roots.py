"""cor-am-gm-roots (05): G^n = prod <= A^n, strict unless all equal (exact random check); G <= A follows by monotonicity."""
import random
from fractions import Fraction as F
from math import prod

QUOTED = {}
random.seed(1)
for _ in range(3000):
    n = random.randint(1, 7)
    a = [F(random.randint(0, 9), random.randint(1, 5)) for _ in range(n)]
    A = sum(a, F(0)) / n
    P = prod(a, start=F(1))
    assert P <= A ** n
    if len(set(a)) > 1:
        assert P < A ** n
print("ok")
