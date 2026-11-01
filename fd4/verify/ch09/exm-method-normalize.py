"""exm-method-normalize: ||u + v|| <= 2 for unit u, v (squared: ||u+v||^2 = 2 + 2<u,v> <= 4), while x = y = 2e_1 gives ||x + y|| = 4 > 2."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"norm_x_plus_y": 4}
x = y = (2, 0)
assert n2(add(x, y)) == QUOTED["norm_x_plus_y"] ** 2 and QUOTED["norm_x_plus_y"] > 2
for u, v in [((1, 0), (1, 0)), ((1, 0), (0, 1)), ((Fr(3, 5), Fr(4, 5)), (Fr(-4, 5), Fr(3, 5)))]:
    assert n2(u) == 1 == n2(v) and n2(add(u, v)) <= 4
print("ok")
