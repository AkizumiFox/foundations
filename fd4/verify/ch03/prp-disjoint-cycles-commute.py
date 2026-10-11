"""prp-disjoint-cycles-commute: exhaustively in S_5, permutations with disjoint supports commute, and
every permutation maps its support onto itself."""
QUOTED = {"n": 5}
GROUP_SIZE = 120  # 5!, checked here only; the page does not print it

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


from itertools import permutations
G = list(permutations(range(1, 6)))
for s in G:
    S = supp(s)
    assert {s[i - 1] for i in S} == S
for s in G:
    for t in G:
        if not (supp(s) & supp(t)):
            assert mul(s, t) == mul(t, s)
assert len(G) == GROUP_SIZE
print("ok")
