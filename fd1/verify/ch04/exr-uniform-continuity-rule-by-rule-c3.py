"""exr-uniform-continuity-rule-by-rule-c3 (b): D = {a, b}, P = D, R = identity; the premise
forall y exists x (P(x) and R(x, y)) is true and exists x (P(x) and forall y R(x, y)) is false.
Also (a)'s sequent holds in every structure with at most three elements (sanity)."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, P, ALL, EX, AND, all_relations, all_subsets

QUOTED = {"domain size": 2}
prem = ALL("y", EX("x", AND(P("P", "x"), P("R", "x", "y"))))
concl = EX("x", AND(P("P", "x"), ALL("y", P("R", "x", "y"))))
M = structure(["a", "b"], pred={"P": {("a",), ("b",)}, "R": {("a", "a"), ("b", "b")}})
assert len(M["D"]) == QUOTED["domain size"]
assert sat(prem, M, {}) and not sat(concl, M, {})
for n in (1, 2, 3):
    D = list(range(n))
    for R in all_relations(D, 2):
        for Pp in all_subsets(D):
            N = structure(D, pred={"P": Pp, "R": R})
            if sat(concl, N, {}):
                assert sat(prem, N, {})
print("exr-uniform-continuity-rule-by-rule-c3: all quoted values check")
