"""exm-isomorphic-small-groups: (a) Z/2Z ~ {1,-1}; (b) [k] -> [2]^k, powers [1],[2],[4],[3],[1],
(Z/5Z)^x = {1,2,3,4} with [2][3] = [1], [4][4] = [1]; (c) (Z/8Z)^x = {1,3,5,7}, all squares [1],
even classes zero divisors [2][4] = [6][4] = [0], and no isomorphism Z/4Z -> (Z/8Z)^x exists
(checked over all bijections); (d) x -> 2x additive and injective on a range."""
from itertools import permutations
QUOTED = {"pow2": [1, 2, 4, 3, 1], "units5": [1, 2, 3, 4], "units8": [1, 3, 5, 7]}
# (a)
phi = {0: 1, 1: -1}
assert all(phi[(a + b) % 2] == phi[a] * phi[b] for a in range(2) for b in range(2))
# (b)
assert [pow(2, k, 5) for k in range(5)] == QUOTED["pow2"]
assert [x for x in range(5) if any(x * y % 5 == 1 for y in range(5))] == QUOTED["units5"]
assert 2 * 3 % 5 == 1 and 4 * 4 % 5 == 1
psi = {k: pow(2, k, 5) for k in range(4)}
assert sorted(psi.values()) == QUOTED["units5"]
assert all(psi[(a + b) % 4] == psi[a] * psi[b] % 5 for a in range(4) for b in range(4))
for k in range(0, 40):  # well defined: [2]^k depends only on k mod 4
    assert pow(2, k, 5) == pow(2, k % 4, 5)
# (c)
assert [x for x in range(8) if any(x * y % 8 == 1 for y in range(8))] == QUOTED["units8"]
assert all(x * x % 8 == 1 for x in QUOTED["units8"])
assert 2 * 4 % 8 == 0 and 6 * 4 % 8 == 0
found = False
for img in permutations(QUOTED["units8"]):
    f = dict(zip(range(4), img))
    if all(f[(a + b) % 4] == f[a] * f[b] % 8 for a in range(4) for b in range(4)):
        found = True
assert not found
# (d)
assert all(2 * (x + y) == 2 * x + 2 * y for x in range(-5, 6) for y in range(-5, 6))
assert len({2 * x for x in range(-50, 51)}) == 101
print("ok")
