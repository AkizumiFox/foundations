"""exr-universal-introduction-c2 (Ch 4, Section 4.4): the student's checks, and the
polynomial x(x - 1)(x - 2) that passes them and fails at -1."""
from fractions import Fraction as Fr

q = lambda x: x * x - 2 * x + 1
p = lambda x: x * (x - 1) * (x - 2)
QUOTED = {"q(0)": 1, "q(1)": 0, "q(2)": 1, "p(0)": 0, "p(1)": 0, "p(2)": 0, "p(-1)": -6}
for k in (0, 1, 2):
    assert q(k) == QUOTED[f"q({k})"]
    assert p(k) == QUOTED[f"p({k})"]
assert p(-1) == QUOTED["p(-1)"] < 0
# the claim is true: q(x) = (x - 1)^2 (degree 2, checked at many exact points)
assert all(q(t) == (t - 1) ** 2 >= 0 for t in [Fr(k, 9) for k in range(-90, 90)])
# the three displayed computations: 0 - 0 + 1, 1 - 2 + 1, 4 - 4 + 1, and (-1)(-2)(-3)
assert (0 - 0 + 1, 1 - 2 + 1, 4 - 4 + 1) == (1, 0, 1)
assert (-1) * (-2) * (-3) == -6
print("exr-universal-introduction-c2: all quoted values check")
