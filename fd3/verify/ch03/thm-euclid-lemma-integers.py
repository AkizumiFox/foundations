"""thm-euclid-lemma-integers: the aftermath (dropping coprimality)."""
from math import gcd

QUOTED = {"a": 4, "b": 2, "c": 6, "bc": 12, "div_6_by_4": (1, 2), "gcd_4_2": 2}
a, b, c = QUOTED["a"], QUOTED["b"], QUOTED["c"]
assert b * c == QUOTED["bc"] and QUOTED["bc"] % a == 0
q, r = QUOTED["div_6_by_4"]
assert c == q * a + r and 0 < r < a  # non-zero remainder: 4 does not divide 6
assert c % a != 0
assert gcd(a, b) == QUOTED["gcd_4_2"]
# the lemma itself on a grid (sanity)
for a in range(-12, 13):
    for b in range(-12, 13):
        if gcd(a, b) != 1:
            continue
        for c in range(-12, 13):
            if a != 0 and (b * c) % a == 0:
                assert c % a == 0
print("thm-euclid-lemma-integers: ok")
