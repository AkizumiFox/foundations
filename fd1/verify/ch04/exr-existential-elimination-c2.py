"""exr-existential-elimination-c2 (Ch 4, Section 4.6): the conclusion follows (no small
counter-model), while the illegal step's consequence exists x P(x) |- forall x P(x) fails over
Z with P even."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_subsets, P, EX, AND

QUOTED = {"illegal line": 4}

prem = EX("x", AND(P("P", "x"), P("Q", "x")))
concl = EX("x", P("P", "x"))
for n in (1, 2, 3):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            M = structure(D, pred={"P": Ps, "Q": Qs})
            assert (not sat(prem, M, {})) or sat(concl, M, {})
W = range(-100, 101)
assert any(d % 2 == 0 for d in W) and not all(d % 2 == 0 for d in W)
print("exr-existential-elimination-c2: all quoted values check")
