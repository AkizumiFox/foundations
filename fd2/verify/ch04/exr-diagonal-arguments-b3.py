"""exr-diagonal-arguments-b3: sum_{k<=n} 10^-k = (1 - 10^-n)/9; all-threes has
t_n = 1/3 - 10^-n/3 and is an expansion of 1/3; a digit <= 8 at place m forces
t_m + 10^-m <= 1 - 10^-m < 1 (checked on all short digit strings)."""
from fractions import Fraction as Fr
from itertools import product

QUOTED = {}
for n in range(1, 30):
    assert sum(Fr(1, 10**k) for k in range(1, n + 1)) == (1 - Fr(1, 10**n)) / 9
    tn = sum(Fr(3, 10**k) for k in range(1, n + 1))
    assert tn == Fr(1, 3) - Fr(1, 3 * 10**n)
    assert tn <= Fr(1, 3) <= tn + Fr(1, 10**n)
for m in range(1, 5):
    for digs in product(range(10), repeat=m):
        if min(digs) <= 8:
            tm = sum(Fr(d, 10**(k + 1)) for k, d in enumerate(digs))
            assert tm <= 1 - 2 * Fr(1, 10**m)
            assert tm + Fr(1, 10**m) < 1
print("exr-diagonal-arguments-b3: all quoted values check")
