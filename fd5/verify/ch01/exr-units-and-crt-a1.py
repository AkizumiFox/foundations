"""exr-units-and-crt-a1: [5]^{-1} = [5] mod 12 (25 = 2*12 + 1); units of Z/12Z are
[1],[5],[7],[11], each its own inverse (1, 25, 49, 121); 4*(-2) + 9*1 = 1;
x = 1*9*1 + 2*4*(-2) = -7; solutions 29 + 36Z; 29 = 7*4 + 1 = 3*9 + 2."""
from math import gcd
QUOTED = {"units": [1, 5, 7, 11], "x": -7, "rep": 29}
assert 25 == 2 * 12 + 1
assert [a for a in range(12) if gcd(a, 12) == 1] == QUOTED["units"]
assert all(a * a % 12 == 1 for a in QUOTED["units"]) and [1, 25, 49, 121] == [a * a for a in QUOTED["units"]]
assert 4 * (-2) + 9 * 1 == 1
assert 1 * 9 * 1 + 2 * 4 * (-2) == QUOTED["x"] and QUOTED["x"] + 36 == QUOTED["rep"]
assert 29 == 7 * 4 + 1 == 3 * 9 + 2
assert [y for y in range(36) if y % 4 == 1 and y % 9 == 2] == [29]
print("ok")
