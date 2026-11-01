"""exr-transpositions-a1 (b): sigma = (1 3 4 2) in S_4; tau = (2 4), tau sigma = (1 3 2);
tau' = (2 3), tau' sigma' = (1 2); word (2 4)(2 3)(1 2); second-route word (1 2)(1 4)(1 3);
third word (2 4)(1 2)(1 3)."""
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
QUOTED = {"run": [(2, 4), (2, 3), (1, 2)], "route2": [(1, 2), (1, 4), (1, 3)], "third": [(2, 4), (1, 2), (1, 3)]}
s = cyc(4, 1, 3, 4, 2)
assert s[3] == 2
ts = mul(cyc(4, 2, 4), s)
assert ts == cyc(4, 1, 3, 2) and ts[3] == 4
s3 = ts[:3]
assert s3 == cyc(3, 1, 3, 2) and s3[2] == 2
t3 = mul(cyc(3, 2, 3), s3)
assert t3 == cyc(3, 1, 2) and t3[2] == 3 and t3[:2] == (2, 1)
for w in QUOTED.values():
    assert mul(*[cyc(4, *t) for t in w]) == s
assert mul(cyc(3, 2, 3), cyc(3, 1, 2)) == cyc(3, 1, 3, 2)
print("ok")
