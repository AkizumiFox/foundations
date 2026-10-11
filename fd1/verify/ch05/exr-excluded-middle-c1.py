"""exr-excluded-middle-c1 (Ch 5, Section 5.7): (a) sqrt2^(log2 25) = 5, log2 25 = 2 log2 5 > 0,
2^p = 25^q impossible by parity. (b) sqrt2^(log2(m^2)) = m for every m >= 2; m a power of 2
gives b = 2k rational; otherwise m = 2^k r with r odd >= 3 and r^(2q) = 2^(p - 2kq) is
impossible (odd vs even), with p > 2kq forced by r^(2q) > 1. Smallest working m: 3, 5, 6, 7."""
from decimal import Decimal, getcontext

QUOTED = {"a_pow_b_25": 5, "smallest": [3, 5, 6, 7]}

getcontext().prec = 80
ln2 = Decimal(2).ln()
log2 = lambda x: Decimal(x).ln() / ln2
r2 = Decimal(2).sqrt()
tol = Decimal(10) ** -55

assert abs(r2 ** log2(25) - QUOTED["a_pow_b_25"]) < tol
assert abs(log2(25) - 2 * log2(5)) < tol and log2(25) > 0
for p in range(1, 150):
    for q in range(1, 40):
        assert 2 ** p != 25 ** q


def split(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k, m


def is_power_of_two(m):
    return m >= 1 and m & (m - 1) == 0


working = []
for m in range(2, 300):
    assert abs(r2 ** log2(m * m) - m) < tol
    k, r = split(m)
    assert m == 2 ** k * r and r % 2 == 1
    if r == 1:
        assert is_power_of_two(m) and abs(log2(m * m) - 2 * k) < tol
    else:
        assert r >= 3 and not is_power_of_two(m)
        working.append(m)
        # the clash: 2^p = 2^(2kq) r^(2q) would force r^(2q) = 2^(p-2kq), p - 2kq >= 1
        for q in range(1, 4):
            rq = r ** (2 * q)
            assert rq > 1 and rq % 2 == 1  # odd, so never a positive power of 2
assert working[:4] == QUOTED["smallest"]
print("exr-excluded-middle-c1: all quoted values check")
