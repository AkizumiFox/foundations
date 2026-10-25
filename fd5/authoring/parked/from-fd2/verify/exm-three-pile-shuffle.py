"""exm-three-pile-shuffle (and the hook, def-permutation table, A1 (c)): twelve cards, three piles of four."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits, power, least_identity_power

QUOTED = {
    "new_row": [0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11],
    "bottom_row": [0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8, 11],
    "orbit1": [1, 3, 9, 5, 4],
    "orbit2": [2, 6, 7, 10, 8],
    "fixed": [0, 11],
    "lengths": [1, 1, 5, 5],
    "N": 5,
    "3^5": (243, 22, 1),
}

# simulate the deal: piles of four, take card r of each pile in turn
piles = [list(range(4 * p, 4 * p + 4)) for p in range(3)]
new_row = [piles[p][r] for r in range(4) for p in range(3)]
assert new_row == QUOTED["new_row"]
sigma = {old: new for new, old in enumerate(new_row)}

def formula(i):
    return 3 * i if i <= 3 else (3 * i - 11 if i <= 7 else 3 * i - 22)

for i in range(12):
    p, r = divmod(i, 4)
    assert sigma[i] == formula(i) == 3 * r + p
    assert (3 * i - sigma[i]) == 11 * p
    if i <= 10:
        assert sigma[i] == (3 * i) % 11
    # inverse 3r + p -> 4p + r
    r2, p2 = divmod(sigma[i], 3)
    assert 4 * p2 + r2 == i
assert sigma[11] == 11
assert [sigma[i] for i in range(12)] == QUOTED["bottom_row"]
assert formula(2) == 6 and formula(5) == 4 and formula(10) == 8
assert sorted(sigma.values()) == list(range(12))

orbs = orbits(sigma, range(12))
assert QUOTED["orbit1"] in orbs and QUOTED["orbit2"] in orbs
assert sorted(len(o) for o in orbs) == QUOTED["lengths"]
assert [x for x in range(12) if sigma[x] == x] == QUOTED["fixed"]
assert least_identity_power(sigma) == QUOTED["N"]
assert all(power(sigma, n)[1] != 1 for n in range(1, 5))
a, q, r = QUOTED["3^5"]
assert 3 ** 5 == a == q * 11 + r
print("exm-three-pile-shuffle: all quoted values check")
