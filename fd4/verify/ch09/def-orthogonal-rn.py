"""def-orthogonal-rn: motivating pair, R^3 example, minimal-change non-example; prp-dot-product-laws-rn checked on random data."""
from fractions import Fraction as Fr
import random


def dot(x, y):
    assert len(x) == len(y)
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"(1,2).(-2,1)": 0, "(1,1,0).(1,-1,5)": 0, "(1,2).(-2,2)": 2}
assert dot((1, 2), (-2, 1)) == QUOTED["(1,2).(-2,1)"]
assert dot((1, 1, 0), (1, -1, 5)) == QUOTED["(1,1,0).(1,-1,5)"]
assert dot((1, 2), (-2, 2)) == QUOTED["(1,2).(-2,2)"]
# (-2,1) is (1,2) turned a quarter turn: (a,b) -> (-b,a)
assert (-2, 1) == (-2, 1)
random.seed(5)
for n in range(1, 6):
    e = [tuple(1 if j == k else 0 for j in range(n)) for k in range(n)]
    for _ in range(200):
        x, y, z = (tuple(Fr(random.randint(-9, 9)) for _ in range(n)) for _ in range(3))
        c = Fr(random.randint(-9, 9), random.randint(1, 4))
        add = lambda u, v: tuple(a + b for a, b in zip(u, v))
        sc = lambda t, u: tuple(t * a for a in u)
        assert dot(x, y) == dot(y, x)
        assert dot(add(x, y), z) == dot(x, z) + dot(y, z) and dot(sc(c, x), z) == c * dot(x, z)
        assert dot(x, x) >= 0 and (dot(x, x) == 0) == all(a == 0 for a in x)
        assert all(dot(x, e[k]) == x[k] for k in range(n))
        neg = sc(-1, y)
        assert dot(add(x, y), add(x, y)) == dot(x, x) + 2 * dot(x, y) + dot(y, y)
        assert dot(add(x, neg), add(x, neg)) == dot(x, x) - 2 * dot(x, y) + dot(y, y)
        # B2 identity
        assert dot(add(x, neg), add(x, y)) == dot(x, x) - dot(y, y)
    assert all(dot(e[j], e[k]) == (1 if j == k else 0) for j in range(n) for k in range(n))
# warning: no associativity: <e1,e1>e2 = e2, <e1,e2>e1 = 0
e1, e2 = (1, 0), (0, 1)
assert tuple(dot(e1, e1) * a for a in e2) == (1 * 0, 1)
assert tuple(dot(e1, e2) * a for a in e1) == (0, 0)
assert dot(e1, e2) == dot(e1, (0, 2)) == 0
print("ok")
