"""thm-subgroups-of-integers: the try-it-first (15 - 6 = 9, 9 - 6 = 3; the smallest subgroup
containing 6 and 15 is 3Z, checked on a window as 6Z + 15Z) and the Quick check
6Z cap 15Z = 30Z (30 = 5*6 = 2*15; 15 = 2*6 + 3). Also a brute-force check that the
subgroups of Z/NZ-windows behave: least positive element divides every element."""
from math import gcd
QUOTED = {"try": (9, 3), "gen": 3, "check": 30, "arith": [(30, 5, 6), (30, 2, 15)], "div": (15, 2, 3)}
assert 15 - 6 == QUOTED["try"][0] and 9 - 6 == QUOTED["try"][1]
W = range(-60, 61)
comb = {6 * x + 15 * y for x in W for y in W}
assert min(c for c in comb if c > 0) == QUOTED["gen"] == gcd(6, 15)
assert all(c % 3 == 0 for c in comb) and all(k in comb for k in range(-90, 91, 3))
inter = [c for c in range(1, 500) if c % 6 == 0 and c % 15 == 0]
assert inter[0] == QUOTED["check"] and all(c % 30 == 0 for c in inter)
for v, a, b in QUOTED["arith"]:
    assert v == a * b
x, q, r = QUOTED["div"]
assert x == q * 6 + r and r != 0
assert [15 * k for k in range(1, 3) if 15 * k < 30] == [15]
print("thm-subgroups-of-integers: ok")
