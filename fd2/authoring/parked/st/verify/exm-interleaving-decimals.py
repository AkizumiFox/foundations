"""exm-interleaving-decimals: 0.090909... is an expansion of 1/11; the bound z <= 1 - 10^-n."""
from fractions import Fraction as F
import itertools

QUOTED = {"z": F(1, 11)}


def truncs(digits):
    t, out = F(0), []
    for k, d in enumerate(digits, start=1):
        t += F(d, 10**k)
        out.append(t)
    return out


# 0.0909...: digits 0 at odd places, 9 at even places
digits = [0 if k % 2 == 1 else 9 for k in range(1, 41)]
t = truncs(digits)
for n, tn in enumerate(t, start=1):
    assert tn <= QUOTED["z"] <= tn + F(1, 10**n)
for j in range(1, 21):
    assert t[2 * j - 1] == F(9, 99) * (1 - F(1, 100**j)) == F(1, 11) - F(1, 11) * F(1, 100**j)
# bound: n = first place with digit <= 8, all earlier digits 9
for n in range(1, 8):
    for last in range(9):
        ds = [9] * (n - 1) + [last]
        tn = truncs(ds)[-1]
        assert tn <= (1 - F(1, 10**(n - 1))) + 8 * F(1, 10**n) == 1 - 2 * F(1, 10**n)
        assert tn + F(1, 10**n) <= 1 - F(1, 10**n) < 1
# reals proof: digits 0 and 1 give y_b <= t_1 + 1/10 <= 2/10; A1 (d): first digit <= 8 gives < 1
for d1 in (0, 1):
    assert F(d1, 10) + F(1, 10) <= F(2, 10)
assert F(8, 10) + F(1, 10) < 1
print("ok")
