"""exr-existential-elimination-b1 (Ch 4, Section 4.6): the reading over Z (P positive,
Q negative), and the entailment in every small structure."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_subsets, P, ALL, EX, NOT, AND

QUOTED = {"lines": 10}

prem = [ALL("x", NOT(AND(P("P", "x"), P("Q", "x")))), EX("x", P("P", "x"))]
concl = EX("x", NOT(P("Q", "x")))
for n in (1, 2, 3):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            M = structure(D, pred={"P": Ps, "Q": Qs})
            assert (not all(sat(p, M, {}) for p in prem)) or sat(concl, M, {})
W = range(-100, 101)
assert not any(d > 0 and d < 0 for d in W) and any(d > 0 for d in W)
assert any(not (d < 0) for d in W if d > 0)
print("exr-existential-elimination-b1: all quoted values check")
