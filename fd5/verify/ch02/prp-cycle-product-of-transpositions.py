"""prp-cycle-product-of-transpositions: (i_1 ... i_k) = (i_1 i_k)(i_1 i_{k-1}) ... (i_1 i_2),
checked for every list of k distinct points of {1..n}, 2 <= k <= n <= 7 (n = 7 restricted to k <= 7);
examples (1 2 3 4) = (1 4)(1 3)(1 2); (2 3 1) gives (1 2)(2 3) = (1 2 3);
quick check (2 5 3) = (2 3)(2 5); the facts (a b) = (b a), (a b)(a b) = id."""
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

QUOTED = {"ex4": [(1, 4), (1, 3), (1, 2)], "rot": [(1, 2), (2, 3)], "check": [(2, 3), (2, 5)]}
assert mul(cyc(3, 1, 3), cyc(3, 1, 2)) == cyc(3, 1, 2, 3)  # convention, exm-cycle-notation
for n in range(2, 8):
    for k in range(2, n + 1):
        for c in permutations(range(1, n + 1), k):
            word = [cyc(n, c[0], c[j]) for j in range(k - 1, 0, -1)]
            assert mul(*word) == cyc(n, *c)
            assert len(word) == k - 1
assert mul(*[cyc(4, *t) for t in QUOTED["ex4"]]) == cyc(4, 1, 2, 3, 4)
assert mul(*[cyc(3, *t) for t in QUOTED["rot"]]) == cyc(3, 1, 2, 3) == cyc(3, 2, 3, 1)
assert mul(*[cyc(5, *t) for t in QUOTED["check"]]) == cyc(5, 2, 5, 3)
for a in range(1, 6):
    for b in range(1, 6):
        if a != b:
            assert cyc(5, a, b) == cyc(5, b, a) and mul(cyc(5, a, b), cyc(5, a, b)) == ident(5)
print("ok")
