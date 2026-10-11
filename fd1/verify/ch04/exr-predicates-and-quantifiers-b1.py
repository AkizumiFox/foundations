"""exr-predicates-and-quantifiers-b1 (Ch 4, Section 4.1): four ordered-quantifier sentences."""
from fractions import Fraction as Fr

QUOTED = {"(b) the forced y": -1, "(c) witness": 1, "(d) counterexample": -1}

N = range(0, 200)
R = sorted({Fr(p, q) for p in range(-30, 31) for q in range(1, 7)})
# (a) y = x + 1
assert all(x < x + 1 for x in N)
# (b) x = 2: 2 + y = 1 forces y = -1, not in N; 2 + y >= 2 for y in N; x = 0, 1 have witnesses 1, 0
assert all(2 + y >= 2 for y in N) and 1 - 2 == -1 and -1 not in N
assert 0 + 1 == 1 and 1 + 0 == 1 and 0 in N and 1 in N
# (c) x = 1 works for every y
assert all(1 * y == y for y in R)
# (d) y*y >= 0 > -1
assert all(y * y >= 0 for y in R) and 0 > -1
print("exr-predicates-and-quantifiers-b1: all quoted values check")
