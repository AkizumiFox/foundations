"""prp-log2-9-irrational (Ch 5, Section 5.7): log2 9 > 0; 2^p = 9^q is impossible for
p, q >= 1 (even vs odd); log2 9 = 2 log2 3; (2^(1/2))^(log2 9) = 2^(log2 3) = 3.
Also the motivating sentence before it: sqrt2^(log2(m^2)) = m, and m = 2 gives b = 2."""
from decimal import Decimal, getcontext

QUOTED = {"a_pow_b": 3, "b_for_m2": 2}

getcontext().prec = 80
ln2 = Decimal(2).ln()
log2 = lambda x: Decimal(x).ln() / ln2
r2 = Decimal(2).sqrt()

b = log2(9)
assert b > 0
assert abs(b - 2 * log2(3)) < Decimal(10) ** -70
assert abs(r2 ** b - QUOTED["a_pow_b"]) < Decimal(10) ** -60
assert abs(Decimal(2) ** (b / 2) - 3) < Decimal(10) ** -60

# parity clash: 2^p even for p >= 1, 9^q odd for q >= 1, so never equal
for p in range(1, 200):
    assert (2 ** p) % 2 == 0
for q in range(1, 200):
    assert (9 ** q) % 2 == 1

# the motivation: sqrt2^(log2(m^2)) = m; m = 2 gives b = 2 (rational)
for m in range(2, 60):
    assert abs(r2 ** log2(m * m) - m) < Decimal(10) ** -55
assert abs(log2(4) - QUOTED["b_for_m2"]) < Decimal(10) ** -70
print("prp-log2-9-irrational: all quoted values check")
