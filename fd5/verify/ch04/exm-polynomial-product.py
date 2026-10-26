"""exm-polynomial-product (Section 4.2): (3x^2 - x + 2)(x + 1) over Q, F_3 and Z/6Z."""
from fractions import Fraction

QUOTED = {
    "Q": [2, 1, 2, 3],          # constant term first: 3x^3 + 2x^2 + x + 2
    "Q_terms_1": (2, -1),
    "Q_terms_2": (0, -1, 3),
    "F3_p": [2, 2, 0],          # 3x^2 - x + 2 read in F_3
    "F3": [2, 1, 2],            # 2x^2 + x + 2
    "F3_pos1": 4,               # 2 + 2 = 4 = 1
    "Z6_p": [2, 5, 3],
    "Z6_sums": (7, 8),          # [2] + [5] = [7] = [1], [5] + [3] = [8] = [2]
    "Z6": [2, 1, 2, 3],
}


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


p = [Fraction(2), Fraction(-1), Fraction(3)]
q = [Fraction(1), Fraction(1)]
pq = mul(p, q)
assert pq == QUOTED["Q"]
assert p[0] * q[1] + p[1] * q[0] == sum(QUOTED["Q_terms_1"])
assert 0 * q[0] + p[1] * q[1] + p[2] * q[0] == sum(QUOTED["Q_terms_2"])
p3 = [int(c) % 3 for c in p]
assert p3 == QUOTED["F3_p"]
r3 = [c % 3 for c in mul(p3, [1, 1])]
assert r3[:3] == QUOTED["F3"] and r3[3] == 0
assert 2 + 2 == QUOTED["F3_pos1"] and 4 % 3 == 1
p6 = [int(c) % 6 for c in p]
assert p6 == QUOTED["Z6_p"]
raw6 = mul(p6, [1, 1])
assert (raw6[1], raw6[2]) == QUOTED["Z6_sums"]
assert [c % 6 for c in raw6] == QUOTED["Z6"]
# each answer is the rational answer with integer coefficients reduced
assert [int(c) % 3 for c in pq] == r3 and [int(c) % 6 for c in pq] == [c % 6 for c in raw6]
print("exm-polynomial-product: ok")
