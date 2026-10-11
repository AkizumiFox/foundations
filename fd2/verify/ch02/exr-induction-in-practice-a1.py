"""exr-induction-in-practice-a1 (Ch 7, 02): (i) 6 | 7^n - 1; (ii) 2^n > n^2 for n >= 5, fails at 2, 3, 4,
2n^2 >= (n+1)^2 for n >= 3; (iii) n >= 12 is 3a + 7b, base cases 12, 13, 14, and 11 is not;
(iv) n^2 = 2m^2 has no positive solution (checked on a range); (d) a = 2: a^1 = 2 != 1, a^-1 = 1/2."""
from fractions import Fraction as F

def rep(n, x, y):
    return any((n - y * b) >= 0 and (n - y * b) % x == 0 for b in range(n // y + 1))

assert all((7 ** n - 1) % 6 == 0 for n in range(80))
assert all(2 ** n > n * n for n in range(5, 300))
assert [n for n in range(0, 5) if not 2 ** n > n * n] == [2, 3, 4]
assert all(2 * n * n >= (n + 1) ** 2 for n in range(3, 300)) and not 2 * 4 >= 9
assert 12 == 3 * 4 and 13 == 3 * 2 + 7 and 14 == 7 * 2
assert all(rep(n, 3, 7) for n in range(12, 400)) and not rep(11, 3, 7)
assert not any(n * n == 2 * m * m for n in range(1, 2000) for m in range(1, n))
a = F(2)
assert a ** 1 != 1 and a ** -1 == F(1, 2) != 1
for n in range(1, 30):
    assert a ** n * a ** n / a ** (n - 1) == a ** (n + 1)
print("exr-induction-in-practice-a1: all quoted values check")
