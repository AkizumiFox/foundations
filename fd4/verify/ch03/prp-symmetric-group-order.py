"""prp-symmetric-group-order: card S_n = n! for n <= 6 (enumeration, counting bijections among all maps),
the classes A_k all have n! elements; 3! = 6, 4! = 24, 10! = 3628800; the six listed elements of S_3."""
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


from itertools import permutations, product
from math import factorial
QUOTED = {3: 6, 4: 24, 10: 3628800}
for n in range(0, 6):
    maps = list(product(range(1, n + 1), repeat=n))
    bij = [m for m in maps if len(set(m)) == n]
    assert len(bij) == factorial(n)
    if n >= 1:
        for k in range(1, n + 1):
            assert len([s for s in bij if s[n - 1] == k]) == factorial(n - 1)
assert len(list(permutations(range(1, 7)))) == factorial(6)
for n, v in QUOTED.items():
    assert factorial(n) == v
S3 = {ident(3), cyc(3, 1, 2), cyc(3, 1, 3), cyc(3, 2, 3), cyc(3, 1, 2, 3), cyc(3, 1, 3, 2)}
assert S3 == set(permutations((1, 2, 3)))
print("ok")
