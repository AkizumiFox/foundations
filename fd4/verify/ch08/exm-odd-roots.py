"""exm-odd-roots: (-x)^(2k+1) = ((-x)^2)^k (-x) = -x^(2k+1); x -> x^n strictly increasing on R
for odd n (sampled, exact), not injective for n = 2 ((-1)^2 = 1^2)."""
from fractions import Fraction as F
import random

random.seed(3)
for k in range(0, 6):
    n = 2 * k + 1
    for _ in range(300):
        x = F(random.randint(-300, 300), random.randint(1, 30))
        assert (-x) ** n == ((-x) ** 2) ** k * (-x) == -(x ** n)
        y = x + F(random.randint(1, 300), random.randint(1, 30))
        assert x ** n < y ** n
assert (-1) ** 2 == 1 ** 2
print("ok")
