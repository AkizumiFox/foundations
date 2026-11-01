"""prp-zigzag-all-values, exm-strange-zigzag: Z(x) = dist(1/x, Z)."""
from fractions import Fraction as Fr
from math import floor

QUOTED = {
    "peak": Fr(1, 2),          # Z(2/(2n+1)) = 1/2
    "bound": Fr(1, 2),         # |x Z(x)| <= |x|/2
}

def dist(y: Fr) -> Fr:
    m = floor(y)
    return min(y - m, m + 1 - y)

def Z(x: Fr) -> Fr:
    return Fr(0) if x == 0 else dist(1 / x)

for n in range(1, 100):
    assert Z(Fr(1, n)) == 0 and Z(Fr(1, n + 1)) == 0
    assert Z(Fr(2, 2 * n + 1)) == QUOTED["peak"]
    for t in [Fr(0), Fr(1, 7), Fr(1, 3), Fr(49, 100), Fr(1, 2)]:
        x = 1 / (n + t)
        assert 0 < x <= Fr(1, n)
        assert Z(x) == t
    # min formula on [1/(n+1), 1/n]
    for k in range(0, 21):
        x = Fr(1, n + 1) + (Fr(1, n) - Fr(1, n + 1)) * Fr(k, 20)
        assert Z(x) == min(1 / x - n, n + 1 - 1 / x)

for q in range(1, 60):
    for p in range(-80, 80):
        x = Fr(p, q)
        assert abs(x * Z(x)) <= abs(x) * QUOTED["bound"]
print("prp-zigzag-all-values: all checks passed")
