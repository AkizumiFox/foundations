"""exm-not-allowed-catalogue (Ch 5, Section 5.6), with the Quick check before it:
- Quick check: n(n - 1) >= 0 for every integer n; at n = 1/2 it is -1/4.
- (N1) n^2 - n + 11 is prime for n = 0..10 with the listed values; 121 = 11^2 at n = 11.
- (N3) A = {-1, 1}: some element positive, not all.  (N4) m = 2, n = 4.
- (N5) x = -2: x^2 = 4 > 1, x > 1 fails.  (N6) 6 even, not a multiple of 4.
- (N7) |0| = 0.  (N8) x = 1/2: neither x >= 1 nor x <= 0, x^2 = 1/4 < 1/2.
- (N9) x = -2 < 1, x^2 = 4.  (N10) n = 1: 4 does not divide 1.
- (N11) x = 0: 'x > 2 -> x^2 > 4' and 'x <= 2 -> x^2 <= 4' both true; x > 2 -> x^2 > 4 for all
  real x; |a_n - 0| >= eps for every eps <= 0.
Section 8.6 additions:
- 2x2 table: n = 2k gives n^2 = 2(2k^2); forall-E at 1/2 of "x >= 1 or x <= 0" is false; x = -2.
- (N11)(a): 0 < x < 3 gives x^2 < 9; x^2 > 9 and x > 0 give x > 3; x = 3 has x^2 = 9.
- (N12): the roots of x^2 - 5x + 6 are 2 and 3; a = b = 2 are roots and 2 + 2 = 4 != 5.
- (N13): 1/(n + 1) < 1/n, so {1/n : n >= 1} has no least element.
- (N14): N largest would give N + 1 <= N, i.e. 1 <= 0.
- F8.6-b: a strictly decreasing list in N from a_1 has at most a_1 + 1 terms (search, a_1 <= 30);
  8 is the least positive m with m^2 > 50 (7^2 = 49, 8^2 = 64).
- valid but improper: a^2 + b^2 >= 2ab for reals a, b (grid), symmetric in a, b.
- family Quick check: n^2 = n + 6 at n = 3, not at n = 0."""
from fractions import Fraction as F

QUOTED = {
    "N1_values": [11, 11, 13, 17, 23, 31, 41, 53, 67, 83, 101],
    "N1_at_11": 121,
    "check_half": F(-1, 4),
}

def prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))

for n in range(-500, 501):
    assert n * (n - 1) >= 0
h = F(1, 2)
assert h * (h - 1) == QUOTED["check_half"]

vals = [n * n - n + 11 for n in range(11)]
assert vals == QUOTED["N1_values"] and all(prime(v) for v in vals)
assert 11 * 11 - 11 + 11 == QUOTED["N1_at_11"] == 11 ** 2 and not prime(121)

A = [-1, 1]
assert any(a > 0 for a in A) and not all(a > 0 for a in A)
m, n = 2, 4
assert m % 2 == 0 and n % 2 == 0 and m != n
x = -2
assert x * x > 1 and not x > 1                      # N5
assert 6 % 2 == 0 and 6 % 4 != 0                    # N6 (both patterns)
assert abs(0) == 0                                  # N7
x = F(1, 2)
assert not (x >= 1 or x <= 0) and x * x == F(1, 4) < x     # N8
x = -2
assert x < 1 and x * x == 4 and not x * x < 1       # N9
assert 1 % 4 != 0                                   # N10
x = 0
assert ((not x > 2) or x * x > 4) and ((not x <= 2) or x * x <= 4)   # N11
for k in range(-300, 301):
    x = F(k, 7)
    if x > 2:
        assert x * x > 4
for eps in [F(0), F(-1), F(-1, 3)]:
    assert all(abs(0 - 0) >= eps for _ in range(10))
# --- Section 8.6 additions ---
for k in range(-50, 51):
    assert (2 * k) ** 2 == 2 * (2 * k * k)
h = F(1, 2)
assert not (h >= 1 or h <= 0)
assert -2 < 1 and (-2) ** 2 == 4 and not 4 < 1
for k in range(-500, 501):
    x = F(k, 50)
    if 0 < x < 3:
        assert x * x < 9
    if x * x > 9 and x > 0:
        assert x > 3
assert 3 * 3 == 9 and not 3 * 3 > 9
roots = [x for x in range(-20, 21) if x * x - 5 * x + 6 == 0]
assert roots == [2, 3]
a = b = 2
assert a * a - 5 * a + 6 == 0 and a + b == 4 != 5
for n in range(1, 2000):
    assert F(1, n + 1) < F(1, n)
N = 10 ** 6
assert not (N + 1 <= N)              # the step N + 1 <= N fails for every actual N
def longest(a1):
    # longest strictly decreasing list of naturals starting at a1
    return 1 + max([longest(b) for b in range(a1)], default=0)
from functools import lru_cache
longest = lru_cache(None)(longest)
for a1 in range(31):
    assert longest(a1) == a1 + 1
assert 7 ** 2 == 49 <= 50 < 64 == 8 ** 2
assert min(m for m in range(1, 100) if m * m > 50) == 8
for i in range(-40, 41):
    for j in range(-40, 41):
        a, b = F(i, 7), F(j, 5)
        assert a * a + b * b >= 2 * a * b and b * b + a * a >= 2 * b * a
assert 3 * 3 == 3 + 6 and not 0 * 0 == 0 + 6
print("exm-not-allowed-catalogue: all quoted values check")
