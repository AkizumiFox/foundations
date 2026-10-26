"""thm-polynomial-ring-laws (Section 4.2).
1. The ring laws of (Z/nZ)[x]: commutativity and 1 * p = p exhaustively on polynomials
   with coefficients in positions 0..2, n <= 6; distributivity on all triples of the first
   60 such polynomials (all of them for n <= 3), and on the random triples below; associativity exhaustively in positions 0..1
   for n <= 6 and in positions 0..2 for n <= 3, and on 20000 random triples (positions 0..2)
   for n = 4, 5, 6.
2. The Try-it-first identity: the coefficient of x^2 in (pq)r and p(qr) for linear p, q, r.
3. The Quick check: (x + 1)^2 has coefficients 1, 2, 1 over Q and 1, 0, 1 over F_2.
"""
import random
from itertools import product

QUOTED = {
    "check_Q": [1, 2, 1],
    "check_F2": [1, 0, 1],
}


def mul(p, q, n):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = (out[i + j] + a * b) % n
    return tuple(out)


def add(p, q, n):
    L = max(len(p), len(q))
    p, q = list(p) + [0] * (L - len(p)), list(q) + [0] * (L - len(q))
    return tuple((a + b) % n for a, b in zip(p, q))


def strip(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


for n in range(1, 7):
    polys2 = list(product(range(n), repeat=3))
    for p in polys2:
        assert strip(mul((1,), p, n)) == strip(p)                     # 1 * p = p
        for q in polys2:
            assert strip(mul(p, q, n)) == strip(mul(q, p, n))
    for p, q, r in product(polys2[: min(len(polys2), 60)], repeat=3):
        assert strip(mul(p, add(q, r, n), n)) == strip(add(mul(p, q, n), mul(p, r, n), n))
    polys1 = list(product(range(n), repeat=2))
    for p, q, r in product(polys1, repeat=3):
        assert strip(mul(mul(p, q, n), r, n)) == strip(mul(p, mul(q, r, n), n))
    if n <= 3:
        for p, q, r in product(polys2, repeat=3):
            assert strip(mul(mul(p, q, n), r, n)) == strip(mul(p, mul(q, r, n), n))
    else:
        rng = random.Random(n)
        for _ in range(20000):
            p, q, r = (tuple(rng.randrange(n) for _ in range(3)) for _ in range(3))
            assert strip(mul(mul(p, q, n), r, n)) == strip(mul(p, mul(q, r, n), n))
            assert strip(mul(p, add(q, r, n), n)) == strip(add(mul(p, q, n), mul(p, r, n), n))

# Try it first: coefficient of x^2
rng = random.Random(1)
for _ in range(2000):
    a0, a1, b0, b1, c0, c1 = (rng.randint(-50, 50) for _ in range(6))
    big = 10**12
    pq = mul((a0, a1), (b0, b1), big * 10)
    left = (a0 * b1 + a1 * b0) * c1 + (a1 * b1) * c0
    right = a0 * (b1 * c1) + a1 * (b0 * c1 + b1 * c0)
    three = a0 * b1 * c1 + a1 * b0 * c1 + a1 * b1 * c0
    assert left == right == three
    # and both equal the convolution coefficient
    def conv(p, q):
        out = [0] * (len(p) + len(q) - 1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i + j] += x * y
        return out
    assert conv(conv([a0, a1], [b0, b1]), [c0, c1])[2] == left
    assert conv([a0, a1], conv([b0, b1], [c0, c1]))[2] == right

# Quick check
assert list(mul((1, 1), (1, 1), 10**6)) == QUOTED["check_Q"]
assert list(mul((1, 1), (1, 1), 2)) == QUOTED["check_F2"]
print("thm-polynomial-ring-laws: ok")
