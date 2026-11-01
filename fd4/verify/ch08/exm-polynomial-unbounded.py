"""exm-polynomial-unbounded: the example x^3 - 4x + 1, the choice x = R + 2|M|/|a_d|, Quick check 5."""
from fractions import Fraction as Fr

QUOTED = {"K": 5, "R": 10, "qc5_bound": 10000, "qc5_parts": (8000, 2000)}

def ev(c, x):  # coefficients lowest degree first
    return sum(Fr(a) * Fr(x)**j for j, a in enumerate(c))

def KR(c):
    d = len(c) - 1
    K = sum(abs(Fr(a)) for a in c[:-1])
    return K, max(Fr(1), 2 * K / abs(Fr(c[-1])))

c = [1, -4, 0, 1]
K, R = KR(c)
assert (K, R) == (QUOTED["K"], QUOTED["R"])

for c in [[1, -4, 0, 1], [3, 0, -7, 2, -1], [-5, 2], [1, 0, 1], [0, 0, 0, -3, 0, 1]]:
    K, R = KR(c); ad = abs(Fr(c[-1]))
    for t in [R, R + Fr(1, 3), R + 5, -R, -R - Fr(2, 7), -R - 40]:
        assert abs(ev(c, t)) >= ad * abs(t) / 2                 # part (a) on samples
        assert ev(c, t) != 0                                     # part (b)
    for M in [-10, 0, Fr(1, 2), 7, 1000, 10**6]:
        x = R + 2 * abs(Fr(M)) / ad
        assert x >= R > 0
        assert abs(ev(c, x)) >= ad * x / 2 == ad * R / 2 + abs(Fr(M)) > abs(Fr(M)) >= M

# Quick check 5
assert 20**3 == QUOTED["qc5_parts"][0] and 100 * 20 == QUOTED["qc5_parts"][1]
assert sum(QUOTED["qc5_parts"]) == QUOTED["qc5_bound"]
assert max(abs(Fr(k, 10)**3 - 100 * Fr(k, 10)) for k in range(-200, 201)) <= QUOTED["qc5_bound"]
print("ok")
