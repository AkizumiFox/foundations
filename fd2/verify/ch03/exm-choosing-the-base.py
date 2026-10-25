"""exm-choosing-the-base (F2.2, 02), with the scratch-work example, the two Quick checks
of the subsection on finding the step, and the gallery's Quick check."""
from fractions import Fraction
# Scratch work and proof: 9^(n+1) - 2^(n+1) = 9(9^n - 2^n) + 7*2^n; 7 | 9^n - 2^n.
for n in range(0, 200):
    assert (9 ** n - 2 ** n) % 7 == 0
    k = (9 ** n - 2 ** n) // 7
    assert 9 ** (n + 1) - 2 ** (n + 1) == 9 * (9 ** n - 2 ** n) + 7 * 2 ** n == 7 * (9 * k + 2 ** n)
# Quick check: 9^(n+1) - 4^(n+1) = 9(9^n - 4^n) + 5*4^n.
for n in range(0, 200):
    assert (9 ** n - 4 ** n) % 5 == 0
    k = (9 ** n - 4 ** n) // 5
    assert 9 ** (n + 1) - 4 ** (n + 1) == 9 * (9 ** n - 4 ** n) + 5 * 4 ** n == 5 * (9 * k + 4 ** n)
# The example: 3^n >= n^3 for all n; small cases.
assert (3 ** 0, 3 ** 1, 3 ** 2, 3 ** 3) == (1, 3, 9, 27) and (0, 1, 8, 27) == tuple(n ** 3 for n in range(4))
for n in range(0, 300):
    assert 3 ** n >= n ** 3
# The chain 2n^3 >= 6n^2 >= 3n^2 + 9n >= 3n^2 + 3n + 1 for n >= 3, and (n+1)^3 expanded.
for n in range(3, 2000):
    assert 2 * n ** 3 >= 6 * n ** 2 >= 3 * n ** 2 + 9 * n >= 3 * n ** 2 + 3 * n + 1
    assert (n + 1) ** 3 == n ** 3 + 3 * n ** 2 + 3 * n + 1
# Quick check: 3n^3 < (n+1)^3 exactly at n = 0, 1, 2 (0 < 1, 3 < 8, 24 < 27).
assert [n for n in range(0, 2000) if 3 * n ** 3 < (n + 1) ** 3] == [0, 1, 2]
assert [(3 * n ** 3, (n + 1) ** 3) for n in range(3)] == [(0, 1), (3, 8), (24, 27)]
# Gallery check: n^2 <= 2^n for n >= 4 (16 <= 16), false at 3 (9 > 8); 2n^2 >= (n+1)^2 for n >= 3.
assert 4 ** 2 == 16 == 2 ** 4 and 3 ** 2 == 9 > 8 == 2 ** 3
for n in range(4, 500):
    assert n * n <= 2 ** n
assert [n for n in range(0, 2000) if 2 * n * n < (n + 1) ** 2] == [0, 1, 2]
# The step run backwards: n^2 >= 2n for n >= 2; (n+1)^2 = n^2 + 2n + 1 >= 2n + 2 from n^2 >= 1.
for n in range(2, 500):
    assert n * n >= 2 * n and (n + 1) ** 2 == n * n + 2 * n + 1 >= 2 * n + 2
assert 1 != -1 and 1 ** 2 == (-1) ** 2
print("exm-choosing-the-base: all quoted values check")
