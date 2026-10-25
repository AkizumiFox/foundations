"""exr-theories-and-models-c1 (Section 7.4): the four descriptions of every model, checked
on all structures of sizes 1-3."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, all_relations, P, ALL, EX, AND, OR, IMP, NOT

eq = lambda s, t: ("eq", s, t)
a = ALL("x", ALL("y", eq("x", "y")))
b = AND(EX("x", EX("y", NOT(eq("x", "y")))),
        ALL("x", ALL("y", ALL("z", OR(OR(eq("x", "y"), eq("x", "z")), eq("y", "z"))))))
c = ALL("x", ALL("y", P("R", "x", "y")))
d = ALL("x", EX("y", AND(P("R", "x", "y"), ALL("z", IMP(P("R", "x", "z"), eq("z", "y"))))))
for n in (1, 2, 3):
    D = list(range(n))
    M = structure(D)
    assert sat(a, M, {}) == (n == 1)
    assert sat(b, M, {}) == (n == 2)
    for R in all_relations(D, 2):
        M = structure(D, pred={"R": R})
        assert sat(c, M, {}) == (len(R) == n * n)
        assert sat(d, M, {}) == all(sum((x, y) in R for y in D) == 1 for x in D)
print("exr-theories-and-models-c1: all quoted values check")
