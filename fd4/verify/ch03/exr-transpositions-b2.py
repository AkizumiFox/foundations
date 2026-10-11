"""exr-transpositions-b2: sigma (a b) sigma^{-1} = (sigma(a) sigma(b)) in S_n (n <= 5, all sigma);
rho = (1 2 ... n): rho^m(j) = j + m for j + m <= n; rho^{i-1}(1 2)rho^{-(i-1)} = (i i+1), n <= 6;
(1 2), rho, rho^{-1} generate S_n for n <= 5."""
QUOTED = {"for n = 2, rho = (1 2)": (1, 2),
          "conjugation formula": r"\rho^{i-1}(1\ 2)\rho^{-(i-1)} = (i\ \ i{+}1)"}
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
for n in range(2, 6):
    for s in permutations(range(1, n + 1)):
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                assert mul(s, cyc(n, a, b), inv(s)) == cyc(n, s[a - 1], s[b - 1])
for n in range(2, 7):
    rho = cyc(n, *range(1, n + 1))
    pw = ident(n)
    for m in range(n):
        for j in range(1, n + 1 - m):
            assert pw[j - 1] == j + m
        pw = mul(pw, rho)
    for i in range(1, n):
        p = ident(n)
        for _ in range(i - 1):
            p = mul(p, rho)
        assert mul(p, cyc(n, 1, 2), inv(p)) == cyc(n, i, i + 1)
for n in range(2, 6):
    rho = cyc(n, *range(1, n + 1))
    gens = [cyc(n, 1, 2), rho, inv(rho)]
    reach, frontier = set(gens), set(gens)
    while frontier:
        new = {mul(p, g) for p in frontier for g in gens} - reach
        reach |= new
        frontier = new
    assert len(reach) == factorial(n)
# QUOTED: n = 2, and the formula of (b) read off the printed string (i in place of the exponent)
assert cyc(2, *range(1, 3)) == cyc(2, *QUOTED["for n = 2, rho = (1 2)"])
assert QUOTED["conjugation formula"].replace(" ", "") == r"\rho^{i-1}(1\2)\rho^{-(i-1)}=(i\\i{+}1)"
print("ok")
