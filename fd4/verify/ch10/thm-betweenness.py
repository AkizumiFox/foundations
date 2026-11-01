"""thm-betweenness: moreover clause (on squares, exact); off-segment points give a strict inequality; warning data."""
import random
from fractions import Fraction as Fr
from math import sqrt, isclose

QUOTED = {"warn_sq": 2, "pq": 2}


def sq(x):
    return sum(Fr(c) ** 2 for c in x)


def comb(a, x, b, y):
    return tuple(a * xi + b * yi for xi, yi in zip(x, y))


p, q, x = (-1, 0), (1, 0), (0, 1)
assert sq(comb(1, p, -1, x)) == QUOTED["warn_sq"] == sq(comb(1, x, -1, q))
assert sq(comb(1, p, -1, q)) == QUOTED["pq"] ** 2
assert (2 * sqrt(2)) != 2 and Fr(8) != 4  # (2 sqrt 2)^2 = 8 != 4 = 2^2
random.seed(5)
for _ in range(300):
    n = random.randint(1, 4)
    P = tuple(Fr(random.randint(-5, 5)) for _ in range(n)); Q = tuple(Fr(random.randint(-5, 5)) for _ in range(n))
    t = Fr(random.randint(0, 12), 12)
    X = comb(1 - t, P, t, Q)
    # ||p - x||^2 = t^2 ||p - q||^2, ||x - q||^2 = (1 - t)^2 ||p - q||^2
    assert sq(comb(1, P, -1, X)) == t * t * sq(comb(1, P, -1, Q))
    assert sq(comb(1, X, -1, Q)) == (1 - t) ** 2 * sq(comb(1, P, -1, Q))
    T = Fr(random.choice([-3, -1, 13, 20]), 12)
    Y = comb(1 - T, P, T, Q)
    if P != Q:
        lhs = sqrt(sq(comb(1, P, -1, Y))) + sqrt(sq(comb(1, Y, -1, Q)))
        assert lhs > sqrt(sq(comb(1, P, -1, Q))) + 1e-9
print("ok")
