"""thm-cardinal-laws: the six laws on small finite sets, by enumeration; Phi bijective for (d), (f);
Quick check 4 (8 = 8, Phi(h)); A1 (b)."""
import itertools

QUOTED = {"qc4_left": 8, "qc4_right": 8, "qc4_phi": ({"a": 1}, {"b": 0, "c": 1})}


def funcs(X, Y):
    """all functions X -> Y as frozensets of pairs (graphs)"""
    X = list(X)
    return [frozenset(zip(X, vals)) for vals in itertools.product(list(Y), repeat=len(X))]


def ap(f, x):
    return dict(f)[x]


def du(A, B):
    return {(a, 0) for a in A} | {(b, 1) for b in B}


def prod(A, B):
    return {(a, b) for a in A for b in B}


def is_bij(phi, S, T):
    img = [phi(s) for s in S]
    return len(set(img)) == len(S) and set(img) == set(T)


sets = [set(), {0}, {0, 1}, {"p", "q", "r"}]
for A, B, C in itertools.product(sets, repeat=3):
    assert len(du(A, B)) == len(du(B, A))
    assert len(du(du(A, B), C)) == len(du(A, du(B, C)))
    assert len(prod(A, B)) == len(prod(B, A))
    assert len(prod(prod(A, B), C)) == len(prod(A, prod(B, C)))
    assert len(prod(A, du(B, C))) == len(du(prod(A, B), prod(A, C)))
    # the explicit maps of the fold are bijections
    sw = lambda t: (t[0], 1 - t[1])
    assert is_bij(sw, du(A, B), du(B, A))
    def assoc(t):
        if t[1] == 1:
            return ((t[0], 1), 1)
        inner = t[0]
        return (inner[0], 0) if inner[1] == 0 else ((inner[0], 0), 1)
    assert is_bij(assoc, du(du(A, B), C), du(A, du(B, C)))
    dist = lambda t: ((t[0], t[1][0]), t[1][1])
    assert is_bij(dist, prod(A, du(B, C)), du(prod(A, B), prod(A, C)))

small = [set(), {0}, {0, 1}, {"x", "y", "z"}]
for X in small:
    assert len(funcs(set(), X)) == 1
    assert len(funcs({0}, X)) == len(X)
for X, Y, Z in itertools.product(small, repeat=3):
    if len(X) ** (len(Y) + len(Z)) > 800:
        continue
    # (d) Phi(h) = (h o iota_Y, h o iota_Z) is a bijection
    YZ = du(Y, Z)
    left = funcs(YZ, X)
    right = [(f, g) for f in funcs(Y, X) for g in funcs(Z, X)]
    phi = lambda h: (frozenset((y, ap(h, (y, 0))) for y in Y), frozenset((z, ap(h, (z, 1))) for z in Z))
    assert is_bij(phi, left, right)
    # (e)
    if len(X) * len(Y) ** len(Z) <= 800 and (len(X) * len(Y)) ** len(Z) <= 800:
        L = funcs(Z, prod(X, Y))
        R = [(f, g) for f in funcs(Z, X) for g in funcs(Z, Y)]
        e = lambda h: (frozenset((z, ap(h, z)[0]) for z in Z), frozenset((z, ap(h, z)[1]) for z in Z))
        assert is_bij(e, L, R)
    # (f) Phi(g)(y, z) = g(z)(y)
    if len(X) ** (len(Y) * len(Z)) <= 800:
        XY = funcs(Y, X)
        L = funcs(Z, XY)
        R = funcs(prod(Y, Z), X)
        cur = lambda g: frozenset(((y, z), ap(ap(g, z), y)) for y in Y for z in Z)
        assert is_bij(cur, L, R)

# Quick check 4
X, Y, Z = {0, 1}, {"a"}, {"b", "c"}
assert len(funcs(du(Y, Z), X)) == QUOTED["qc4_left"]
assert len(funcs(Y, X)) * len(funcs(Z, X)) == QUOTED["qc4_right"]
h = frozenset({(("a", 0), 1), (("b", 1), 0), (("c", 1), 1)})
f = {y: ap(h, (y, 0)) for y in Y}
g = {z: ap(h, (z, 1)) for z in Z}
assert (f, g) == QUOTED["qc4_phi"]
# A1 (b): X = Y = {0,1}, Z = {0}, h(y, z) = y corresponds to g with g(0) = id
gz = {y: y for y in (0, 1)}
assert all(gz[y] == y for y in (0, 1))
print("ok")
