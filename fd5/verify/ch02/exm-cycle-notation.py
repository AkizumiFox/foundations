"""exm-cycle-notation: (1 3)(1 2) = (1 2 3), (1 2)(1 3) = (1 3 2); S_n non-abelian n >= 3, abelian n <= 2;
sigma = 3 5 1 2 4 = (1 3)(2 5 4) = (2 5 4)(1 3); warnings: (1 3 2)^2 = (1 2 3), sigma^2 tau^2 = id;
check: (1 2 3)(1 2) = (1 3)."""
QUOTED = {"13*12": (1, 2, 3), "12*13": (1, 3, 2), "sigma": [(1, 3), (2, 5, 4)], "sq": (1, 2, 3), "check": (1, 3)}

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
assert mul(cyc(3, 1, 3), cyc(3, 1, 2)) == cyc(3, 1, 2, 3)
assert mul(cyc(3, 1, 2), cyc(3, 1, 3)) == cyc(3, 1, 3, 2)
for n in range(3, 7):
    assert mul(cyc(n, 1, 3), cyc(n, 1, 2)) != mul(cyc(n, 1, 2), cyc(n, 1, 3))
for n in range(0, 3):
    G = list(permutations(range(1, n + 1)))
    assert all(mul(a, b) == mul(b, a) for a in G for b in G) if n else True
s = (3, 5, 1, 2, 4)
assert mul(cyc(5, 1, 3), cyc(5, 2, 5, 4)) == s == mul(cyc(5, 2, 5, 4), cyc(5, 1, 3))
assert cycles(s) == [(1, 3), (2, 5, 4)]
st = mul(cyc(3, 1, 2), cyc(3, 1, 3))
assert power(st, 2) == cyc(3, 1, 2, 3)
assert mul(power(cyc(3, 1, 2), 2), power(cyc(3, 1, 3), 2)) == ident(3)
assert mul(cyc(3, 1, 2, 3), cyc(3, 1, 2)) == cyc(3, 1, 3)
assert mul(cyc(3, 1, 3), cyc(3, 1, 2)) == cyc(3, *QUOTED["13*12"])
assert mul(cyc(3, 1, 2), cyc(3, 1, 3)) == cyc(3, *QUOTED["12*13"])
assert cycles((3, 5, 1, 2, 4)) == QUOTED["sigma"]
assert power(cyc(3, 1, 3, 2), 2) == cyc(3, *QUOTED["sq"])
assert mul(cyc(3, 1, 2, 3), cyc(3, 1, 2)) == cyc(3, *QUOTED["check"])
print("ok")
