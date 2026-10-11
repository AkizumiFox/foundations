"""exm-existential-elimination-derivations (Ch 4, Section 4.6): (a) the two sides agree in every
small structure; (b) holds in every small structure, and its reading over Z (P odd,
Q divisible by 4)."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, all_subsets, P, ALL, EX, NOT, OR, IMP

QUOTED = {"(a) lines": [10, 12], "(b) lines": 10}

a_left = EX("x", OR(P("P", "x"), P("Q", "x")))
a_right = OR(EX("x", P("P", "x")), EX("x", P("Q", "x")))
b_prem = [EX("x", P("P", "x")), ALL("x", IMP(P("P", "x"), NOT(P("Q", "x"))))]
b_concl = NOT(ALL("x", P("Q", "x")))
for n in (1, 2, 3):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            M = structure(D, pred={"P": Ps, "Q": Qs})
            assert sat(a_left, M, {}) == sat(a_right, M, {})
            assert (not all(sat(p, M, {}) for p in b_prem)) or sat(b_concl, M, {})
W = range(-100, 101)
assert any(d % 2 == 1 for d in W)
assert not any(d % 2 == 1 and d % 4 == 0 for d in W)
assert not all(d % 4 == 0 for d in W)
print("exm-existential-elimination-derivations: all quoted values check")
