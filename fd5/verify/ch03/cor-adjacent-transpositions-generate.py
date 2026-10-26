"""cor-adjacent-transpositions-generate: (i j) = (i i+1)(i+1 j)(i i+1) for j - i >= 2 (n <= 7);
the mirror (i j) = (j-1 j)(i j-1)(j-1 j); every sigma in S_n, 2 <= n <= 5, is a product of adjacent
transpositions (closure of the adjacent ones under products reaches all n! elements);
(1 4) = (1 2)(2 3)(3 4)(2 3)(1 2) and (3 4)(2 3)(1 2)(2 3)(3 4)."""
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

from math import factorial
QUOTED = {"w1": [(1, 2), (2, 3), (3, 4), (2, 3), (1, 2)], "w2": [(3, 4), (2, 3), (1, 2), (2, 3), (3, 4)]}
for n in range(3, 8):
    for i in range(1, n + 1):
        for j in range(i + 2, n + 1):
            assert mul(cyc(n, i, i + 1), cyc(n, i + 1, j), cyc(n, i, i + 1)) == cyc(n, i, j)
            assert mul(cyc(n, j - 1, j), cyc(n, i, j - 1), cyc(n, j - 1, j)) == cyc(n, i, j)
for n in range(2, 6):
    adj = [cyc(n, i, i + 1) for i in range(1, n)]
    reach = set(adj)
    frontier = set(adj)
    while frontier:
        new = {mul(p, a) for p in frontier for a in adj} - reach
        reach |= new
        frontier = new
    assert len(reach) == factorial(n) and reach == set(permutations(range(1, n + 1)))
for w in QUOTED.values():
    assert mul(*[cyc(4, *t) for t in w]) == cyc(4, 1, 4)
print("ok")
