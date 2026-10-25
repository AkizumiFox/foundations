"""exr-checking-proofs-a2 (Section 8.6): (a) n^2 + n = n(n + 1) is even; (c) x = 1, y = 3 odd, not
both 2k + 1; (d) n = 2 even, not divisible by 4; (e) (2k)^3 - 2k = 2(4k^3 - k), n^3 - n even;
(f) x = 0: x^2 > 0 fails; (g) |x| >= -1 for all x, and at x = 0 the original holds; (i) x = y = 3
solve x^2 = 9, x + y = 6; (j) a_1 = 2, a_{n+1} = a_n^2 - 2 gives a_n = 2; (k) no integer squares
to 2; (l) the propositional step is valid (truth table)."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"c": (1, 3), "d": 2, "i": (3, 3, 6)}
for n in range(-300, 301):
    assert (n * n + n) % 2 == 0 and n * n + n == n * (n + 1)
    assert (n ** 3 - n) % 2 == 0 and n ** 3 - n == (n - 1) * n * (n + 1)
for k in range(-100, 101):
    assert (2 * k) ** 3 - 2 * k == 2 * (4 * k ** 3 - k)
x, y = QUOTED["c"]
assert x % 2 == 1 and y % 2 == 1 and x != y
n = QUOTED["d"]
assert n % 2 == 0 and n % 4 != 0
assert not (0 * 0 > 0)
for k in range(-100, 101):
    xx = F(k, 10)
    assert abs(xx) >= -1
assert all(abs(0) < e for e in [F(1), F(1, 1000)])     # original holds at x = 0
x, y, s = QUOTED["i"]
assert x * x == 9 and y * y == 9 and x + y == s
a = 2
for _ in range(50):
    assert a == 2
    a = a * a - 2
assert all(m * m != 2 for m in range(-100, 101))
for X, Y, Z in product([False, True], repeat=3):
    imp = lambda p, q: (not p) or q
    if X and (imp(X, Y) and imp(Y, Z)):
        assert Z
print("exr-checking-proofs-a2: all quoted values check")
