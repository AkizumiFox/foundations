"""exr-permutations-and-cycles-b1: the table of S_3 (rows x, columns y, entry xy), the x with x^2 = id,
and the center {id}; the four quoted non-commuting pairs."""
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


E = {"id": ident(3), "12": cyc(3, 1, 2), "13": cyc(3, 1, 3), "23": cyc(3, 2, 3),
     "123": cyc(3, 1, 2, 3), "132": cyc(3, 1, 3, 2)}
order = ["id", "12", "13", "23", "123", "132"]
QUOTED = {
    "id": ["id", "12", "13", "23", "123", "132"],
    "12": ["12", "id", "132", "123", "23", "13"],
    "13": ["13", "123", "id", "132", "12", "23"],
    "23": ["23", "132", "123", "id", "13", "12"],
    "123": ["123", "13", "23", "12", "132", "id"],
    "132": ["132", "23", "12", "13", "id", "123"],
}
for x in order:
    for j, y in enumerate(order):
        assert mul(E[x], E[y]) == E[QUOTED[x][j]], (x, y)
assert [x for x in order if mul(E[x], E[x]) == ident(3)] == ["id", "12", "13", "23"]
assert [x for x in order if all(mul(E[x], E[y]) == mul(E[y], E[x]) for y in order)] == ["id"]
assert mul(E["12"], E["13"]) == E["132"] and mul(E["13"], E["12"]) == E["123"]
assert mul(E["23"], E["12"]) == E["132"] and mul(E["12"], E["23"]) == E["123"]
assert mul(E["123"], E["12"]) == E["13"] and mul(E["12"], E["123"]) == E["23"]
assert mul(E["132"], E["12"]) == E["23"] and mul(E["12"], E["132"]) == E["13"]
print("ok")
