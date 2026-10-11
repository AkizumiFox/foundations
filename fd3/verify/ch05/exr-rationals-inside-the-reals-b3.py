"""exr-rationals-inside-the-reals-b3: counterexample to line (viii):
a = (5, 0, 0, ...), n = 1, k = 0 gives |a_m - a_0| = 5 >= 1/(2n) for every m >= 1,
so no N_0 exists; a is Cauchy (constant from index 1 on)."""
from fractions import Fraction as F
QUOTED = {"a0": 5, "n": 1, "gap": 5}
def a(m):
    return F(QUOTED["a0"]) if m == 0 else F(0)
n = QUOTED["n"]
assert all(abs(a(m) - a(0)) == QUOTED["gap"] for m in range(1, 200))
assert QUOTED["gap"] >= F(1, 2 * n)
# Cauchy: |a_m - a_k| = 0 < 1/(2n) for all m, k >= 1
assert all(abs(a(m) - a(k)) < F(1, 2 * n) for m in range(1, 50) for k in range(1, 50))
print("ok")
