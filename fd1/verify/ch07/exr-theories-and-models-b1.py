"""exr-theories-and-models-b1 (Section 7.4): the four properties of each answer by
enumeration; (iii) no irreflexive, symmetric, transitive, non-empty relation on domains
of size 1-4."""
import sys
sys.path.insert(0, "verify/ch07")
from _rel_props import refl, irrefl, sym, antisym, trans, all_relations

D = [1, 2, 3, 4]
QUOTED = {
    "i": {(d, d) for d in D} | {(1, 2), (2, 1), (1, 3), (2, 3)},
    "ii": {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)},
}
R = QUOTED["i"]
assert refl(D, R) and trans(D, R) and not sym(D, R) and not antisym(D, R)
R = QUOTED["ii"]
assert sym(D, R) and trans(D, R) and not refl(D, R)
assert all(any((d, e) in R for e in D) for d in (1, 2, 3))
assert not any((4, e) in R or (e, 4) in R for e in D)
for n in range(1, 5):
    Dn = list(range(n))
    assert not any(R and irrefl(Dn, R) and sym(Dn, R) and trans(Dn, R)
                   for R in all_relations(Dn))
print("exr-theories-and-models-b1: all quoted values check")
