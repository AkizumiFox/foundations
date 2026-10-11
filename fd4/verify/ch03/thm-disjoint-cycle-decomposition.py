"""thm-disjoint-cycle-decomposition: worked run sigma = 4 6 3 1 2 5 in S_6 = (1 4)(2 6 5), rho after
peeling (1 4) has support {2, 5, 6}; check: 3 6 5 4 1 2 = (1 3 5)(2 6); the algorithm of the proof
(peel the orbit of the least moved point) yields disjoint cycles with product sigma, exhaustively in S_6."""
QUOTED = {"run": [(1, 4), (2, 6, 5)], "rho_supp": {2, 5, 6}, "check": [(1, 3, 5), (2, 6)]}

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
s = (4, 6, 3, 1, 2, 5)
assert supp(s) == {1, 2, 4, 5, 6}
g = cyc(6, 1, 4)
rho = mul(inv(g), s)
assert supp(rho) == {2, 5, 6} and rho == cyc(6, 2, 6, 5)
assert mul(cyc(6, 1, 4), cyc(6, 2, 6, 5)) == s
c = (3, 6, 5, 4, 1, 2)
assert mul(cyc(6, 1, 3, 5), cyc(6, 2, 6)) == c == mul(cyc(6, 2, 6), cyc(6, 1, 3, 5))
for n in range(0, 7):
    for p in permutations(range(1, n + 1)):
        cs = cycles(p)
        sets = [set(x) for x in cs]
        assert all(not (sets[a] & sets[b]) for a in range(len(cs)) for b in range(a))
        assert all(x <= supp(p) for x in sets)
        prod = ident(n)
        for x in cs:
            prod = mul(prod, cyc(n, *x))
        assert prod == p
# the non-injective map of the prompt never returns to 1
f = {1: 2, 2: 2}
x, orbit = 1, []
for _ in range(5):
    x = f[x]
    orbit.append(x)
assert 1 not in orbit
assert cycles((4, 6, 3, 1, 2, 5)) == QUOTED["run"]
assert supp(mul(inv(cyc(6, 1, 4)), (4, 6, 3, 1, 2, 5))) == QUOTED["rho_supp"]
assert cycles((3, 6, 5, 4, 1, 2)) == QUOTED["check"]
print("ok")
