"""def-decimal-expansion examples: t_n = 1/2 for 5,0,0,...; t_n = 1/2 - 10^-n for 4,9,9,...;
t_n = 1 - 10^-n for 9,9,9,...; 0 for all zeros; non-example: 5,0,0,... and x = 0.51 satisfy
the inequalities at n = 1, 2 and fail first at n = 3."""
from fractions import Fraction as Fr

QUOTED = {"first_failure": 3}


def t(d, n):
    return sum(Fr(d(k), 10**k) for k in range(1, n + 1))


def ok(d, x, n):
    return t(d, n) <= x <= t(d, n) + Fr(1, 10**n)


half0 = lambda k: 5 if k == 1 else 0
half9 = lambda k: 4 if k == 1 else 9
nines = lambda k: 9
zeros = lambda k: 0
for n in range(1, 40):
    assert t(half0, n) == Fr(1, 2) and ok(half0, Fr(1, 2), n)
    assert t(half9, n) == Fr(1, 2) - Fr(1, 10**n) and ok(half9, Fr(1, 2), n)
    assert t(nines, n) == 1 - Fr(1, 10**n) and ok(nines, Fr(1), n)
    assert ok(zeros, Fr(0), n)
    # strict right inequality would exclude x = 1 for the all-nine sequence
    assert not (Fr(1) < t(nines, n) + Fr(1, 10**n))
x = Fr(51, 100)
fails = [n for n in range(1, 10) if not ok(half0, x, n)]
assert fails[0] == QUOTED["first_failure"] and ok(half0, x, 1) and ok(half0, x, 2)
print("def-decimal-expansion: all quoted values check")
