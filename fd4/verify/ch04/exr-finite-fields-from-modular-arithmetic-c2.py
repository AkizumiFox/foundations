"""exr-finite-fields-from-modular-arithmetic-c2: the step "[a]^{-1} = [1/a]" names a class of
integers only for a = 1, -1; counterexample p = 5, a = 2: 1/2 is not an integer, and the inverse
of [2] in Z/5Z is [3]; the repair 2x + 5y = 1 (x = 3, y = -1) gives [2][3] = [1]; the same lines
would "prove" Z/6Z a field, but [2] has no inverse there."""
from fractions import Fraction

QUOTED = {"p": 5, "a": 2, "inverse of [2]": 3, "Z/6Z": 6, "1/a an integer only for a =": (1, -1)}

p, a = QUOTED["p"], QUOTED["a"]
assert all(p % d for d in range(2, p))                       # 5 is prime
assert Fraction(1, a).denominator != 1                         # 1/2 is not an integer
assert {t for t in range(-20, 21) if t and Fraction(1, t).denominator == 1} \
    == set(QUOTED["1/a an integer only for a ="])
assert [x for x in range(p) if a * x % p == 1] == [QUOTED["inverse of [2]"]]
x, y = QUOTED["inverse of [2]"], -1                            # Bezout repair: ax + py = 1
assert a * x + p * y == 1 and (a * x - 1) % p == 0
n = QUOTED["Z/6Z"]
assert [x for x in range(n) if a * x % n == 1] == []           # [2] has no inverse in Z/6Z
for q in (2, 3, 5, 7, 11, 13):                                 # the claim itself: Z/qZ is a field
    assert all(any(b * x % q == 1 for x in range(q)) for b in range(1, q))
print("ok")
