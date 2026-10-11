"""prp-exists-and (Ch 4, Section 4.6): the entailment holds in every small structure, and the
Quick check's reading of the converse over Z (P even, Q odd) has true premise, false conclusion."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_subsets, P, EX, AND

QUOTED = {"lines": 8}

prem = EX("x", AND(P("P", "x"), P("Q", "x")))
concl = AND(EX("x", P("P", "x")), EX("x", P("Q", "x")))
for n in (1, 2, 3):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            M = structure(D, pred={"P": Ps, "Q": Qs})
            assert (not sat(prem, M, {})) or sat(concl, M, {})
W = range(-100, 101)
assert any(d % 2 == 0 for d in W) and any(d % 2 == 1 for d in W)
assert not any(d % 2 == 0 and d % 2 == 1 for d in W)
print("prp-exists-and: all quoted values check")
