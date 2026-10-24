"""exr-existential-elimination-b4 (Section 5.6, Derive or break): each counter-reading as a finite
structure (every premise true, the conclusion false), and a sanity check of each "derive"
verdict: no counter-reading on any domain of size 1-3 (all relevant relations, predicates and
functions enumerated). The derivations themselves are checked by tools/check_fitch.py."""
import itertools
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import structure, is_counter_model, all_relations, all_subsets, P, ALL, EX, NOT, IMP

fx = lambda t: ("f", "f", t)
A = ([EX("x", ALL("y", P("R", "x", "y")))], EX("x", P("R", "x", "x")))
B = ([ALL("x", EX("y", P("R", "x", "y")))], EX("x", P("R", "x", "x")))
Cc = ([ALL("x", IMP(P("P", "x"), P("Q", "x"))), EX("x", NOT(P("Q", "x")))], EX("x", NOT(P("P", "x"))))
D = ([ALL("x", IMP(P("P", "x"), P("Q", "x"))), EX("x", NOT(P("P", "x")))], EX("x", NOT(P("Q", "x"))))
E = ([EX("x", P("P", fx("x")))], EX("y", P("P", "y")))
Fc = ([EX("y", P("P", "y"))], EX("x", P("P", fx("x"))))
G = ([ALL("x", IMP(P("P", "x"), EX("y", P("R", "x", "y")))), EX("x", P("P", "x"))],
     EX("y", EX("x", P("R", "x", "y"))))

# the three counter-readings of the solution, on {0, 1}
assert is_counter_model(*B, structure([0, 1], pred={"R": {(0, 1), (1, 0)}}))
assert is_counter_model(*D, structure([0, 1], pred={"P": set(), "Q": {(0,), (1,)}}))
assert is_counter_model(*Fc, structure([0, 1], func={"f": lambda a: 0}, pred={"P": {(1,)}}))


def funcs(D_):
    for vals in itertools.product(D_, repeat=len(D_)):
        m = dict(zip(D_, vals))
        yield lambda a, m=m: m[a]


for n in (1, 2, 3):
    D_ = list(range(n))
    for R in all_relations(D_, 2):
        assert not is_counter_model(*A, structure(D_, pred={"R": R}))
        for Pset in all_subsets(D_):
            assert not is_counter_model(*G, structure(D_, pred={"R": R, "P": Pset}))
    for Pset in all_subsets(D_):
        for Qset in all_subsets(D_):
            assert not is_counter_model(*Cc, structure(D_, pred={"P": Pset, "Q": Qset}))
        for f in funcs(D_):
            assert not is_counter_model(*E, structure(D_, func={"f": f}, pred={"P": Pset}))
print("exr-existential-elimination-b4: all counter-readings and derive checks hold")
