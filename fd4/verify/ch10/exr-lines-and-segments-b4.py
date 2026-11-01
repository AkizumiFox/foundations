"""exr-lines-and-segments-b4: (a) s = r = 1/2 ||p - q|| sum to ||p - q||; (b) ||p - x||^2 = ||x - q||^2 = 2 for p = (-1,0), q = (1,0), x = (0,1)."""
from fractions import Fraction as Fr

QUOTED = {"half": "1/2", "sq": 2}
for N in [Fr(1), Fr(5, 3), Fr(7)]:
    s = r = Fr(1, 2) * N
    assert s >= 0 and s + r == N
p, q, x = (-1, 0), (1, 0), (0, 1)
d = lambda a, b: sum((ai - bi) ** 2 for ai, bi in zip(a, b))
assert d(p, x) == d(x, q) == QUOTED["sq"] and x[1] == 1
print("ok")
