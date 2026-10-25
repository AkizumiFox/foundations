"""exr-permutations-and-iteration-c1: fifteen cards in three piles of five (simulated deal)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits, least_identity_power

QUOTED = {"images": [[0, 3, 6, 9, 12], [1, 4, 7, 10, 13], [2, 5, 8, 11, 14]],
          "fixed": [0, 7, 14], "c1": [1, 3, 9, 13, 11, 5], "c2": [2, 6, 4, 12, 8, 10],
          "N": 6, "3^6": (729, 52, 1)}
piles = [list(range(5 * p, 5 * p + 5)) for p in range(3)]
new_row = [piles[p][r] for r in range(5) for p in range(3)]
sigma = {old: new for new, old in enumerate(new_row)}
def formula(i):
    return 3 * i if i <= 4 else (3 * i - 14 if i <= 9 else 3 * i - 28)
for i in range(15):
    p, r = divmod(i, 5)
    assert sigma[i] == formula(i) == 3 * r + p and 3 * i - sigma[i] == 14 * p
    if i <= 13:
        assert sigma[i] == (3 * i) % 14
for p in range(3):
    assert sorted(sigma[i] for i in range(5 * p, 5 * p + 5)) == QUOTED["images"][p]
assert sorted(sigma.values()) == list(range(15))
orbs = orbits(sigma, range(15))
assert [o[0] for o in orbs if len(o) == 1] == QUOTED["fixed"]
assert QUOTED["c1"] in orbs and QUOTED["c2"] in orbs and len(orbs) == 5
assert least_identity_power(sigma) == QUOTED["N"]
a, q, r = QUOTED["3^6"]
assert 3 ** 6 == a == q * 14 + r
for k in range(1, 8):  # sigma^k(i) = 3^k i mod 14
    for i in range(14):
        x = i
        for _ in range(k):
            x = sigma[x]
        assert x == (3 ** k * i) % 14
print("exr-permutations-and-iteration-c1: all quoted values check")
