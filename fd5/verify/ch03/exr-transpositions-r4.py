"""exr-transpositions-r4: in small groups of even size there is g != e with g^2 = e, and the number of
g with g^2 = e is even: Z/nZ for even n <= 20, S_3, S_4, (Z/8Z)^x, Z/2Z x Z/4Z; (Z/6Z,+): 2*[1] = [2] != [0],
2*[3] = [0]."""
QUOTED = {"modulus": 6, "2 * [1]": 2, "the element that works": 3}
from itertools import permutations


def cyc(n, *c):
    """the cycle (c_1 ... c_k) in S_n, as a tuple p with p[i-1] = image of i."""
    p = list(range(1, n + 1))
    for j, x in enumerate(c):
        p[x - 1] = c[(j + 1) % len(c)]
    return tuple(p)


def mul(*ps):
    """product p_1 p_2 ... p_r, read right to left (the right factor acts first)."""
    n = len(ps[0])
    r = tuple(range(1, n + 1))
    for p in ps:
        r = tuple(r[p[i] - 1] for i in range(n))
    return r


def inv(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x - 1] = i + 1
    return tuple(q)


def ident(n):
    return tuple(range(1, n + 1))
def count_T(elems, op, e):
    return sum(1 for g in elems if op(g, g) == e)
for n in range(2, 21, 2):
    t = count_T(range(n), lambda a, b: (a + b) % n, 0)
    assert t % 2 == 0 and t >= 2
for n in (3, 4):
    G = list(permutations(range(1, n + 1)))
    t = count_T(G, mul, ident(n))
    assert len(G) % 2 == 0 and t % 2 == 0 and t >= 2
U8 = [1, 3, 5, 7]
assert count_T(U8, lambda a, b: a * b % 8, 1) == 4
P = [(a, b) for a in range(2) for b in range(4)]
assert count_T(P, lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 4), (0, 0)) % 2 == 0
assert 2 * 1 % 6 == 2 and 2 * 3 % 6 == 0
m = QUOTED["modulus"]
assert 2 * 1 % m == QUOTED["2 * [1]"] != 0
assert [g for g in range(1, m) if 2 * g % m == 0] == [QUOTED["the element that works"]]
print("ok")
