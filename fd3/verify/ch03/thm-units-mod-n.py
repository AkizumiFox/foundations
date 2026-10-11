"""thm-units-mod-n: [a] unit in Z/nZ iff gcd(a, n) = 1, exhaustively for n <= 60, |a| <= 70;
and [x] is the inverse for every x with ax + ny = 1. Quick check: [3]^{-1} = [5] in Z/7Z,
15 = 2*7 + 1, 3*5 + 7*(-2) = 1."""
from math import gcd
QUOTED = {"inv3mod7": 5, "bezout": (5, -2)}
for n in range(1, 61):
    for a in range(-70, 71):
        unit = any((a * x - 1) % n == 0 for x in range(n))
        assert unit == (gcd(a, n) == 1), (a, n)
        for x in range(-20, 21):
            if (1 - a * x) % n == 0:  # ax + ny = 1 for y = (1 - ax)/n
                assert (a * x) % n == 1 % n
assert 3 * QUOTED["inv3mod7"] == 15 == 2 * 7 + 1
x, y = QUOTED["bezout"]
assert 3 * x + 7 * y == 1
print("ok")
