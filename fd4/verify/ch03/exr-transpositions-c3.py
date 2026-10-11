"""exr-transpositions-c3: sigma (i_1 ... i_k) sigma^{-1} = (sigma(i_1) ... sigma(i_k)) in S_5;
the conjugating pi with pi(1) = a, pi(2) = b: id, (2 b) for a = 1, b >= 3, (1 a)(2 b) for a >= 2."""
QUOTED = {"pi for (a, b) = (1, 2)": r"\pi = \id", "pi for a = 1, b >= 3": r"\pi = (2\ b)",
          "pi for a >= 2": r"\pi = (1\ a)(2\ b)"}
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
n = 5
for s in permutations(range(1, n + 1)):
    for k in range(2, n + 1):
        for c in permutations(range(1, n + 1), k):
            assert mul(s, cyc(n, *c), inv(s)) == cyc(n, *[s[x - 1] for x in c])
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if (a, b) == (1, 2):
            pi = ident(n)
        elif a == 1:
            pi = cyc(n, 2, b)
        else:
            assert b >= 3
            pi = mul(cyc(n, 1, a), cyc(n, 2, b))
        assert pi[0] == a and pi[1] == b
        assert mul(pi, cyc(n, 1, 2), inv(pi)) == cyc(n, a, b)
# QUOTED: build pi from the printed words and check pi(1) = a, pi(2) = b, pi (1 2) pi^{-1} = (a b)
import re


def word(text, a, b):
    """the permutation named by a printed word "\\pi = (x\\ y)(u\\ v)..." or "\\pi = \\id"."""
    p = ident(n)
    for x, y in re.findall(r"\((\w)\\ (\w)\)", text):
        x, y = [{"a": a, "b": b}.get(t) or int(t) for t in (x, y)]
        p = mul(p, cyc(n, x, y))
    return p


for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        key = ("pi for (a, b) = (1, 2)" if (a, b) == (1, 2) else
               "pi for a = 1, b >= 3" if a == 1 else "pi for a >= 2")
        pi = word(QUOTED[key], a, b)
        assert pi[0] == a and pi[1] == b and mul(pi, cyc(n, 1, 2), inv(pi)) == cyc(n, a, b)
print("ok")
