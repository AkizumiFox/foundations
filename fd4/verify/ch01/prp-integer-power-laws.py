"""prp-integer-power-laws (05): all sign cases checked exactly in Q; Quick check 2^-3 * 4^2 = 2, (2/3)^-2 = 9/4;
def-integer-power example 2^-3 = 1/8."""
from fractions import Fraction as F

QUOTED = {"qc1": F(2), "qc2": F(9, 4), "two_m3": F(1, 8)}


def ipow(a, n):
    """a^n by the book's definition: recursion for n >= 0, (a^{-1})^{-n} for n < 0."""
    if n < 0:
        return ipow(1 / a, -n)
    r = F(1)
    for _ in range(n):
        r *= a
    return r


assert ipow(F(2), -3) == QUOTED["two_m3"]
assert ipow(F(2), -3) * ipow(F(4), 2) == QUOTED["qc1"]
assert ipow(F(2, 3), -2) == QUOTED["qc2"]
vals = [F(2), F(-3), F(1, 2), F(-5, 7), F(3, 2)]
for a in vals:
    for b in vals:
        for m in range(-5, 6):
            for n in range(-5, 6):
                assert ipow(a, m + n) == ipow(a, m) * ipow(a, n)
                assert ipow(ipow(a, m), n) == ipow(a, m * n)
                assert ipow(a * b, n) == ipow(a, n) * ipow(b, n)
                assert ipow(a, n) != 0 and ipow(a, -n) == 1 / ipow(a, n)
                if a > 0:
                    assert ipow(a, n) > 0
                if a > 1 and m < n:
                    assert ipow(a, m) < ipow(a, n)
print("ok")
