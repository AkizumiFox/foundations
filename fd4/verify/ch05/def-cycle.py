"""def-cycle: (2 4 1) = (1 2 4) != (1 4 2) in S_4; two-line form of (1 4 2) is 4 1 3 2; inverse formula;
supp of a cycle is its entries; (1 2 3) = (2 3 1) = (3 1 2) != (1 3 2); (1 2 3) in S_4 is 2 3 1 4."""
def cyc(n, *c):
    """the cycle (c_1 ... c_k) in S_n as a tuple p with p[i-1] = image of i"""
    p = list(range(1, n + 1))
    for j, x in enumerate(c):
        p[x - 1] = c[(j + 1) % len(c)]
    return tuple(p)


def mul(*ps):
    """product read right to left: mul(s, t)(i) = s(t(i))"""
    n = len(ps[0])
    r = tuple(range(1, n + 1))
    for p in reversed(ps):
        r = tuple(p[r[i] - 1] for i in range(n))
    return r


def ident(n):
    return tuple(range(1, n + 1))


def inv(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x - 1] = i + 1
    return tuple(q)


def power(p, m):
    r = ident(len(p))
    for _ in range(m):
        r = mul(r, p)
    return r


def supp(p):
    return {i + 1 for i, x in enumerate(p) if x != i + 1}


def cycles(p):
    """disjoint cycle decomposition by following orbits from the smallest moved point"""
    seen, out = set(), []
    for i in range(1, len(p) + 1):
        if i in seen or p[i - 1] == i:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = p[j - 1]
        out.append(tuple(c))
    return out


QUOTED = {"two_line_142": (4, 1, 3, 2), "two_line_123": (2, 3, 1, 4)}
assert cyc(4, 2, 4, 1) == cyc(4, 1, 2, 4) != cyc(4, 1, 4, 2)
assert cyc(4, 1, 4, 2) == QUOTED["two_line_142"] == inv(cyc(4, 1, 2, 4))
assert cyc(4, 1, 2, 3) == cyc(4, 2, 3, 1) == cyc(4, 3, 1, 2) != cyc(4, 1, 3, 2)
assert cyc(4, 1, 2, 3) == QUOTED["two_line_123"]
from itertools import permutations
for k in range(2, 6):
    for c in permutations(range(1, 6), k):
        g = cyc(5, *c)
        assert inv(g) == cyc(5, *reversed(c)) and supp(g) == set(c)
        if k == 2:
            assert mul(g, g) == ident(5)
print("ok")
