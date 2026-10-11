"""prp-exists-forall-swap (Ch 4, Section 4.6): the entailment holds in every structure with at
most 3 elements; the converse attempts must stall, since the converse fails (e.g. Z with <,
window check, and a two-element structure; Section 4.11 gives the proof)."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_relations, is_counter_model, P, ALL, EX

QUOTED = {"lines": 6}

prem = EX("x", ALL("y", P("R", "x", "y")))
concl = ALL("y", EX("x", P("R", "x", "y")))
for n in (1, 2, 3):
    D = list(range(n))
    for R in all_relations(D, 2):
        M = structure(D, pred={"R": R})
        assert (not sat(prem, M, {})) or sat(concl, M, {})
M2 = structure([0, 1], pred={"R": {(0, 0), (1, 1)}})
assert is_counter_model([concl], prem, M2)
W = range(-50, 51)
assert all(any(x < y for x in [y - 1]) for y in W)        # every integer has a smaller one
assert not any(all(x < y for y in [x]) for x in W)        # no x is below every y (y = x)
print("prp-exists-forall-swap: all quoted values check")
