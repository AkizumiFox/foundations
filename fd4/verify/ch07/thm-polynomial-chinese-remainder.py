"""thm-polynomial-chinese-remainder: the quick check (f = 3 + 2x from e_1 = 1 - x, e_2 = x);
parts (a)-(d) on random pairwise coprime moduli over F_5, and the bijection by counting over F_2."""
from fractions import Fraction as F

QUOTED = {"f": "3 + 2x", "e_1": "1 - x", "values": (3, 5)}

# --- small dense-polynomial helpers (coefficients low degree first; p=None: exact Fractions, else mod p) ---
from fractions import Fraction as F


def trim(a, p=None):
    a = [(c % p) if p else c for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p=None):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], p)


def scal(c, a, p=None):
    return trim([c * x for x in a], p)


def sub(a, b, p=None):
    return add(a, scal(-1, b), p)


def mul(a, b, p=None):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out, p)


def prod(lst, p=None):
    out = [1]
    for f in lst:
        out = mul(out, f, p)
    return out


def inv(c, p=None):
    return pow(c % p, p - 2, p) if p else F(1) / c


def pdivmod(a, b, p=None):
    a, b = trim(a, p), trim(b, p)
    assert b
    q = [0] * max(len(a) - len(b) + 1, 1)
    r = list(a)
    lb = inv(b[-1], p)
    while len(r) >= len(b) and r:
        k = len(r) - len(b)
        c = (r[-1] * lb) % p if p else r[-1] * lb
        q[k] = c
        r = sub(r, [0] * k + scal(c, b, p), p)
    return trim(q, p), r


def ev(a, x, p=None):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v % p if p else v


def deriv(a, p=None):
    return trim([i * a[i] for i in range(1, len(a))], p)


def monic(a, p=None):
    a = trim(a, p)
    return scal(inv(a[-1], p), a, p) if a else a


def pgcd(a, b, p=None):
    a, b = trim(a, p), trim(b, p)
    while b:
        a, b = b, pdivmod(a, b, p)[1]
    return monic(a, p)


X = [0, 1]


def lin(c, p=None):
    return trim([-c, 1], p)


def lagrange(nodes, i, p=None):
    out = [1]
    for j, cj in enumerate(nodes):
        if j != i:
            out = mul(out, scal(inv(nodes[i] - cj, p), lin(cj, p), p), p)
    return out
# --- end helpers ---

import random, itertools
e1, e2 = scal(-1, lin(1)), [0, 1]
assert e1 == [1, -1] and sub([0, 1], lin(1)) == [1]
f = add(scal(3, e1), scal(5, e2))
assert f == [3, 2] and (ev(f, 0), ev(f, 1)) == QUOTED["values"]
assert f == add(scal(3, lagrange([0, 1], 0)), scal(5, lagrange([0, 1], 1)))

def bez(a, b, p):
    # extended Euclid: returns (u, v) with u a + v b = gcd (monic)
    r0, r1, s0, s1, t0, t1 = a, b, [1], [], [], [1]
    while r1:
        q, r = pdivmod(r0, r1, p)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1, p), p)
        t0, t1 = t1, sub(t0, mul(q, t1, p), p)
    c = inv(r0[-1], p)
    return scal(c, s0, p), scal(c, t0, p)

p = 5
random.seed(4)
cands = [trim(list(c), p) for d in (1, 2) for c in itertools.product(range(p), repeat=d + 1) if c[-1] == 1]
for _ in range(60):
    ms = random.sample(cands, 3)
    if any(pgcd(a, b, p) != [1] for a, b in itertools.combinations(ms, 2)):
        continue
    m = prod(ms, p)
    rs = [trim([random.randrange(p) for _ in range(3)], p) for _ in ms]
    es = []
    for i, mi in enumerate(ms):
        Mi = prod([mj for j, mj in enumerate(ms) if j != i], p)
        a, b = bez(Mi, mi, p)
        assert add(mul(a, Mi, p), mul(b, mi, p), p) == [1]
        es.append(mul(a, Mi, p))
    for i, e in enumerate(es):
        for j, mj in enumerate(ms):
            assert pdivmod(sub(e, [1] if i == j else [], p), mj, p)[1] == []
    fsol = []
    for r, e in zip(rs, es):
        fsol = add(fsol, mul(r, e, p), p)
    for r, mi in zip(rs, ms):
        assert pdivmod(sub(fsol, r, p), mi, p)[1] == []
    red = pdivmod(fsol, m, p)[1]
    assert len(red) < len(m)
# (d) bijection by counting: F_2[x]/<x(x+1)(x^2+x+1)> against the product of the three quotients
p = 2
ms = [[0, 1], [1, 1], [1, 1, 1]]
m = prod(ms, p)
reps = [trim(list(c), p) for c in itertools.product(range(p), repeat=len(m) - 1)]
images = {tuple(tuple(pdivmod(r, mi, p)[1]) for mi in ms) for r in reps}
assert len(images) == len(reps) == 16
print("ok")
