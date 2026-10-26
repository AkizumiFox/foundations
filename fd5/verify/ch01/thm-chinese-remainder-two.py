"""thm-chinese-remainder-two: x - a = m(bu - au), x - b = n(av - bv) when mu + nv = 1
(on a box of integers); the theorem on all coprime m, n <= 12 and all a, b; try-it-first numbers:
1 = 2*3 - 1*5, e = nv = -5, f = mu = 6, 2e + 3f = 8."""
from math import gcd
from itertools import product
# the identities hold whenever mu + nv = 1: check on all integer quadruples in a box
for m, n, u, v, a, b in product(range(-4, 5), repeat=6):
    if m * u + n * v != 1:
        continue
    x = a * n * v + b * m * u
    assert x - a == m * (b * u - a * u) and x - b == n * (a * v - b * v)
def bez(m, n):
    for U in range(-n, n + 1):
        for V in range(-m, m + 1):
            if m * U + n * V == 1:
                return U, V
for M in range(1, 13):
    for N in range(1, 13):
        if gcd(M, N) != 1:
            continue
        U, V = bez(M, N)
        for A in range(-5, 6):
            for B in range(-5, 6):
                X = A * N * V + B * M * U
                assert (X - A) % M == 0 and (X - B) % N == 0
                sols = [y for y in range(-60, 60) if (y - A) % M == 0 and (y - B) % N == 0]
                assert sols == [y for y in range(-60, 60) if (y - X) % (M * N) == 0]
        images = {(y % M, y % N) for y in range(M * N)}
        assert len(images) == M * N
QUOTED = {"uv": (2, -1), "e": -5, "f": 6, "x": 8}
assert 2 * 3 - 1 * 5 == 1
U, V = QUOTED["uv"]
e, f = 5 * V, 3 * U
assert (e, f) == (QUOTED["e"], QUOTED["f"]) and 2 * e + 3 * f == QUOTED["x"]
assert e % 3 == 1 and e % 5 == 0 and f % 3 == 0 and f % 5 == 1
print("ok")
