"""exm-chinese-remainder-instances: (i) x = 2*5*(-1) + 3*3*2 = 8, 8 = 2*3 + 2 = 1*5 + 3,
solutions 8 + 15Z (..., -7, 8, 23, 38, ...); (ii) x = 0 mod 2, x = 1 mod 4 has no solution;
x = 0 mod 2, x = 2 mod 4 has solutions 2 + 4Z, two classes mod 8 ([2], [6]); Phi on Z/8Z:
Phi([0]) = Phi([4]) = ([0],[0]) and ([0],[1]) not in the image; gcd(2, 4) = 2."""
from math import gcd
QUOTED = {"x": 8, "list": [-7, 8, 23, 38], "classes8": [2, 6]}
assert 2 * 5 * (-1) + 3 * 3 * 2 == QUOTED["x"] and 8 == 2 * 3 + 2 == 1 * 5 + 3
sols = [y for y in range(-20, 50) if y % 3 == 2 and y % 5 == 3]
assert sols == [y for y in range(-20, 50) if (y - 8) % 15 == 0]
assert all(y in sols for y in QUOTED["list"])
assert not [y for y in range(-100, 100) if y % 2 == 0 and y % 4 == 1]
s2 = [y for y in range(-100, 100) if y % 2 == 0 and y % 4 == 2]
assert s2 == [y for y in range(-100, 100) if (y - 2) % 4 == 0]
assert sorted({y % 8 for y in s2}) == QUOTED["classes8"] and (6 - 2) % 8 != 0
phi = {c: (c % 2, c % 4) for c in range(8)}
assert phi[0] == phi[4] == (0, 0) and (0, 1) not in phi.values()
assert gcd(2, 4) == 2
# remark after the example: [x] -> [2][x] on Z/5Z, [3][2] = [6] = [1], injective and onto
assert 3 * 2 == 6 and 6 % 5 == 1
assert sorted({2 * c % 5 for c in range(5)}) == list(range(5))
print("ok")
