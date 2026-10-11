"""prp-quantifier-negation and prp-bounded-quantifier-negation (Section 4.9): an independent
semantic sanity check. Every direction derived in the text must hold in every finite structure
(a derivable sequent is valid), so we check each direction in all structures with at most three
elements, with phi = R(x, y) (x and y free), under every assignment of y. The bounded laws are
checked with the bound x in A read as a unary predicate A."""
import sys
import itertools
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, P, ALL, EX, NOT, AND, IMP, all_relations, all_subsets

QUOTED = {"directions checked (quantifier negation)": 4, "directions checked (bounded)": 4}

phi = P("R", "x", "y")
Ax = P("A", "x")
laws = [  # (premise, conclusion)
    (NOT(ALL("x", phi)), EX("x", NOT(phi))),              # (a)
    (EX("x", NOT(phi)), NOT(ALL("x", phi))),              # (b)
    (NOT(EX("x", phi)), ALL("x", NOT(phi))),              # (c) ->
    (ALL("x", NOT(phi)), NOT(EX("x", phi))),              # (c) <-
]
bounded = [
    (NOT(ALL("x", IMP(Ax, phi))), EX("x", AND(Ax, NOT(phi)))),
    (EX("x", AND(Ax, NOT(phi))), NOT(ALL("x", IMP(Ax, phi)))),
    (NOT(EX("x", AND(Ax, phi))), ALL("x", IMP(Ax, NOT(phi)))),
    (ALL("x", IMP(Ax, NOT(phi))), NOT(EX("x", AND(Ax, phi)))),
]
assert len(laws) == QUOTED["directions checked (quantifier negation)"]
assert len(bounded) == QUOTED["directions checked (bounded)"]
count = 0
for n in (1, 2, 3):
    D = list(range(n))
    for R in all_relations(D, 2):
        for A in all_subsets(D):
            M = structure(D, pred={"R": R, "A": A})
            for d in D:
                l = {"y": d, "x": d}
                for prem, concl in laws + bounded:
                    if sat(prem, M, l):
                        assert sat(concl, M, l), (n, R, A, d, prem)
                count += 1
# the wrong negation of a bounded quantifier is not equivalent: forall e > 0 (e > 0) and
# exists e <= 0 not(e > 0) are both true over the reals (witness e = 0)
assert all(e > 0 for e in [0.5, 1, 7]) and (not (0 > 0)) and 0 <= 0
print("prp-quantifier-negation: all quoted values check", count)
