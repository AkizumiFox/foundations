"""exr-rationals-as-classes-c1 (Section 10.4): [(1, 2)] = [(2, 4)] with denominators 2, 4;
N(6/4) = 2 (4p = 6 has no integer solution; (3, 2) ~ (6, 4)); and N agrees with the
lowest-terms denominator on a window (computed independently with Fraction)."""
from fractions import Fraction
QUOTED = {"N_6_4": 2, "witness": (3, 2)}
assert 1 * 4 == 2 * 2
assert all(4 * p != 6 for p in range(-100, 101))
assert 4 * 3 == 6 * 2 and QUOTED["witness"] == (3, 2)
assert 4 * 1 == 4 < 6 < 8 == 4 * 2


def N(p, q, bound=60):
    return min(s for s in range(1, bound) for r in range(-bound * abs(p) - 1, bound * abs(p) + 2) if r * q == p * s)


assert N(6, 4) == QUOTED["N_6_4"] == Fraction(6, 4).denominator
for p in range(-6, 7):
    for q in range(1, 7):
        assert N(p, q) == Fraction(p, q).denominator
print("exr-rationals-as-classes-c1: all quoted values check")
