"""thm-integers-division-remainder and its aftermath in 01-division-with-remainder:
the Quick check (-17 by 5), the warning, the divisibility test instance (12 by 5),
and the divisions quoted in the small-primes remark."""
from fractions import Fraction as F
import math

QUOTED = {
    "check": (-17, 5, -4, 3),          # a, n, q, r
    "test": (12, 5, 2, 2),
    "warning_false": (-17, 5, -3, -2),  # a true equation, but -2 is not a remainder
    "small_primes": {
        3: [(2, 1, 1)],                                   # d, k, rem: p = k*d + rem
        5: [(2, 2, 1), (3, 1, 2), (4, 1, 1)],
        7: [(2, 3, 1), (3, 2, 1), (4, 1, 3), (5, 1, 2), (6, 1, 1)],
    },
}


def divmod_pos(a, n):
    assert n > 0
    q = math.floor(F(a, n))
    r = a - q * n
    assert 0 <= r < n
    return q, r


for key in ("check", "test"):
    a, n, q, r = QUOTED[key]
    assert divmod_pos(a, n) == (q, r) and a == q * n + r
a, n, q, r = QUOTED["check"]
assert math.floor(F(a, n)) == q == -4 and (-4) * 5 == -20 and -20 <= -17 < -15
a, n, q, r = QUOTED["warning_false"]
assert a == q * n + r and not (0 <= r < n)
# uniqueness: only one pair with 0 <= r < n
assert [(qq, a - qq * n) for qq in range(-50, 50) if 0 <= a - qq * n < n] == [(-4, 3)]
# 12 not divisible by 5
assert 12 % 5 == 2 and all(5 * k != 12 for k in range(-20, 21))
for p, rows in QUOTED["small_primes"].items():
    ds = [d for d, _, _ in rows]
    assert ds == list(range(2, p))
    for d, k, rem in rows:
        assert p == k * d + rem and 0 < rem < d and divmod_pos(p, d) == (k, rem)
    assert [d for d in range(1, p + 1) if p % d == 0] == [1, p]
print("ok")
