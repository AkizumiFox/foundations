"""exr-counter-models-b2 (Section 7.2): every verdict by brute force over all structures on up to
3 elements (P, Q one-place; R two-place, up to 2 elements for the parts with R and up to 3 for the
others), and every counter-model as stated."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import (structure, sat, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, OR, IMP)
Px, Qx, Qy = P("P", "x"), P("Q", "x"), P("Q", "y")
parts = {
 "a": ([ALL("x", IMP(Px, Qx)), ALL("x", NOT(Qx))], ALL("x", NOT(Px)), True),
 "b": ([ALL("x", IMP(Px, Qx)), EX("x", NOT(Px))], EX("x", NOT(Qx)), False),
 "c": ([EX("x", ALL("y", P("R", "x", "y")))], EX("x", P("R", "x", "x")), True),
 "d": ([ALL("x", EX("y", P("R", "x", "y")))], ALL("x", EX("y", P("R", "y", "x"))), False),
 "e": ([ALL("x", IMP(Px, EX("y", Qy)))], IMP(EX("x", Px), EX("y", Qy)), True),
 "f": ([IMP(EX("x", Px), ALL("y", Qy))], ALL("x", IMP(Px, Qx)), True),
 "g": ([ALL("x", OR(Px, Qx)), EX("x", NOT(Px))], ALL("x", Qx), False),
 "h": ([ALL("x", OR(Px, Qx)), ALL("x", NOT(Px))], ALL("x", Qx), True),
}
def structures(n):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            for R in all_relations(D, 2):
                yield structure(D, pred={"P": Ps, "Q": Qs, "R": R})
for n in (1, 2, 3):
    for M in structures(n):
        for k, (G, phi, holds) in parts.items():
            if holds:
                assert not is_counter_model(G, phi, M), k
# the stated counter-models
assert is_counter_model(*parts["b"][:2], structure(["a"], pred={"P": set(), "Q": {("a",)}}))
assert is_counter_model(*parts["d"][:2], structure("ab", pred={"R": {("a", "b"), ("b", "b")}}))
assert is_counter_model(*parts["g"][:2], structure("ab", pred={"P": {("a",)}, "Q": {("b",)}}))
print("exr-counter-models-b2: all quoted values check")
