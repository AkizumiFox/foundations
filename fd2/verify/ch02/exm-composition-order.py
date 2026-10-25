"""exm-composition-order and the quick check after prp-composition-associative (Ch 6 Section 6.4)."""
from fractions import Fraction as F

QUOTED = {"(g o f)(0)": 2, "(f o g)(0)": 1, "check at 2": (1, 1), "check at 0": (-3, 9)}

f = lambda x: x + 1
g = lambda x: 2 * x
assert g(f(0)) == QUOTED["(g o f)(0)"] and f(g(0)) == QUOTED["(f o g)(0)"]
assert all(g(f(x)) == 2 * x + 2 and f(g(x)) == 2 * x + 1 for x in [F(k, 3) for k in range(-30, 31)])
# quick check: f(x) = x^2, g(x) = x - 3
f2 = lambda x: x * x
g2 = lambda x: x - 3
assert (g2(f2(2)), f2(g2(2))) == QUOTED["check at 2"]
assert (g2(f2(0)), f2(g2(0))) == QUOTED["check at 0"]
print("exm-composition-order: all quoted values check")
