"""exr-permutations-and-cycles-a1: (a) (1 2 3 4)(2 4) = (1 2)(3 4), (2 4)(1 2 3 4) = (1 4)(2 3);
(b) (1 5 2 7)^{-1} = (1 7 2 5); (c) sigma = 2 5 4 3 1: orbit 1,2,5, r = 3, rho = (3 4), sigma = (1 2 5)(3 4);
(d) ((1 2)(2 3))^2 = (1 3 2), (1 2)^2 (2 3)^2 = id."""
QUOTED = {"a1": [(1, 2), (3, 4)], "a2": [(1, 4), (2, 3)], "b": (1, 7, 2, 5), "c": [(1, 2, 5), (3, 4)], "r": 3, "d": (1, 3, 2)}

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


assert mul(cyc(4, 1, 2, 3, 4), cyc(4, 2, 4)) == mul(cyc(4, 1, 2), cyc(4, 3, 4))
assert mul(cyc(4, 2, 4), cyc(4, 1, 2, 3, 4)) == mul(cyc(4, 1, 4), cyc(4, 2, 3))
assert inv(cyc(7, 1, 5, 2, 7)) == cyc(7, 1, 7, 2, 5) == cyc(7, 7, 2, 5, 1)
s = (2, 5, 4, 3, 1)
assert [power(s, c)[0] for c in range(4)] == [1, 2, 5, 1]
g = cyc(5, 1, 2, 5)
assert inv(g) == cyc(5, 1, 5, 2)
assert mul(inv(g), s) == cyc(5, 3, 4)
assert mul(cyc(5, 1, 2, 5), cyc(5, 3, 4)) == s
p = mul(cyc(3, 1, 2), cyc(3, 2, 3))
assert p == cyc(3, 1, 2, 3) and power(p, 2) == cyc(3, 1, 3, 2)
assert mul(power(cyc(3, 1, 2), 2), power(cyc(3, 2, 3), 2)) == ident(3)
assert cycles(mul(cyc(4, 1, 2, 3, 4), cyc(4, 2, 4))) == QUOTED["a1"]
assert cycles(mul(cyc(4, 2, 4), cyc(4, 1, 2, 3, 4))) == QUOTED["a2"]
assert cycles(inv(cyc(7, 1, 5, 2, 7))) == [QUOTED["b"]]
assert cycles((2, 5, 4, 3, 1)) == QUOTED["c"]
assert min(c for c in range(1, 6) if power((2, 5, 4, 3, 1), c)[0] == 1) == QUOTED["r"]
assert cycles(power(mul(cyc(3, 1, 2), cyc(3, 2, 3)), 2)) == [QUOTED["d"]]
print("ok")
