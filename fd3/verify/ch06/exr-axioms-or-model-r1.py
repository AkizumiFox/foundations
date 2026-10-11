"""exr-axioms-or-model-r1: binary truncations of sqrt 2.
k_n = largest natural k with k^2 <= 2 (2^n)^2, q_n = k_n / 2^n.
Checks the quoted values q_0..q_5, the bounds 1 <= q_n < 2, (q_n + 1/2^n)^2 > 2,
monotonicity via 2 k_n <= k_{n+1}, the gap bound 0 <= q_m - q_n < 1/2^n <= 1/(n+1),
and 0 <= 2 - q_n^2 < (1/2^n)(2 q_n + 1/2^n) <= 5/2^n <= 5/(n+1); exact fractions."""
from fractions import Fraction
Fr = Fraction
from math import isqrt
QUOTED = {"q": [1, 1, Fraction(5, 4), Fraction(11, 8), Fraction(11, 8), Fraction(45, 32)]}

def k(n):
    kk = isqrt(2 * (2 ** n) ** 2)
    assert kk * kk <= 2 * (2 ** n) ** 2 < (kk + 1) ** 2
    return kk

def q(n):
    return Fr(k(n), 2 ** n)

assert [q(n) for n in range(6)] == QUOTED["q"]
NMAX = 60
for n in range(NMAX):
    p = Fr(1, 2 ** n)
    assert 2 ** n >= n + 1
    assert 1 <= q(n) < 2
    assert (q(n) + p) ** 2 > 2 and q(n) ** 2 <= 2
    assert (2 * k(n)) ** 2 == 4 * k(n) ** 2 and 8 * (2 ** n) ** 2 == 2 * (2 ** (n + 1)) ** 2
    assert 2 * k(n) <= k(n + 1)
    assert 0 <= 2 - q(n) ** 2 < p * (2 * q(n) + p) <= 5 * p <= Fr(5, n + 1)
    # the expansion used in (c)
    assert (q(n) + p) ** 2 == q(n) ** 2 + 2 * q(n) * p + p * p
    for m in range(n, NMAX):
        assert 0 <= q(m) - q(n) < p <= Fr(1, n + 1)
print("ok")
