"""exr-transpositions-b1: (1 2 3 4 5) = (1 5)(1 4)(1 3)(1 2) = (1 2)(2 3)(3 4)(4 5);
(1 5)(2 4) = ten adjacent transpositions; also (1 5) = (1 2)(2 5)(1 2) etc."""
from itertools import permutations


def cyc(n, *c):
    """the cycle (c_1 ... c_k) in S_n, as a tuple p with p[i-1] = image of i."""
    p = list(range(1, n + 1))
    for j, x in enumerate(c):
        p[x - 1] = c[(j + 1) % len(c)]
    return tuple(p)


def mul(*ps):
    """product p_1 p_2 ... p_r, read right to left (the right factor acts first)."""
    n = len(ps[0])
    r = tuple(range(1, n + 1))
    for p in ps:
        r = tuple(r[p[i] - 1] for i in range(n))
    return r


def inv(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x - 1] = i + 1
    return tuple(q)


def ident(n):
    return tuple(range(1, n + 1))
QUOTED = {"c5": [(1, 5), (1, 4), (1, 3), (1, 2)], "c5adj": [(1, 2), (2, 3), (3, 4), (4, 5)],
          "v": [(1, 2), (2, 3), (3, 4), (4, 5), (3, 4), (2, 3), (1, 2), (2, 3), (3, 4), (2, 3)]}
c = cyc(5, 1, 2, 3, 4, 5)
assert mul(*[cyc(5, *t) for t in QUOTED["c5"]]) == c
assert mul(*[cyc(5, *t) for t in QUOTED["c5adj"]]) == c
v = mul(cyc(5, 1, 5), cyc(5, 2, 4))
assert len(QUOTED["v"]) == 10 and all(b == a + 1 for a, b in QUOTED["v"])
assert mul(*[cyc(5, *t) for t in QUOTED["v"]]) == v
assert mul(cyc(5, 1, 2), cyc(5, 2, 5), cyc(5, 1, 2)) == cyc(5, 1, 5)
assert mul(cyc(5, 2, 3), cyc(5, 3, 5), cyc(5, 2, 3)) == cyc(5, 2, 5)
assert mul(cyc(5, 3, 4), cyc(5, 4, 5), cyc(5, 3, 4)) == cyc(5, 3, 5)
assert mul(cyc(5, 2, 3), cyc(5, 3, 4), cyc(5, 2, 3)) == cyc(5, 2, 4)
print("ok")
