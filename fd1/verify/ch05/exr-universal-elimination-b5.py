"""exr-universal-elimination-b5 (Section 5.3, derive or break): each counter-reading of
(b), (d), (e), (g) makes every premise true and the conclusion false; each "derive" claim
(a), (c), (f), (h) is true in every structure on a domain of size 1-3 (a sanity check only;
the derivations are checked by tools/check_fitch.py)."""
import itertools
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import (structure, sat, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, OR, IMP)

c = ("c", "c")
def f(t):
    return ("f", "f", t)

CLAIMS = {
    "a": ([ALL("x", OR(P("P", "x"), P("Q", "x"))), NOT(P("P", c))], P("Q", c)),
    "b": ([ALL("x", IMP(P("P", "x"), P("Q", "x"))), P("Q", c)], P("P", c)),
    "c": ([ALL("x", P("R", "x", f("x")))], AND(P("R", c, f(c)), P("R", f(c), f(f(c))))),
    "d": ([ALL("x", P("R", "x", f("x")))], P("R", f(c), c)),
    "e": ([ALL("x", IMP(P("P", "x"), NOT(P("P", f("x"))))), P("P", c)], NOT(P("P", f(f(c))))),
    "f": ([ALL("x", IMP(P("P", "x"), NOT(P("P", f("x"))))), P("P", f(c))],
          AND(NOT(P("P", c)), NOT(P("P", f(f(c)))))),
    "g": ([ALL("x", EX("y", P("R", "x", "y")))], EX("y", P("R", "y", "y"))),
    "h": ([ALL("x", EX("y", P("R", "x", "y")))], EX("y", P("R", c, "y"))),
}

# The counter-readings, as printed in the solution.
QUOTED = {
    "b": structure([0], const={"c": 0}, pred={"P": set(), "Q": {(0,)}}),
    "d": structure([0, 1], const={"c": 0}, func={"f": {0: 1, 1: 1}.get},
                   pred={"R": {(0, 1), (1, 1)}}),
    "e": structure([0, 1], const={"c": 0}, func={"f": {0: 1, 1: 0}.get},
                   pred={"P": {(0,)}}),
    "g": structure([0, 1], pred={"R": {(0, 1), (1, 0)}}),
}
for k, M in QUOTED.items():
    prem, concl = CLAIMS[k]
    assert is_counter_model(prem, concl, M), k


def functions(D):
    for vals in itertools.product(D, repeat=len(D)):
        yield dict(zip(D, vals)).get


def structures(D, k):
    """Every interpretation of the symbols claim k uses, on domain D."""
    uses_f = k in "cf"
    uses_R = k in "ch"
    for cv in D:
        for fn in (functions(D) if uses_f else [None]):
            if uses_R:
                preds_iter = ({"R": R} for R in all_relations(D, 2))
            elif k == "a":
                preds_iter = ({"P": p, "Q": q} for p in all_subsets(D) for q in all_subsets(D))
            else:
                preds_iter = ({"P": p} for p in all_subsets(D))
            for preds in preds_iter:
                yield structure(D, const={"c": cv}, func={"f": fn} if fn else {}, pred=preds)


for k in "acfh":
    prem, concl = CLAIMS[k]
    for n in (1, 2, 3):
        for M in structures(list(range(n)), k):
            assert not is_counter_model(prem, concl, M), (k, n)
print("exr-universal-elimination-b5: all quoted values check")
