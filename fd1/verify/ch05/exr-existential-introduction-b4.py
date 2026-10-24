"""exr-existential-introduction-b4 (Section 5.5, Derive or break) and A2 (i): each counter-reading
as a finite structure (every premise true, the conclusion false), and a sanity check of each
"derive" verdict: the sequent has no counter-reading on any domain of size 1-3 (all relations
and functions enumerated). The derivations themselves are checked by tools/check_fitch.py."""
import itertools
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import structure, sat, is_counter_model, all_relations, all_subsets, P, ALL, EX, NOT, AND, OR, IMP

c, d = ("c", "c"), ("c", "d")
fx = lambda t: ("f", "f", t)

# the claims, as (premises, conclusion)
A = ([ALL("x", P("P", "x"))], EX("x", OR(P("P", "x"), P("Q", "x"))))
B = ([EX("x", P("P", "x"))], ALL("x", P("P", "x")))
Cc = ([AND(P("R", c, d), P("R", d, c))], EX("x", P("R", "x", "x")))
D = ([AND(P("R", c, d), P("R", d, c))], EX("x", EX("y", AND(P("R", "x", "y"), P("R", "y", "x")))))
E = ([ALL("x", P("R", "x", fx("x")))], ALL("x", EX("y", P("R", "x", "y"))))
Fc = ([ALL("x", P("R", "x", fx("x")))], EX("y", ALL("x", P("R", "x", "y"))))
G = ([], EX("x", IMP(P("P", "x"), P("P", "x"))))

# the three counter-readings of the solution, on {0, 1}
MB = structure([0, 1], pred={"P": {(0,)}})
assert is_counter_model(*B, MB)
MC = structure([0, 1], const={"c": 0, "d": 1}, pred={"R": {(0, 1), (1, 0)}})
assert is_counter_model(*Cc, MC)
MF = structure([0, 1], func={"f": lambda a: a}, pred={"R": {(0, 0), (1, 1)}})
assert is_counter_model(*Fc, MF)

# A2 (i): P(a), Q(b) with goal exists x (P(x) /\ Q(x)): domain {a, b}, P of a only, Q of b only
MI = structure(["a", "b"], const={"a": "a", "b": "b"}, pred={"P": {("a",)}, "Q": {("b",)}})
assert is_counter_model([P("P", ("c", "a")), P("Q", ("c", "b"))],
                        EX("x", AND(P("P", "x"), P("Q", "x"))), MI)


def funcs(D_):
    for vals in itertools.product(D_, repeat=len(D_)):
        m = dict(zip(D_, vals))
        yield lambda a, m=m: m[a]


for n in (1, 2, 3):
    D_ = list(range(n))
    for Pset in all_subsets(D_):                       # (a), (g): P and Q only
        for Qset in all_subsets(D_):
            M = structure(D_, pred={"P": Pset, "Q": Qset})
            for claim in (A, G):
                assert not is_counter_model(*claim, M, {"x": 0})
    for R in all_relations(D_, 2):                     # (d): R, c, d; (e): R, f
        for cv, dv in itertools.product(D_, repeat=2):
            assert not is_counter_model(*D, structure(D_, const={"c": cv, "d": dv}, pred={"R": R}))
        for f in funcs(D_):
            assert not is_counter_model(*E, structure(D_, func={"f": f}, pred={"R": R}))
print("exr-existential-introduction-b4: all counter-readings and derive checks hold")
