"""exr-models-r4 (Section 4.11): in (N, <) the hypothesis forall x exists y (x < y) holds
(witness d + 1) and the conclusion exists y forall x (x < y) fails (at x = e); window check.
The propositional skeleton p -> q is refutable while forall x P -> exists x P is valid on small
structures (the look-alike)."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_subsets, P, ALL, EX, IMP

QUOTED = {}
W = range(0, 500)
assert all(d + 1 > d for d in W)
assert all(not (e < e) for e in W)
f = IMP(ALL("x", P("P", "x")), EX("x", P("P", "x")))
for n in range(1, 4):
    for Ps in all_subsets(range(n)):
        assert sat(f, structure(range(n), pred={"P": Ps}), {})
print("exr-models-r4: all quoted values check")
