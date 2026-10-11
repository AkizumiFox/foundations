"""exm-unit-inverse-mod-n: Euclid on (60, 17): 60 = 3*17 + 9, 17 = 1*9 + 8, 9 = 1*8 + 1,
8 = 8*1 + 0; 1 = 2*9 - 17 = 2*60 - 7*17; [17]^{-1} = [-7] = [53]; 17*53 = 901 = 15*60 + 1;
gcd(12, 60) = 12; [12][5] = [0], [5] != [0]."""
from math import gcd
QUOTED = {"steps": [(60, 3, 17, 9), (17, 1, 9, 8), (9, 1, 8, 1), (8, 8, 1, 0)],
          "bezout": (2, -7), "inv": (-7, 53), "check": (901, 15), "gcd12": 12}
for a, q, b, r in QUOTED["steps"]:
    assert a == q * b + r and 0 <= r < b and divmod(a, b) == (q, r)
assert 2 * 9 - 17 == 1
c60, c17 = QUOTED["bezout"]
assert c60 * 60 + c17 * 17 == 1
assert QUOTED["inv"][0] == c17 and QUOTED["inv"][0] % 60 == QUOTED["inv"][1]
assert 17 * 53 == QUOTED["check"][0] == QUOTED["check"][1] * 60 + 1
assert gcd(12, 60) == QUOTED["gcd12"] and 12 * 5 % 60 == 0 and 5 % 60 != 0
print("ok")
