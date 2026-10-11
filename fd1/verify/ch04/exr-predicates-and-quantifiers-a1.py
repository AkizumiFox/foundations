"""exr-predicates-and-quantifiers-a1 (Ch 4, Section 4.1): truth over N, Z, R of five sentences."""
from fractions import Fraction
Fr = Fraction

QUOTED = {"witness in (ii)": -1, "witness in (iv) and counterexample in (v)": Fraction(1, 2),
          "(1/2)^2": Fraction(1, 4)}

N = range(0, 60)
Z = range(-60, 60)
# a finite sample of R (rationals), enough for the witnesses and counterexamples quoted
R = sorted({Fr(p, q) for p in range(-40, 41) for q in range(1, 9)})

# (i) x + 1 > x holds everywhere
assert all(x + 1 > x for x in list(Z) + R)
# (ii) x + 1 = 0: only -1
assert not any(x + 1 == 0 for x in N) and -1 in Z and Fr(-1) in R
# (iii) forall x exists y (y < x): fails at x = 0 in N; y = x - 1 in Z and R
assert not any(y < 0 for y in N)
assert all((x - 1) < x for x in list(Z) + R)
# (iv) 2x = 1 only at 1/2
assert not any(2 * x == 1 for x in Z) and 2 * Fr(1, 2) == 1
# (v) x*x >= x on N and Z, fails at 1/2 in R
assert all(x * x >= x for x in Z) and all(x * x >= x for x in N) and 0 * 0 == 0
assert Fr(1, 2) ** 2 == Fr(1, 4) and Fr(1, 4) < Fr(1, 2)
print("exr-predicates-and-quantifiers-a1: all quoted values check")
