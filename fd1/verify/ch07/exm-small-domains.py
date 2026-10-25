"""exm-small-domains (Section 7.2): no counter-model of size 1; on {a, b} the counter-model is
exactly R = {(a, b), (b, a)}; the reading x != y on {0, 1}; the expansions (first premise, the
Quick check on exists x forall y R(x, y)) agree with the sentences on every structure on {a, b}."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, is_counter_model, all_relations, P, ALL, EX, IMP

prem = [ALL("x", EX("y", P("R", "x", "y"))),
        ALL("x", ALL("y", IMP(P("R", "x", "y"), P("R", "y", "x"))))]
concl = EX("x", P("R", "x", "x"))

assert not any(is_counter_model(prem, concl, structure(["a"], pred={"R": R}))
               for R in all_relations(["a"], 2))
cms = [R for R in all_relations(["a", "b"], 2)
       if is_counter_model(prem, concl, structure(["a", "b"], pred={"R": R}))]
assert cms == [{("a", "b"), ("b", "a")}]
assert {(x, y) for x in (0, 1) for y in (0, 1) if x != y} == {(0, 1), (1, 0)}

for R in all_relations(["a", "b"], 2):
    M = structure(["a", "b"], pred={"R": R})
    r = lambda x, y: (x, y) in R
    assert sat(prem[0], M, {}) == ((r("a", "a") or r("a", "b")) and (r("b", "a") or r("b", "b")))
    assert sat(EX("x", ALL("y", P("R", "x", "y"))), M, {}) == \
        ((r("a", "a") and r("a", "b")) or (r("b", "a") and r("b", "b")))
print("exm-small-domains: all quoted values check")
