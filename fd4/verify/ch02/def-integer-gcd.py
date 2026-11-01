"""def-integer-gcd examples (02-gcd-and-bezout): gcd(4, 6) = 2 via 6 = 1*4 + 2, 4 = 1*3 + 1;
gcd(-5, 5) = 5; gcd(1, b) = 1."""
import math
QUOTED = {(4, 6): 2, (-5, 5): 5}
assert 6 == 1 * 4 + 2 and 4 == 1 * 3 + 1
for (a, b), g in QUOTED.items():
    common = [d for d in range(-50, 51) if d != 0 and a % d == 0 and b % d == 0]
    assert max(common) == g == math.gcd(a, b)
for b in range(-30, 31):
    assert math.gcd(1, b) == 1
print("ok")
