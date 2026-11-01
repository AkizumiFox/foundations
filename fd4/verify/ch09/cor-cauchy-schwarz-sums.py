"""cor-cauchy-schwarz-sums: the remark's instance (1,2,3), (4,5,6): 32^2 = 1024 <= 14*77 = 1078; Lagrange n = 2."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"C": 32, "C2": 1024, "A": 14, "B": 77, "AB": 1078}
x, y = (1, 2, 3), (4, 5, 6)
assert dot(x, y) == QUOTED["C"] and QUOTED["C"] ** 2 == QUOTED["C2"]
assert n2(x) == QUOTED["A"] and n2(y) == QUOTED["B"] and QUOTED["A"] * QUOTED["B"] == QUOTED["AB"]
assert QUOTED["C2"] < QUOTED["AB"] and not parallel(x, y)
random.seed(1)
for _ in range(2000):
    a, b, c, d = (random.randint(-20, 20) for _ in range(4))
    assert (a*c + b*d)**2 + (a*d - b*c)**2 == (a*a + b*b) * (c*c + d*d)
# instance before the corollary: 4 + 10 + 18 = 32, 1 + 4 + 9 = 14, 16 + 25 + 36 = 77
assert 4 + 10 + 18 == 32 == dot((1, 2, 3), (4, 5, 6)) and 1 + 4 + 9 == 14 and 16 + 25 + 36 == 77
print("ok")
