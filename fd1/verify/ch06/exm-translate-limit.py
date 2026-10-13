"""exm-translate-limit (Ch 4, Section 4.8): the warning's constants and the Quick check on (0, 1)."""
from fractions import Fraction as Fr

QUOTED = {"warning (3): N for a_n = n - 3": 4, "warning (3): a_0": -3,
          "warning (2): bound of f(x) = x on [0, 1]": 1, "check: m bounding (0, 1)": 1}

a = lambda n: n - 3
assert all(a(n) > 0 for n in range(4, 200))       # N = 4 works
assert a(0) == -3 and not a(0) > 0                # so not every n
# f(x) = x is bounded by 1 on [0, 1]; the bound fails off [0, 1] (x = 2)
assert all(abs(Fr(k, 100)) <= 1 for k in range(0, 101))
assert abs(Fr(2)) > 1
# (0, 1): bounded above by m = 1, which is not in (0, 1); no element is a maximum
A = [Fr(p, q) for q in range(2, 30) for p in range(1, q)]
assert all(x <= 1 for x in A) and not (0 < 1 < 1)
assert all(m < (m + 1) / 2 < 1 for m in A)
print("exm-translate-limit: all quoted values check")
