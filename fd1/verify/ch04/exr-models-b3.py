"""exr-models-b3 (Section 4.11): D = {a, b}, P = {a}, Q = {b} is a counter-model to
forall x not Q(x) -> forall x not P(x) |= forall x (P(x) -> Q(x)); the forward sequent of
Section 4.4 B2 has no counter-model on up to 3 elements."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, is_counter_model, all_subsets, P, ALL, NOT, IMP

QUOTED = {}
Px, Qx = P("P", "x"), P("Q", "x")
left = IMP(ALL("x", NOT(Qx)), ALL("x", NOT(Px)))
right = ALL("x", IMP(Px, Qx))
M = structure(["a", "b"], pred={"P": {("a",)}, "Q": {("b",)}})
assert is_counter_model([left], right, M)
for n in range(1, 4):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            assert not is_counter_model([right], left, structure(D, pred={"P": Ps, "Q": Qs}))
print("exr-models-b3: all quoted values check")
