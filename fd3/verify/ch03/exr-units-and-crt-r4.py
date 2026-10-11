"""exr-units-and-crt-r4: 6x = 4 mod 10 iff x = 4 mod 5; 3*2 = 6 = 5 + 1; 3*4 = 12 = 2 mod 5;
6*4 - 4 = 20, 6*9 - 4 = 50; gcd(6, 10) = 2; classes mod 10 are [4], [9]."""
from math import gcd
assert [y for y in range(-50, 50) if (6 * y - 4) % 10 == 0] == [y for y in range(-50, 50) if y % 5 == 4]
assert 3 * 2 == 6 == 5 + 1 and 12 % 5 == 2 and (2 * 2) % 5 == 4
assert 6 * 4 - 4 == 20 and 6 * 9 - 4 == 50 and gcd(6, 10) == 2
assert sorted({y % 10 for y in range(-50, 50) if y % 5 == 4}) == [4, 9]
print("ok")
