"""exr-cardinal-arithmetic-a1 (d): with digits missing 9 the first digit is <= 8, so y_b <= 8/10 + 1/10 < 1;
with a pair containing 9 the all-9 sequence has truncations 1 - 10^-n, so it is the expansion of 1."""
from fractions import Fraction as F

QUOTED = {"first": r"\frac{8}{10}", "step": F(1, 10)}
FIRST = F(8, 10)

assert FIRST + QUOTED["step"] < 1
for n in range(1, 30):
    t = sum(F(9, 10**k) for k in range(1, n + 1))
    assert t == 1 - F(1, 10**n) and t <= 1 <= t + F(1, 10**n)
print("ok")
