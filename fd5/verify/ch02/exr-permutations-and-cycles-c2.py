"""exr-permutations-and-cycles-c2: k-cycle sigma^m = id iff k | m (k <= 6, m <= 30); disjoint k-, l-cycles:
(sigma tau)^m = id iff k | m and l | m; least m is lcm; ((1 2)(3 4 5))^m: least m = 6."""
QUOTED = {"least": 6}

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


from math import lcm
for k in range(2, 7):
    g = cyc(7, *range(1, k + 1))
    for m in range(1, 31):
        assert (power(g, m) == ident(7)) == (m % k == 0)
for k in range(2, 5):
    for l in range(2, 9 - k):
        s = cyc(9, *range(1, k + 1))
        t = cyc(9, *range(k + 1, k + l + 1))
        st = mul(s, t)
        for m in range(1, 40):
            assert (power(st, m) == ident(9)) == (m % k == 0 and m % l == 0)
        assert min(m for m in range(1, 100) if power(st, m) == ident(9)) == lcm(k, l)
x = mul(cyc(5, 1, 2), cyc(5, 3, 4, 5))
assert min(m for m in range(1, 50) if power(x, m) == ident(5)) == 6
assert min(m for m in range(1, 50) if power(mul(cyc(5, 1, 2), cyc(5, 3, 4, 5)), m) == ident(5)) == QUOTED["least"] == lcm(2, 3)
print("ok")
