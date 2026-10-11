"""exr-existential-elimination-c1 (Ch 4, Section 4.6): the reading over Z with R(x, y) as
'x * y = 0': symmetric, 0 is the only witness for the first premise; and the entailment in every
structure with at most 3 elements."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_relations, P, ALL, EX, IMP

QUOTED = {"witness": 0, "lines": 10}

W = range(-60, 61)
R = lambda x, y: x * y == 0
assert all(R(x, y) == R(y, x) for x in W for y in W)
assert all(R(QUOTED["witness"], y) for y in W)
assert all(R(y, QUOTED["witness"]) for y in W)
assert [x for x in W if all(R(x, y) for y in W)] == [QUOTED["witness"]]
prem = [EX("x", ALL("y", P("R", "x", "y"))),
        ALL("x", ALL("y", IMP(P("R", "x", "y"), P("R", "y", "x"))))]
concl = ALL("y", EX("x", P("R", "y", "x")))
for n in (1, 2, 3):
    D = list(range(n))
    for Rr in all_relations(D, 2):
        M = structure(D, pred={"R": Rr})
        assert (not all(sat(p, M, {}) for p in prem)) or sat(concl, M, {})
print("exr-existential-elimination-c1: all quoted values check")
