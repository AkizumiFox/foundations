"""lem-monomial-product (Section 4.2): multiplying by a x^m shifts by m and scales by a;
(a x^m)(b x^n) = (ab) x^(m+n). Checked on random data over Z/nZ."""
import random

QUOTED = {}


def mul(p, q, n):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = (out[i + j] + a * b) % n
    return out


def mono(a, m, length):
    v = [0] * length
    v[m] = a
    return v


rng = random.Random(7)
for _ in range(3000):
    n = rng.randint(2, 12)
    a, b = rng.randrange(n), rng.randrange(n)
    m, k = rng.randint(0, 6), rng.randint(0, 6)
    q = [rng.randrange(n) for _ in range(rng.randint(1, 6))]
    prod = mul(mono(a, m, m + 1), q, n)
    for idx in range(len(prod)):
        expected = (a * q[idx - m]) % n if idx >= m and idx - m < len(q) else 0
        assert prod[idx] == expected
    prod2 = mul(mono(a, m, m + 1), mono(b, k, k + 1), n)
    assert prod2 == mono((a * b) % n, m + k, m + k + 1)
print("lem-monomial-product: ok")
