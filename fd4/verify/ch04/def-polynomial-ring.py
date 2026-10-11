"""def-polynomial-ring (Section 4.2): the warning (a coefficientwise product would give
x * x = x; the convolution gives x * x = x^2), and the closure bound m + n on random data."""
import random

QUOTED = {
    "x": [0, 1, 0],
    "x_times_x_position_2": 1,     # 0 + 1 + 0
}


def mul(p, q, n=None):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return [c % n for c in out] if n else out


x = QUOTED["x"]
assert [a * b for a, b in zip(x, x)] == x                  # the wrong rule
xx = mul(x, x)
assert xx[2] == QUOTED["x_times_x_position_2"] and xx == [0, 0, 1, 0, 0]
# closure: if m, n admissible, (pq)_k = 0 for k > m + n (convolution with zero padding)
rng = random.Random(4)
for _ in range(2000):
    n_mod = rng.randint(2, 9)
    m, n = rng.randint(0, 5), rng.randint(0, 5)
    p = [rng.randrange(n_mod) for _ in range(m + 1)] + [0] * 4
    q = [rng.randrange(n_mod) for _ in range(n + 1)] + [0] * 4
    pq = mul(p, q, n_mod)
    assert all(c == 0 for c in pq[m + n + 1:])
print("def-polynomial-ring: ok")
