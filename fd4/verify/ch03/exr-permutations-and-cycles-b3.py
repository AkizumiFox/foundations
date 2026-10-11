"""exr-permutations-and-cycles-b3: rho = (1 2 3 4), rho^2 = (1 3)(2 4), rho^3 = (1 4 3 2), rho^4 = id;
[k] -> rho^k is a well-defined isomorphism Z/4Z -> <rho>."""
QUOTED = {"rho2": [(1, 3), (2, 4)], "rho3": [(1, 4, 3, 2)]}

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


r = cyc(4, 1, 2, 3, 4)
assert r == (2, 3, 4, 1)
assert power(r, 2) == mul(cyc(4, 1, 3), cyc(4, 2, 4))
assert power(r, 3) == cyc(4, 1, 4, 3, 2) and power(r, 4) == ident(4)
P = [power(r, k) for k in range(4)]
assert len(set(P)) == 4 and [p[0] for p in P] == [1, 2, 3, 4]
assert all(power(r, k) == P[k % 4] for k in range(40))
assert all(P[(a + b) % 4] == mul(P[a], P[b]) for a in range(4) for b in range(4))
assert cycles(power(cyc(4, 1, 2, 3, 4), 2)) == QUOTED["rho2"]
assert cycles(power(cyc(4, 1, 2, 3, 4), 3)) == QUOTED["rho3"]
print("ok")
