"""thm-transpositions-generate: every sigma in S_n (2 <= n <= 6) is a product of transpositions,
by running the proof's recursion (fix n, then induct); S_2 = {id, (1 2)}, id = (1 2)(1 2);
remark: (1 3)(2 5 4) = (1 3)(2 4)(2 5), and it is the sigma of exm-cycle-notation (1->3,2->5,3->1,4->2,5->4);
the words (1 2 3) = (1 3)(1 2) = (1 2)(2 3) = (1 3)(1 2)(1 2)(1 2), lengths 2, 2, 4;
(1 2)(1 3) = (1 3 2); non-example: the 3-cycles of S_3, H = {id, (1 2 3), (1 3 2)} closed, (1 2) not in H;
the try-it-first: (1 2 3 4) = (1 4)(1 3)(1 2)."""
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


def word(s):
    """the proof's word for s in S_n, n >= 2, as a list of transpositions (pairs)."""
    n = len(s)
    if n == 2:
        return [(1, 2)] if s == (2, 1) else [(1, 2), (1, 2)]
    k = s[n - 1]
    if k == n:  # Case 1: restrict
        return word(s[: n - 1])
    t = cyc(n, k, n)  # Case 2
    return [(k, n)] + word(mul(t, s)[: n - 1])

QUOTED = {"S2": {(1, 2), (2, 1)}, "remark": [(1, 3), (2, 4), (2, 5)], "lengths": [2, 2, 4]}
assert set(permutations((1, 2))) == QUOTED["S2"] and mul(cyc(2, 1, 2), cyc(2, 1, 2)) == ident(2)
for n in range(2, 7):
    for s in permutations(range(1, n + 1)):
        w = word(s)
        assert len(w) >= 1 and all(a != b for a, b in w)
        assert mul(*[cyc(n, a, b) for a, b in w]) == s
sig = (3, 5, 1, 2, 4)
assert mul(cyc(5, 1, 3), cyc(5, 2, 5, 4)) == sig
assert mul(*[cyc(5, *t) for t in QUOTED["remark"]]) == sig
c123 = cyc(3, 1, 2, 3)
words = [[(1, 3), (1, 2)], [(1, 2), (2, 3)], [(1, 3), (1, 2), (1, 2), (1, 2)]]
assert [len(w) for w in words] == QUOTED["lengths"]
assert all(mul(*[cyc(3, *t) for t in w]) == c123 for w in words)
assert mul(cyc(3, 1, 2), cyc(3, 1, 3)) == cyc(3, 1, 3, 2) != c123
three = {cyc(3, *c) for c in permutations((1, 2, 3))}
assert three == {cyc(3, 1, 2, 3), cyc(3, 1, 3, 2)}
H = {ident(3), cyc(3, 1, 2, 3), cyc(3, 1, 3, 2)}
assert mul(c123, c123) == cyc(3, 1, 3, 2) and mul(cyc(3, 1, 3, 2), cyc(3, 1, 3, 2)) == c123
assert mul(c123, cyc(3, 1, 3, 2)) == ident(3) == mul(cyc(3, 1, 3, 2), c123)
assert all(mul(x, y) in H for x in H for y in H) and cyc(3, 1, 2) not in H
assert mul(cyc(4, 1, 4), cyc(4, 1, 3), cyc(4, 1, 2)) == cyc(4, 1, 2, 3, 4)
print("ok")
