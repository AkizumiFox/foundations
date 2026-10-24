"""exm-extensionality-logical-half (Section 5.7): the logical half
forall x forall y (x = y -> forall z (z in x <-> z in y)) is true in every structure on
1-3 elements (a sanity check), and the converse breaks on two dots a, b with empty membership."""
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import structure, sat, all_relations, P, ALL, IMP

QUOTED = {"dots": 2}

mem = lambda s, t: P("in", s, t)
iff = lambda f, g: ("iff", f, g)
half = ALL("x", ALL("y", IMP(("eq", "x", "y"), ALL("z", iff(mem("z", "x"), mem("z", "y"))))))
for n in (1, 2, 3):
    for R in all_relations(range(n), 2):
        assert sat(half, structure(range(n), pred={"in": R}), {})

# the converse, with x naming a = 0 and y naming b = 1, nothing an element of anything
conv = IMP(ALL("z", iff(mem("z", "x"), mem("z", "y"))), ("eq", "x", "y"))
M = structure(range(QUOTED["dots"]), pred={"in": set()})
l = {"x": 0, "y": 1}
assert sat(ALL("z", iff(mem("z", "x"), mem("z", "y"))), M, l)
assert not sat(("eq", "x", "y"), M, l)
assert not sat(conv, M, l)
print("exm-extensionality-logical-half: all quoted values check")
