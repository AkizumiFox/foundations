"""exr-transpositions-c2: (1 2)(1 3) = (1 3 2) != (1 2 3); in general the left-to-right product
(i_1 i_2)(i_1 i_3)...(i_1 i_k) is the inverse cycle, for all lists of distinct points, k <= n <= 6."""
QUOTED = {"(1 2)(1 3)": (1, 3, 2), "is not": (1, 2, 3), "k": 3}
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
assert mul(cyc(3, 1, 2), cyc(3, 1, 3)) == cyc(3, 1, 3, 2) != cyc(3, 1, 2, 3)
for n in range(2, 7):
    for k in range(2, n + 1):
        for c in permutations(range(1, n + 1), k):
            wrong = mul(*[cyc(n, c[0], c[j]) for j in range(1, k)])
            g = cyc(n, *c)
            assert wrong == inv(g)
            assert (wrong == g) == (k == 2)
assert mul(cyc(3, 1, 2), cyc(3, 1, 3)) == cyc(3, *QUOTED["(1 2)(1 3)"])
assert cyc(3, *QUOTED["(1 2)(1 3)"]) != cyc(3, *QUOTED["is not"])
assert len(QUOTED["is not"]) == QUOTED["k"]
print("ok")
