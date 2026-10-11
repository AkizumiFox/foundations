"""exr-disjunction-and-cases-b4 (Section 1.6): min(a, b) = -max(-a, -b), by cases a >= b or
a < b, the first split again on (-a < -b) or (-a = -b); the checks at (3, -5) and (2, 2)."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"check 1": (3, -5, -5, 5), "check 2": (2, 2, 2, -2)}

def mx(a, b):
    return a if a >= b else b

def mn(a, b):
    return b if a >= b else a

pts = [F(k, 4) for k in range(-40, 41)]
for a, b in product(pts, pts):
    assert mn(a, b) == -mx(-a, -b)
    if a < b:
        assert -a > -b and mx(-a, -b) == -a and mn(a, b) == a
    else:
        assert -a <= -b and (-a < -b or -a == -b)
        if -a < -b:
            assert mx(-a, -b) == -b and mn(a, b) == b
        else:
            assert mx(-a, -b) == -a and a == b == mn(a, b)
for a, b, m, M in QUOTED.values():
    assert mn(a, b) == m and mx(-a, -b) == M and -M == m
print("exr-disjunction-and-cases-b4: checks")
