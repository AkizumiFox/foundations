"""exr-universal-elimination-c1 (Ch 4, Section 4.3): on {0, 1} the relation {(0, 0)} is
symmetric and transitive, and (1, 1) is not in it."""
from itertools import product

QUOTED = {"domain": {0, 1}, "R": {(0, 0)}}
D, R = QUOTED["domain"], QUOTED["R"]
assert all(((x, y) not in R) or ((y, x) in R) for x, y in product(D, D))
assert all(not ((x, y) in R and (y, z) in R) or ((x, z) in R) for x, y, z in product(D, D, D))
assert (1, 1) not in R
# and the theorem itself: in every symmetric, transitive relation on a small set,
# R(a, b) gives R(a, a)
for bits in range(2 ** 9):
    S = {(i, j) for i in range(3) for j in range(3) if bits >> (3 * i + j) & 1}
    sym = all((j, i) in S for i, j in S)
    tr = all((i, k) in S for i, j in S for j2, k in S if j == j2)
    if sym and tr:
        assert all((i, i) in S for i, j in S)
print("exr-universal-elimination-c1: all quoted values check")
