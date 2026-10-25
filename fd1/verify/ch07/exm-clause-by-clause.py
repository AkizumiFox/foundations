"""exm-clause-by-clause (Section 7.1): exists x forall y R(x, y) |= forall y exists x R(x, y) on
every structure with one two-place relation on 1-3 elements (and the converse fails on some), and
the two stacked changes of item 6 give the same assignment."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, is_counter_model, all_relations, P, ALL, EX

prem = EX("x", ALL("y", P("R", "x", "y")))
concl = ALL("y", EX("x", P("R", "x", "y")))
converse_fails = False
for n in range(1, 4):
    D = list(range(n))
    for R in all_relations(D, 2):
        M = structure(D, pred={"R": R})
        assert not is_counter_model([prem], concl, M)
        converse_fails |= is_counter_model([concl], prem, M)
assert converse_fails  # "The converse fails" (drawn in 7.2)

# item 6 / Quick check: l[x->d][y->e] == l[y->e][x->d] for different variables x, y
l = {"x": 7, "y": 8, "z": 9}
for d in range(3):
    for e in range(3):
        assert {**{**l, "x": d}, "y": e} == {**{**l, "y": e}, "x": d}
print("exm-clause-by-clause: all quoted values check")
