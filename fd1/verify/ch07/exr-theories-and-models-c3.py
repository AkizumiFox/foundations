"""exr-theories-and-models-c3 (Section 7.4 exit check): (N, <) and the non-negative rationals
are models of T (windows); (Dense) fails in N at 0 < 1 and holds in the rationals via
(p + q)/2; the TAUT skeleton A v B, C v D, not E, (B & D) -> E, C -> A |= A by truth table.
(The derivation is checked by tools/check_fitch.py.)"""
import itertools
from fractions import Fraction as F


def strict_linear_least(D):
    irr = all(not x < x for x in D)
    tr = all(x < z for x in D for y in D for z in D if x < y and y < z)
    tri = all(x < y or x == y or y < x for x in D for y in D)
    least = any(all(x == y or x < y for y in D) for x in D)
    return irr and tr and tri and least


N = list(range(15))
Qp = sorted({F(p, q) for p in range(0, 13) for q in range(1, 5)})
assert strict_linear_least(N) and strict_linear_least(Qp)
assert min(Qp) == 0
assert not any(0 < k < 1 for k in N)
assert all(p < (p + q) / 2 < q and (p + q) / 2 >= 0 for p in Qp for q in Qp if p < q)
for A, B, C, D, E in itertools.product([False, True], repeat=5):
    prem = (A or B) and (C or D) and (not E) and ((not (B and D)) or E) and ((not C) or A)
    assert (not prem) or A
print("exr-theories-and-models-c3: all quoted values check")
