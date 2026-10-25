"""exm-three-classes (Section 7.2): the skeletons by truth table; forall x (x = x) valid on small
structures; the one-element structure with S(0) = 0; the Quick check (valid, skeleton p -> q).
Also the nine counter-models of the side-condition table ("Each side condition, broken"), which
is not a labelled block: finite ones by the evaluator, infinite ones on windows."""
import sys, itertools
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, is_counter_model, P, ALL, EX, NOT, AND, OR, IMP

taut = lambda f, n: all(f(*v) for v in itertools.product([False, True], repeat=n))
assert taut(lambda p: p or not p, 1)            # (a)
assert not taut(lambda p: p, 1)                 # (b) skeleton p
assert not taut(lambda p, q: (not p) or q, 2)   # Quick check skeleton p -> q

zero, S = ("c", "0"), lambda t: ("f", "S", t)
eqf = lambda s, t: ("eq", s, t)
# (b) valid: every structure on up to 3 elements (only = occurs)
for n in (1, 2, 3):
    assert sat(ALL("x", eqf("x", "x")), structure(range(n)), {})
# (c) true in N (window), false in D = {a}, 0 = a, S(a) = a
assert all(n + 1 != 0 for n in range(0, 1000))
M1 = structure(["a"], const={"0": "a"}, func={"S": lambda d: "a"})
assert not sat(ALL("x", NOT(eqf(S("x"), zero))), M1, {})
assert sat(eqf(S(zero), zero), M1, {})
# (d) false in N: no n with n + 1 = 0
assert not any(n + 1 == 0 for n in range(0, 1000))
# Quick check: forall x (x < S(x)) -> 0 < S(0) valid on all structures of size <= 2
from _fo_models import all_relations
for n in (1, 2):
    D = list(range(n))
    for Sv in itertools.product(D, repeat=n):
        for z in D:
            for L in all_relations(D, 2):
                M = structure(D, const={"0": z}, func={"S": lambda d, Sv=Sv: Sv[d]}, pred={"<": L})
                assert sat(IMP(ALL("x", P("<", "x", S("x"))), P("<", zero, S(zero))), M, {})

# --- the side-condition table ---
# 1. forall-E capture: D = {0, 1}
neq = lambda s, t: NOT(eqf(s, t))
M01 = structure([0, 1])
assert is_counter_model([ALL("x", EX("y", neq("y", "x")))], EX("y", neq("y", "y")), M01)
W = range(-200, 201)
# 2. Z, P even, l(x0) = 2: P(x0) true, forall x P(x) false (at 1)
assert 2 % 2 == 0 and 1 % 2 != 0
# 3. Z, l(x0) = 1: 1 > 0 true, forall x (x > 0) false at 0, so the implication is false
assert 1 > 0 and not all(x > 0 for x in W)
# 4. N with <=: premise true; every candidate y is beaten by y + 1
N = range(0, 400)
assert all(x <= x for x in N) and all(not (y + 1 <= y) for y in N)
# 5. Z with <=: forall y R(y, y) true; every candidate x fails at y = x - 1
assert all(y <= y for y in W) and all(not (x <= x - 1) for x in W)
# 6. N: exists x (x > 5) at 6; forall x (x > 5) fails at 0
assert 6 > 5 and not (0 > 5)
# 7. D = {1, 2}, P = {2}, l(x0) = 1
M7 = structure([1, 2], pred={"P": {(2,)}})
assert all(sat(f, M7, {"x0": 1}) for f in [EX("x", P("P", "x")), NOT(P("P", "x0"))])
# 8. three dots a -> b -> c -> a
M8 = structure("abc", pred={"R": {("a", "b"), ("b", "c"), ("c", "a")}})
assert is_counter_model([ALL("y", EX("x", P("R", "x", "y")))], EX("z", P("R", "z", "z")), M8)
# 9. Z, a and y both 0: a = y, exists y (y < a) (at -1), exists y (y < y) false
assert 0 == 0 and -1 < 0 and not any(y < y for y in W)
print("exm-three-classes: all quoted values check")
