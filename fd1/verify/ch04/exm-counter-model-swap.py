"""exm-counter-model-swap and the counter-models after it (Section 4.11): the swap on Z (window)
and on {a, b}; no one-element counter-model; converses of prp-exists-and and of the forall/or
law; exists x P(x) |/= P(c); P(x0) |/= forall x P(x) in Z with l(x0) = 2; the strict-order models
Z and Q (windows) and the one-element non-model; the Quick check model for
forall x P -> forall x Q |/= forall x (P -> Q). Also reused by Section 4.12 (B2, the list after
cor-counter-model)."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch04")
from _fo_models import (structure, sat, is_counter_model, all_relations, all_subsets,
                        P, ALL, EX, NOT, AND, OR, IMP)

QUOTED = {"elements needed": 2}

prem = ALL("y", EX("x", P("R", "x", "y")))
concl = EX("x", ALL("y", P("R", "x", "y")))

# two-element identity model
M2 = structure(["a", "b"], pred={"R": {("a", "a"), ("b", "b")}})
assert is_counter_model([prem], concl, M2)

# no one-element counter-model: both sentences agree on {a}
for R in all_relations(["a"], 2):
    M1 = structure(["a"], pred={"R": R})
    assert sat(prem, M1, {}) == sat(concl, M1, {})
# some two-element counter-model exists (so 2 is the least that will do)
assert any(is_counter_model([prem], concl, structure(["a", "b"], pred={"R": R}))
           for R in all_relations(["a", "b"], 2))

# Z with R(x, y) = x > y: premise witness y + 1; conclusion fails at y = x (window)
W = range(-200, 201)
assert all((e + 1) > e for e in W)
assert all(not (d > d) for d in W)

# converse of prp-exists-and; converse of forall/or law; D = {a, b}, P = {a}, Q = {b}
Mpq = structure(["a", "b"], pred={"P": {("a",)}, "Q": {("b",)}})
Px, Qx = P("P", "x"), P("Q", "x")
assert is_counter_model([AND(EX("x", Px), EX("x", Qx))], EX("x", AND(Px, Qx)), Mpq)
assert is_counter_model([ALL("x", OR(Px, Qx))], OR(ALL("x", Px), ALL("x", Qx)), Mpq)
# ... and the forward laws hold in every structure on up to 3 elements
for n in range(1, 4):
    D = list(range(n))
    for Ps in all_subsets(D):
        for Qs in all_subsets(D):
            M = structure(D, pred={"P": Ps, "Q": Qs})
            assert not is_counter_model([EX("x", AND(Px, Qx))], AND(EX("x", Px), EX("x", Qx)), M)
            assert not is_counter_model([OR(ALL("x", Px), ALL("x", Qx))], ALL("x", OR(Px, Qx)), M)

# exists x P(x) |/= P(c): c = a, P = {b}
Mc = structure(["a", "b"], const={"c": "a"}, pred={"P": {("b",)}})
assert is_counter_model([EX("x", Px)], P("P", ("c", "c")), Mc)

# P(x0) |/= forall x P(x) in Z (window), P = evens, l(x0) = 2; fails at d = 1; l(x0) = 1 refutes nothing
even = lambda d: d % 2 == 0
assert even(2) and not even(1) and not even(1)  # premise true at 2; conclusion fails at 1; at l(x0)=1 premise false

# strict order without largest element: Z and Q windows; one-element non-model
for D in [list(range(-30, 31)), [F(k, 4) for k in range(-40, 41)]]:
    assert all(not (d < d) for d in D)
    assert all((d + 1) > d for d in D)
for R in all_relations(["a"], 2):
    M = structure(["a"], pred={"<": R})
    irr = sat(ALL("x", NOT(P("<", "x", "x"))), M, {})
    nolargest = sat(ALL("x", EX("y", P("<", "x", "y"))), M, {})
    assert not (irr and nolargest)

# Quick check: D = {a, b}, P = {a}, Q = empty
Mq = structure(["a", "b"], pred={"P": {("a",)}, "Q": set()})
assert is_counter_model([IMP(ALL("x", Px), ALL("x", Qx))], ALL("x", IMP(Px, Qx)), Mq)
assert QUOTED["elements needed"] == 2
print("exm-counter-model-swap: all quoted values check")
