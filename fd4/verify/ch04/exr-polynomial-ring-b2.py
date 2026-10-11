"""exr-polynomial-ring-b2 (Section 4.2): sigma(p)_k = (-1)^k p_k is multiplicative,
checked on random pairs over Z/nZ, and sigma(1) = 1."""
import random

QUOTED = {}


def mul(p, q, n):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = (out[i + j] + a * b) % n
    return out


def sigma(p, n):
    return [((-1) ** k * c) % n for k, c in enumerate(p)]


rng = random.Random(2)
for _ in range(5000):
    n = rng.randint(1, 12)
    p = [rng.randrange(n) for _ in range(rng.randint(1, 6))]
    q = [rng.randrange(n) for _ in range(rng.randint(1, 6))]
    assert sigma(mul(p, q, n), n) == mul(sigma(p, n), sigma(q, n), n)
    assert sigma([1 % n], n) == [1 % n]
print("exr-polynomial-ring-b2: ok")
