"""exr-models-b2 (Section 4.11): the cycle {(0,1),(1,2),(2,0)} on {0,1,2}, the two alternatives,
and the stated properties characterize all answers on {0,1,2}."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_relations, P, ALL, EX, NOT

QUOTED = {"elements": 3}
D = [0, 1, 2]
s1 = ALL("x", EX("y", P("R", "x", "y")))
s2 = ALL("x", NOT(P("R", "x", "x")))


def ok(R):
    M = structure(D, pred={"R": R})
    return sat(s1, M, {}) and sat(s2, M, {})


assert ok({(0, 1), (1, 2), (2, 0)})
assert ok({(0, 1), (1, 0), (2, 0)})
assert ok({(d, e) for d in D for e in D if d != e})
for R in all_relations(D, 2):
    props = all(any((d, e) in R for e in D) for d in D) and all((d, d) not in R for d in D)
    assert ok(R) == props
assert len(D) == QUOTED["elements"]
print("exr-models-b2: all quoted values check")
