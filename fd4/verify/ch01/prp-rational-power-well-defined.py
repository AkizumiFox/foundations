"""prp-rational-power-well-defined (05) and the hook: 8^(2/3) = (cbrt 8)^2 = 4; (root6 8)^4 has sixth power 8^4 = 4096 = 4^6.
Representative independence checked exactly on bases a = c^(L) with all roots rational."""
from fractions import Fraction as F

QUOTED = {"hook": 4, "8^4": 4096}
assert 2 ** 3 == 8 and 2 ** 2 == QUOTED["hook"]
assert 8 ** 4 == QUOTED["8^4"] == QUOTED["hook"] ** 6


def ipow(a, n):
    return a ** n  # Fraction supports negative integer exponents as inverses


L = 60  # common multiple of the denominators used below
for c in [F(2), F(3, 5), F(7, 4)]:
    a = c ** L
    for m in range(-4, 5):
        for n in (1, 2, 3, 4, 5, 6):
            root_n = c ** (L // n)          # the n-th root of a: non-negative, n-th power a
            assert root_n ** n == a
            val = ipow(root_n, m)
            for t in (2, 3):
                if L % (n * t) == 0:
                    root_nt = c ** (L // (n * t))
                    assert root_nt ** (n * t) == a
                    assert ipow(root_nt, m * t) == val
            assert val > 0
            assert val ** n == ipow(a, m)   # u^n = a^m, the identity used with exponent nq
print("ok")
