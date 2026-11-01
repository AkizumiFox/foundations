"""prp-thomae-large-values and its Quick check, def-thomae-function values, exr-strange-functions-b1,
exr-strange-functions-a1 (T on [0, 1]): Thomae's function on rationals, exact arithmetic."""
from fractions import Fraction as Fr
from math import floor, gcd

QUOTED = {
    "T(3/4)": Fr(1, 4),
    "T(-6/8)": Fr(1, 4),
    "T(0.6)": Fr(1, 5),
    "T(0)": Fr(1),
    "T(1)": Fr(1),
    "T(2/4)": Fr(1, 2),
    "B1 points": [Fr(0), Fr(1), Fr(1, 2), Fr(1, 3), Fr(2, 3), Fr(1, 4), Fr(3, 4)],
}

def T(x: Fr) -> Fr:
    # Fraction keeps lowest terms with positive denominator
    return Fr(1, x.denominator)

assert T(Fr(3, 4)) == QUOTED["T(3/4)"]
assert T(Fr(-6, 8)) == QUOTED["T(-6/8)"]
assert T(Fr("0.6")) == QUOTED["T(0.6)"]
assert T(Fr(0)) == QUOTED["T(0)"] and T(Fr(1)) == QUOTED["T(1)"]
assert T(Fr(2, 4)) == QUOTED["T(2/4)"]

# B1: all x in [0,1] with T(x) >= 1/4, by brute force over denominators up to 40
pts = {Fr(p, q) for q in range(1, 41) for p in range(0, q + 1) if T(Fr(p, q)) >= Fr(1, 4)}
assert pts == set(QUOTED["B1 points"]) and len(pts) == 7

# figure: points of [0,1] with denominator <= 6 in lowest terms
dots = {Fr(p, q) for q in range(1, 7) for p in range(0, q + 1)}
assert len(dots) == 13

# (a) period 1 on many rationals
for q in range(1, 30):
    for p in range(-60, 60):
        x = Fr(p, q)
        assert T(x + 1) == T(x)
        if gcd(p, q) == 1:
            assert gcd(p + q, q) == 1

# (b) covering by S_q, q <= floor(1/eps), S_q = {p/q : floor(aq) <= p <= floor(bq)}
for (a, b) in [(Fr(-3, 2), Fr(7, 3)), (Fr(0), Fr(1)), (Fr(5, 7), Fr(5, 7)), (Fr(-1, 3), Fr(2, 9))]:
    for eps in [Fr(1, 4), Fr(1, 7), Fr(2, 9), Fr(3, 2), Fr(1)]:
        Q = floor(1 / eps)
        E = {Fr(p, q) for q in range(1, 60) for p in range(floor(a * q) - 1, floor(b * q) + 2)
             if a <= Fr(p, q) <= b and T(Fr(p, q)) >= eps}
        U = {Fr(p, q) for q in range(1, Q + 1) for p in range(floor(a * q), floor(b * q) + 1)}
        assert E <= U, (a, b, eps)
        if eps > 1:
            assert not E
print("prp-thomae-large-values: all checks passed")
