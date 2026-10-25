"""exr-induction-in-practice-b4 (F2.2, 02): verdicts T, F, T, F, T, F and every quoted value."""
from fractions import Fraction
def is_prime(m):
    return m >= 2 and all(m % d for d in range(2, int(m ** 0.5) + 1))
# (a) True: 3 | 2^(2n+1) + 1; 2^(2n+3) + 1 = 4(2^(2n+1) + 1) - 3 = 3(4k - 1).
assert 2 ** 1 + 1 == 3
for n in range(0, 200):
    v = 2 ** (2 * n + 1) + 1
    assert v % 3 == 0
    k = v // 3
    assert 2 ** (2 * n + 3) + 1 == 4 * v - 3 == 3 * (4 * k - 1)
# (b) False at 9 only: 512 < 729; holds from 10 on; 2n^3 >= (n+1)^3 for n >= 10.
assert 2 ** 9 == 512 < 729 == 9 ** 3 and 2 ** 10 == 1024 >= 1000
assert [n for n in range(9, 500) if 2 ** n < n ** 3] == [9]
for n in range(10, 2000):
    assert 2 * n ** 3 >= (n + 1) ** 3
# (c) True: sum_{j=0}^{n} (3j + 1) = (n + 1)(3n + 2)/2; the step identity.
for n in range(0, 500):
    assert 2 * sum(3 * j + 1 for j in range(n + 1)) == (n + 1) * (3 * n + 2)
    assert Fraction((n + 1) * (3 * n + 2), 2) + (3 * n + 4) == Fraction(3 * n * n + 11 * n + 10, 2) == Fraction((n + 2) * (3 * n + 5), 2)
# (d) False: 11 is not 3a + 7b; 11 - 7b in {11, 4} for b in {0, 1}; every other n >= 10 up to 500 is.
rep = lambda n: any((n - 7 * b) >= 0 and (n - 7 * b) % 3 == 0 for b in range(n // 7 + 1))
assert not rep(11) and [11 - 7 * b for b in (0, 1)] == [11, 4] and 11 - 14 < 0
assert divmod(11, 3) == (3, 2) and divmod(4, 3) == (1, 1)
assert [n for n in range(10, 500) if not rep(n)] == [11]
# (e) True from 2: 25 >= 16 + 9; fails at 1 (5 < 7) and 0 (1 < 2); 5*4^n >= 4*4^n.
assert 25 >= 16 + 9 and 5 < 4 + 3 and 1 < 1 + 1
for n in range(2, 300):
    assert 5 ** n >= 4 ** n + 3 ** n
# (f) False: 65 = 5 * 13 at n = 8; 5, 17, 37 prime at 2, 4, 6; 8 is the first failure.
assert [n * n + 1 for n in (2, 4, 6, 8)] == [5, 17, 37, 65] and 65 == 5 * 13
assert all(is_prime(v) for v in (5, 17, 37)) and not is_prime(65)
assert min(n for n in range(2, 100, 2) if not is_prime(n * n + 1)) == 8
print("exr-induction-in-practice-b4: all quoted values check (T F T F T F)")
