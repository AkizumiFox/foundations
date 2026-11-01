"""exr-transpositions-c1: base n = 2: S_2 = {id, (1 2)} and id = (1 2)(1 2); the induction
(fix n + 1, else multiply by tau = (k n+1)) writes every sigma in S_n, 2 <= n <= 6, as a product
of transpositions, with (tau sigma)(n + 1) = n + 1 at the Case-2 step."""
from itertools import permutations

QUOTED = {"base n": 2, "S_2 as image lists": ((1, 2), (2, 1)), "id = (1 2)(1 2)": (1, 2)}


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


def ident(n):
    return tuple(range(1, n + 1))


def word(s):
    """the solution's word for s in S_n, n >= 2, as a list of transpositions (pairs)."""
    n = len(s)
    if n == QUOTED["base n"]:
        t = QUOTED["id = (1 2)(1 2)"]
        return [t] if s == (2, 1) else [t, t]
    k = s[n - 1]
    if k == n:                                   # Case 1: restrict to {1, ..., n - 1}
        return word(s[: n - 1])
    tau = cyc(n, k, n)                           # Case 2
    ts = mul(tau, s)
    assert ts[n - 1] == n
    return [(k, n)] + word(ts[: n - 1])


n0 = QUOTED["base n"]
assert tuple(sorted(permutations(range(1, n0 + 1)))) == QUOTED["S_2 as image lists"]
assert mul(cyc(2, *QUOTED["id = (1 2)(1 2)"]), cyc(2, *QUOTED["id = (1 2)(1 2)"])) == ident(2)
for n in range(2, 7):
    for s in permutations(range(1, n + 1)):
        w = word(s)
        assert len(w) >= 1 and all(a != b for a, b in w)
        assert mul(*[cyc(n, *t) for t in w]) == s
print("ok")
