"""Quick check after exm-method-am-gm (03): x(2-x) <= 1 on [0,2], equality only at x = 1."""
from fractions import Fraction as Fr
QUOTED = {"sum": 2, "mean": 1, "eq_at": 1}
for k in range(0, 201):
    x = Fr(k, 100)
    assert x + (2 - x) == QUOTED["sum"]
    v = x * (2 - x)
    assert v <= 1 and ((v == 1) == (x == QUOTED["eq_at"]))
print("ok")
