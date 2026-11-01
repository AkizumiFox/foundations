"""prp-rationals-lowest-terms: the example 252/198 = 14/11 and 6/4 = 3/2; a brute-force check of (b)."""
from fractions import Fraction
from math import gcd

QUOTED = {"r": 252, "s": 198, "d": 18, "p": 14, "q": 11, "six_fourths": (3, 2)}
assert gcd(QUOTED["r"], QUOTED["s"]) == QUOTED["d"]
assert QUOTED["r"] == QUOTED["d"] * QUOTED["p"] and QUOTED["s"] == QUOTED["d"] * QUOTED["q"]
assert gcd(QUOTED["p"], QUOTED["q"]) == 1
assert Fraction(252, 198) == Fraction(14, 11)
assert Fraction(6, 4) == Fraction(*QUOTED["six_fourths"]) == Fraction(9, 6)
for r in range(-40, 41):
    for s in range(1, 41):
        x = Fraction(r, s)
        p, q = x.numerator, x.denominator
        assert gcd(p, q) == 1 and s % q == 0
        t = s // q
        assert t > 0 and r == t * p
print("prp-rationals-lowest-terms: ok")
