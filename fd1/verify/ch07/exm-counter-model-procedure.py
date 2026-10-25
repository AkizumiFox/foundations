"""exm-counter-model-procedure (Section 7.2): the negated conclusion pushed inward is equivalent
to it (all structures on up to 2 elements); y = a clashes; the structure D = {a, b}, P = {a},
R = {(a, b)} is a counter-model; the N reading (P even, R(x, y) as y = 2x + 1) for x in 0..50."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import (structure, sat, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, IMP)

prem1 = ALL("x", IMP(P("P", "x"), EX("y", P("R", "x", "y"))))
prem2 = EX("x", P("P", "x"))
concl = EX("x", EX("y", AND(P("R", "x", "y"), P("P", "y"))))
pushed = ALL("x", ALL("y", IMP(P("R", "x", "y"), NOT(P("P", "y")))))

# step 1: the pushed-in form is equivalent to the negated conclusion
for n in (1, 2):
    D = list(range(n))
    for Ps in all_subsets(D):
        for R in all_relations(D, 2):
            M = structure(D, pred={"P": Ps, "R": R})
            assert sat(NOT(concl), M, {}) == sat(pushed, M, {})

# the clash at y = a: R(a, a) with P(a) breaks the pushed-in member
Ma = structure(["a"], pred={"P": {("a",)}, "R": {("a", "a")}})
assert not sat(pushed, Ma, {})
# no one-element counter-model at all
for Ps in all_subsets(["a"]):
    for R in all_relations(["a"], 2):
        assert not is_counter_model([prem1, prem2], concl, structure(["a"], pred={"P": Ps, "R": R}))

# the structure found
M = structure(["a", "b"], pred={"P": {("a",)}, "R": {("a", "b")}})
assert is_counter_model([prem1, prem2], concl, M)

# the N reading: P even, R(x, y) iff y = 2x + 1
X = range(0, 51)
even = lambda d: d % 2 == 0
assert all(not even(2 * x + 1) for x in X)        # every R-image is odd
assert any(even(x) for x in X)                     # some number is even
assert all(2 * x + 1 in range(0, 102) for x in X)  # every x, even ones included, has 2x + 1 in N
print("exm-counter-model-procedure: all quoted values check")
