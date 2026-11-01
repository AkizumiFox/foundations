"""lem-root-rules (05) and its Quick check: cbrt(sqrt(64)) = sixth root of 64 = 2; sqrt 64 = 8, cbrt 8 = 2.
Also lem-reals-nth-root's quoted 2^3 = 8, (sqrt 2)^4 = ((sqrt 2)^2)^2 = 4.
Roots are identified exactly as in the text: a candidate c >= 0 with c^n = a."""
from fractions import Fraction as F

QUOTED = {"sqrt64": 8, "cbrt8": 2, "root6_64": 2}


def is_root(c, a, n):
    return c >= 0 and F(c) ** n == a


assert is_root(QUOTED["root6_64"], 64, 6)
assert is_root(QUOTED["sqrt64"], 64, 2) and is_root(QUOTED["cbrt8"], QUOTED["sqrt64"], 3)
assert is_root(2, 8, 3) and 2 ** 2 == 4  # (sqrt 2)^4 = 2^2
# (a)-(c) on exact perfect powers: x = p^? chosen so all roots are rational
for n in range(1, 6):
    for m in range(1, 5):
        for x in [F(1, 3), F(2), F(5, 7), F(0)]:
            for y in [F(3), F(1, 2)]:
                a, b = x ** n, y ** n
                assert is_root(x * y, a * b, n)          # (a)
                assert is_root(x ** m, a ** m, n)        # (b)
                z = x  # a = z^(mn) case for (c)
                assert is_root(z ** n, z ** (m * n), m) and is_root(z, z ** (m * n), m * n)
                if a < b:
                    assert x < y                         # (d)
print("ok")
