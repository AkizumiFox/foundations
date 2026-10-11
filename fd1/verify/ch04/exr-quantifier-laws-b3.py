"""exr-quantifier-laws-b3 (Section 4.9): with a > b and eps = min(1, a - b), eps > 0,
eps^2 <= eps <= a - b, so the hypothesis a < b + eps^2 would give a < a; the copied choice
eps = a - b gives a - b < (a - b)^2, true when a - b > 1 (example a - b = 2: 2 < 4)."""
from fractions import Fraction as F

QUOTED = {"example a - b": 2, "its square": 4}
for a, b in [(F(3), F(1)), (F(1, 2), F(1, 3)), (F(10), F(-5)), (F(7, 5), F(1)), (F(2), F(1))]:
    assert a > b
    eps = min(F(1), a - b)
    assert eps > 0 and eps * eps <= eps <= a - b
    assert not (a < b + eps * eps)          # the hypothesis fails at this eps
d = F(QUOTED["example a - b"])
assert d * d == QUOTED["its square"] and d < d * d
for d in [F(3, 2), F(2), F(5)]:
    assert d < d * d                        # no contradiction from eps = a - b when a - b > 1
print("exr-quantifier-laws-b3: all quoted values check")
