"""exr-permutations-and-cycles-b2: number of k-cycles in S_n is n!/((n-k)! k) for 2 <= k <= n <= 6;
lists of k distinct points number n!/(n-k)!; n = 4: 6 transpositions, 8 3-cycles, 6 4-cycles."""
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
from math import factorial
QUOTED = {2: 6, 3: 8, 4: 6}
for n in range(2, 7):
    G = list(permutations(range(1, n + 1)))
    for k in range(2, n + 1):
        lists = list(permutations(range(1, n + 1), k))
        assert len(lists) == factorial(n) // factorial(n - k)
        kc = [p for p in G if len(cycles(p)) == 1 and len(cycles(p)[0]) == k]
        assert len(kc) == factorial(n) // (factorial(n - k) * k)
        assert len({cyc(n, *t) for t in lists}) == len(kc)
        if n == 4:
            assert len(kc) == QUOTED[k]
print("ok")
