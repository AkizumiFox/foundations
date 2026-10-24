"""exr-counting-and-descriptions-b4 (Section 5.8): the counter-reading of (b): on the domain {0}
with 0 in 0, the axiom of extensionality E is true and exists x forall z not(z in x) is false.
Sanity check for (a): in every structure on 1-3 elements, E and the two emptiness premises
for a, b give a = b."""
import sys, itertools
sys.path.insert(0, "verify/ch05")
from _fo_models import structure, sat, all_relations, P, ALL, EX, NOT, IMP, AND

QUOTED = {"domain": [0], "membership": {(0, 0)}}

mem = lambda s, t: P("in", s, t)
iff = lambda f, g: ("iff", f, g)
E = ALL("x", ALL("y", IMP(ALL("z", iff(mem("z", "x"), mem("z", "y"))), ("eq", "x", "y"))))
empty_exists = EX("x", ALL("z", NOT(mem("z", "x"))))

M = structure(QUOTED["domain"], pred={"in": QUOTED["membership"]})
assert sat(E, M, {}) and not sat(empty_exists, M, {})

a, b = ("c", "a"), ("c", "b")
prem = AND(E, AND(ALL("z", NOT(mem("z", a))), ALL("z", NOT(mem("z", b)))))
for n in (1, 2, 3):
    D = range(n)
    for R in all_relations(D, 2):
        for va, vb in itertools.product(D, repeat=2):
            Mn = structure(D, const={"a": va, "b": vb}, pred={"in": R})
            assert not sat(prem, Mn, {}) or sat(("eq", a, b), Mn, {})
print("exr-counting-and-descriptions-b4: all quoted values check")
