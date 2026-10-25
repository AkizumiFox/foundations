"""exr-counter-models-b4 (Section 7.2): the counter-models of (a), (b), (c); in (d) the sequent
has no counter-model (structures up to 3 elements, all assignments), and the step pattern
P(x0) |/= forall x P(x) is refuted in Z with P even, l(x0) = 2."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, is_counter_model, all_subsets, P, ALL, EX, AND, IMP
Px = P("P", "x")
# (a)
assert not sat(ALL("y", IMP(P("P", "y"), ALL("x", Px))), structure("ab", pred={"P": {("a",)}}), {})
# (b) any two-element domain
M2 = structure("ab")
assert is_counter_model([ALL("y", ("eq", "y", "y"))], EX("x", ALL("y", ("eq", "x", "y"))), M2)
# (c) with l(x0) = b
Mc = structure("ab", pred={"P": {("a",)}, "Q": {("a",)}})
assert is_counter_model([EX("x", Px), ALL("x", IMP(Px, P("Q", "x")))], P("Q", "x0"), Mc, {"x0": "b"})
# (d) the sequent holds on all small structures
for n in (1, 2, 3):
    for Ps in all_subsets(range(n)):
        M = structure(range(n), pred={"P": Ps})
        for d in range(n):
            assert not is_counter_model([AND(P("P", "x0"), ALL("x", Px))], ALL("x", Px), M, {"x0": d})
assert 2 % 2 == 0 and 1 % 2 == 1
print("exr-counter-models-b4: all quoted values check")
