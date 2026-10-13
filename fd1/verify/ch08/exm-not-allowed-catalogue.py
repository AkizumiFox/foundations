"""exm-not-allowed-catalogue (Ch 5, Section 5.6), with the Quick check before it:
- Quick check: n(n - 1) >= 0 for every integer n; at n = 1/2 it is -1/4.
- (N1) n^2 - n + 11 is prime for n = 0..10 with the listed values; 121 = 11^2 at n = 11.
- (N3) A = {-1, 1}: some element positive, not all.  (N4) m = 2, n = 4.
- (N5) x = -2: x^2 = 4 > 1, x > 1 fails.  (N6) 6 even, not a multiple of 4.
- (N7) |0| = 0.  (N8) x = 1/2: neither x >= 1 nor x <= 0, x^2 = 1/4 < 1/2.
- (N9) x = -2 < 1, x^2 = 4.  (N10) n = 1: 4 does not divide 1.
- (N11) x = 0: 'x > 2 -> x^2 > 4' and 'x <= 2 -> x^2 <= 4' both true; x > 2 -> x^2 > 4 for all
  real x; |a_n - 0| >= eps for every eps <= 0."""
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
print("exm-not-allowed-catalogue: all quoted values check")
