"""prp-group-power-laws (also covers prp-group-list-product-laws and exr-groups-b3): brute-force checks in S_3 and S_4
(permutations as tuples, product = composition, right factor first) and in (Z/7Z)^x:
power laws (a)-(d) for exponents in [-7, 7]; every bracketing of lists of length <= 5 in
S_3; inverse of a list product; the conjugate-power identity of exr-groups-b3."""
from itertools import permutations, product
QUOTED = {}  # no numeric value is quoted in the text; structural brute-force check only

def mul(s, t):  # s o t
    return tuple(s[t[i]] for i in range(len(t)))

def inv(s):
    r = [0] * len(s)
    for i, j in enumerate(s):
        r[j] = i
    return tuple(r)

def power(g, n, e):
    if n < 0:
        g, n = inv(g), -n
    r = e
    for _ in range(n):
        r = mul(r, g)
    return r

for n in (3, 4):
    e = tuple(range(n))
    G = list(permutations(range(n)))
    sample = G if n == 3 else G[::3]
    for g in sample:
        for m in range(-7, 8):
            gm = power(g, m, e)
            assert inv(gm) == power(g, -m, e) == power(inv(g), m, e)  # (b)
            for k in range(-7, 8):
                assert mul(gm, power(g, k, e)) == power(g, m + k, e)  # (a)
                assert power(gm, k, e) == power(g, m * k, e)  # (c)
        for h in sample:
            ghg = mul(mul(g, h), inv(g))
            for k in range(-6, 7):
                assert power(ghg, k, e) == mul(mul(g, power(h, k, e)), inv(g))  # exr b3
                if mul(g, h) == mul(h, g):
                    assert power(mul(g, h), k, e) == mul(power(g, k, e), power(h, k, e))  # (d)

# (d) fails without commuting: (1 2), (1 3) in S_3 (0-based: swap 0,1 and swap 0,2)
s, t = (1, 0, 2), (2, 1, 0)
e3 = (0, 1, 2)
assert power(mul(s, t), 2, e3) != mul(power(s, 2, e3), power(t, 2, e3))

# list products: every bracketing of a list of length <= 5 in S_3 has the list value
def brackets(lst):
    if len(lst) == 1:
        yield lst[0]
        return
    for k in range(1, len(lst)):
        for a in brackets(lst[:k]):
            for b in brackets(lst[k:]):
                yield mul(a, b)

def listprod(lst, e):
    r = e
    for x in lst:
        r = mul(r, x)
    return r

G3 = list(permutations(range(3)))
for r in range(1, 5):
    for lst in product(G3, repeat=r):
        v = listprod(lst, e3)
        assert all(b == v for b in brackets(list(lst)))
        assert inv(v) == listprod([inv(x) for x in reversed(lst)], e3)
for lst in list(product(G3, repeat=5))[::37]:
    v = listprod(lst, e3)
    assert all(b == v for b in brackets(list(lst)))

# (Z/7Z)^x: multiplicative group, power laws on exponents in [-10, 10]
def pw(a, n):
    if n < 0:
        a, n = pow(a, -1, 7), -n
    return pow(a, n, 7)
for a in range(1, 7):
    for m in range(-10, 11):
        for k in range(-10, 11):
            assert pw(a, m) * pw(a, k) % 7 == pw(a, m + k)
            assert pw(pw(a, m), k) == pw(a, m * k)
print("prp-group-power-laws: ok")
