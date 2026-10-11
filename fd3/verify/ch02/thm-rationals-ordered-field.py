"""thm-rationals-ordered-field (with def-rational-order, prp-reciprocal-order and the midpoint
check of Section 10.5): the positive test is independent of representatives (positive
denominators), the comparison formula, the failure with negative denominators, the warning
1/2 > 2/5, the midpoint 5/12 of 1/3 and 1/2. Exact arithmetic on pairs of integers."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"warning_diff": F(1, 10), "midpoint": F(5, 12), "mid_lhs": (12, 15), "mid_rhs": (10, 12)}

R = range(-6, 7)
Q = range(1, 7)
pairs = [(p, q) for p in R for q in Q]
eq = lambda a, b: a[0] * b[1] == b[0] * a[1]
# positive test well defined on Z x Z_{>0}
for a, b in product(pairs, pairs):
    if eq(a, b):
        assert (a[0] > 0) == (b[0] > 0)
# comparison formula: p/q < r/s iff ps < rq ; sum/product closure
for (p, q), (r, s) in product(pairs, pairs):
    assert (F(p, q) < F(r, s)) == (p * s < r * q)
    assert (F(p, q) <= F(r, s)) == (p * s <= r * q)
    if p > 0 and r > 0:
        assert p * s + r * q > 0 and p * r > 0
    # difference representative [(rq - ps, qs)]
    assert F(r, s) - F(p, q) == F(r * q - p * s, q * s)
# with negative denominators the test fails: (1,1) ~ (-1,-1)
assert 1 * -1 == -1 * 1 and (1 > 0) != (-1 > 0)
# warning: numerators alone mislead
assert 1 < 2 and F(1, 2) > F(2, 5) and F(1, 2) - F(2, 5) == QUOTED["warning_diff"]
# midpoint check
m = (F(1, 3) + F(1, 2)) / 2
assert m == QUOTED["midpoint"] and F(1, 3) + F(1, 2) == F(5, 6)
assert (1 * 12, 5 * 3) == QUOTED["mid_lhs"] and 12 < 15
assert (5 * 2, 1 * 12) == QUOTED["mid_rhs"] and 10 < 12
# reciprocals reverse order on positives (prp-reciprocal-order)
vals = sorted({F(p, q) for p in range(1, 9) for q in Q})
for a, b in product(vals, vals):
    if a < b:
        assert 0 < 1 / b < 1 / a
print("ok")
