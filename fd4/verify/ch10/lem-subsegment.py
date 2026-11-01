"""lem-subsegment: (1-t)x + ty = p + ((1-t)s + tu)(q-p) on random rationals; Quick check: (2,0,1) not on [(1,-1,2),(3,0,0)]."""
import random
from fractions import Fraction as Fr

QUOTED = {"diff": (1, 1, -1), "dir": (2, 1, -2), "t_first": Fr(1, 2), "t_second": 1}


def comb(a, x, b, y):
    return tuple(a * xi + b * yi for xi, yi in zip(x, y))


random.seed(2)
R = lambda: Fr(random.randint(-20, 20), random.randint(1, 9))
for _ in range(300):
    p = tuple(R() for _ in range(3)); q = tuple(R() for _ in range(3))
    s, u, t = (Fr(random.randint(0, 9), 9) for _ in range(3))
    d = comb(1, q, -1, p)
    x = comb(1, p, s, d); y = comb(1, p, u, d)
    lam = (1 - t) * s + t * u
    assert comb(1 - t, x, t, y) == comb(1, p, lam, d) and 0 <= lam <= 1
P, Q, X = (1, -1, 2), (3, 0, 0), (2, 0, 1)
assert comb(1, Q, -1, P) == QUOTED["dir"] and comb(1, X, -1, P) == QUOTED["diff"]
assert Fr(1, 2) == QUOTED["t_first"] and Fr(1, 1) == QUOTED["t_second"]
print("ok")
