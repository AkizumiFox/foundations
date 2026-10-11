"""prp-coprime-divisors-product: the aftermath; also cor-prime-divides-product's 6 | 2*3 example."""
from math import gcd

QUOTED = {"m": 4, "n": 6, "c": 12, "mn": 24, "gcd": 2}
assert QUOTED["c"] % QUOTED["m"] == 0 and QUOTED["c"] % QUOTED["n"] == 0
assert QUOTED["m"] * QUOTED["n"] == QUOTED["mn"] and QUOTED["c"] % QUOTED["mn"] != 0
assert QUOTED["mn"] > QUOTED["c"] > 0
assert gcd(QUOTED["m"], QUOTED["n"]) == QUOTED["gcd"]
# cor-prime-divides-product aftermath: 6 | 2*3, 6 does not divide 2 or 3
assert (2 * 3) % 6 == 0 and 2 % 6 != 0 and 3 % 6 != 0 and 0 < 2 < 6 and 0 < 3 < 6
# the proposition on a grid
for m in range(-10, 11):
    for n in range(-10, 11):
        if gcd(m, n) != 1:
            continue
        for c in range(-60, 61):
            ok_m = (c == 0) if m == 0 else c % m == 0
            ok_n = (c == 0) if n == 0 else c % n == 0
            if ok_m and ok_n:
                assert (c == 0) if m * n == 0 else c % (m * n) == 0
print("prp-coprime-divisors-product: ok")
