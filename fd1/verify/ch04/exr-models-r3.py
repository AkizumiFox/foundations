"""exr-models-r3 (Section 4.11): the printed derivation has 18 lines, no RAA, and its sequent
has no counter-model on structures of up to 3 elements."""
import re
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, is_counter_model, all_subsets, P, ALL, EX, NOT, AND, IMP

QUOTED = {"lines": 18}
src = open("src/ch04-predicate-logic/11-models.md").read()
blk = src.split("{#exr-models-r3}")[1].split("{#exr-models-r4}")[0]
nd = blk.split(r"\begin{nd}")[1].split(r"\end{nd}")[0]
assert len(re.findall(r"\\(hypo|have)\s*\{", nd)) == QUOTED["lines"]
assert r"\raa" not in nd
Px, Qx = P("P", "x"), P("Q", "x")
prem = NOT(EX("x", IMP(Px, NOT(Qx))))
concl = ALL("x", AND(NOT(NOT(Px)), NOT(NOT(Qx))))
for n in range(1, 4):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            assert not is_counter_model([prem], concl, structure(D, pred={"P": Ps, "Q": Qs}))
print("exr-models-r3: all quoted values check")
