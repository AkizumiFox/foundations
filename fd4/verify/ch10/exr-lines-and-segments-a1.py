"""exr-lines-and-segments-a1: (a) direction (2,1,-2), (5,1,-2) at t = 2; (b) midpoint (2,-1/2,1); (c) parameters 0,1,3 on (1,2)+R(2,3), (3,5) at t = 1/3; (d) distances 2, 1, 1, w = -u/2, t = 2."""
from fractions import Fraction as Fr
# --- exact vector helpers (tuples of Fractions) ---


def v(*xs):
    return tuple(Fr(x) for x in xs)


def add(x, y):
    assert len(x) == len(y)
    return tuple(a + b for a, b in zip(x, y))


def smul(c, x):
    return tuple(Fr(c) * a for a in x)


def sub(x, y):
    return add(x, smul(-1, y))


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


def multiple_of(b, a):
    """Is b = c a for some real c? (a != 0)"""
    k = next(i for i, t in enumerate(a) if t != 0)
    c = b[k] / a[k]
    return smul(c, a) == b# ---

QUOTED = {"dir": (2, 1, -2), "t": 2, "point": (5, 1, -2), "mid": (2, Fr(-1, 2), 1),
          "params": (0, 1, 3), "t_c": Fr(1, 3), "dists": (2, 1, 1), "mult": Fr(-1, 2), "t_d": 2}
# (a), (b)
P, Q = v(1, -1, 2), v(3, 0, 0)
assert sub(Q, P) == QUOTED["dir"]
assert add(P, smul(QUOTED["t"], sub(Q, P))) == QUOTED["point"]
assert smul(Fr(1, 2), add(P, Q)) == QUOTED["mid"]
# (c)
p, d = v(1, 2), v(2, 3)
for pt, par in zip([v(1, 2), v(3, 5), v(7, 11)], QUOTED["params"]):
    assert add(p, smul(par, d)) == pt
assert add(v(1, 2), smul(QUOTED["t_c"], sub(v(7, 11), v(1, 2)))) == v(3, 5)
# (d)
P, Q, X = v(0, 0), v(1, 0), v(2, 0)
sq = [dot(sub(P, X), sub(P, X)), dot(sub(X, Q), sub(X, Q)), dot(sub(P, Q), sub(P, Q))]
assert sq == [Fr(c) ** 2 for c in QUOTED["dists"]]
U, W = sub(X, P), sub(Q, X)
assert W == smul(QUOTED["mult"], U) and QUOTED["mult"] < 0
c = QUOTED["mult"]
assert 1 + c > 0 and 1 / (1 + c) == QUOTED["t_d"] > 1
assert sub(Q, P) == smul(Fr(1, 2), U) and X == add(P, smul(QUOTED["t_d"], sub(Q, P)))
print("ok")
