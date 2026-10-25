"""exr-binary-operations-b1: x*y = x + y - xy on R. Associativity expansion, identity 0,
inverse x/(x - 1) for x != 1, 1 has none, 1 - x*y = (1 - x)(1 - y); indicator rule on {0,1}.
Polynomial identities of degree <= 3 in each variable are checked on a 5x5x5 grid of rationals
(enough to determine them), plus the explicit expanded form."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"identity": 0, "non_invertible": 1}


op = lambda x, y: x + y - x * y
expanded = lambda x, y, z: x + y + z - x*y - x*z - y*z + x*y*z
pts = [F(k, 3) for k in range(-2, 3)]
for x, y, z in product(pts, repeat=3):
    assert op(op(x, y), z) == expanded(x, y, z) == op(x, op(y, z))
for x, y in product(pts, repeat=2):
    assert op(x, y) == op(y, x)
    assert 1 - op(x, y) == (1 - x) * (1 - y)
for x in pts + [F(7, 2), F(-5)]:
    assert op(0, x) == x == op(x, 0)
    if x != 1:
        y = x / (x - 1)
        assert op(x, y) == 0 == op(y, x)
for y in pts:
    assert op(1, y) == 1
for u, v in product([0, 1], repeat=2):
    assert op(u, v) == (1 if (u or v) else 0)
assert op(QUOTED["identity"], 5) == 5
assert all(op(QUOTED["non_invertible"], y) != 0 for y in pts)
print("exr-binary-operations-b1: all quoted values check")
