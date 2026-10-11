"""prp-quantifier-passage and prp-quantifier-distribution (Section 4.9): independent semantic
sanity check. Each of the ten passage directions, with phi = R(x, y) and psi = Q(y) (x not free
in psi), holds in every structure with at most three elements under every assignment; the four
distribution laws hold, and the converses of (c) and (d) fail on D = {a, b} with P = {a},
Q = {b}. Also the text's failure when x is free in psi: over Z with P = even and x read as 1,
forall x (P(x) -> P(x)) is true and exists x P(x) -> P(x) is false."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, P, ALL, EX, NOT, AND, OR, IMP, all_relations, all_subsets

QUOTED = {"passage directions": 10, "classical directions": 2, "x read as": 1}

phi, psi = P("R", "x", "y"), P("Q", "y")
pairs = [
    (ALL("x", IMP(psi, phi)), IMP(psi, ALL("x", phi))),   # (a)
    (ALL("x", IMP(phi, psi)), IMP(EX("x", phi), psi)),    # (b)
    (EX("x", AND(phi, psi)), AND(EX("x", phi), psi)),     # (c)
    (EX("x", IMP(phi, psi)), IMP(ALL("x", phi), psi)),    # (d)
    (EX("x", IMP(psi, phi)), IMP(psi, EX("x", phi))),     # (e)
]
directions = [(l, r) for l, r in pairs] + [(r, l) for l, r in pairs]
assert len(directions) == QUOTED["passage directions"]
for n in (1, 2, 3):
    D = list(range(n))
    for R in all_relations(D, 2):
        for Q in all_subsets(D):
            M = structure(D, pred={"R": R, "Q": Q})
            for d in D:
                for e in D:
                    l = {"y": d, "x": e}
                    for prem, concl in directions:
                        if sat(prem, M, l):
                            assert sat(concl, M, l)
# distribution, with phi = P(x), psi = Q(x)
Px, Qx = P("P", "x"), P("Q", "x")
dist = [
    (ALL("x", AND(Px, Qx)), AND(ALL("x", Px), ALL("x", Qx))),
    (AND(ALL("x", Px), ALL("x", Qx)), ALL("x", AND(Px, Qx))),
    (EX("x", OR(Px, Qx)), OR(EX("x", Px), EX("x", Qx))),
    (OR(EX("x", Px), EX("x", Qx)), EX("x", OR(Px, Qx))),
    (OR(ALL("x", Px), ALL("x", Qx)), ALL("x", OR(Px, Qx))),
    (EX("x", AND(Px, Qx)), AND(EX("x", Px), EX("x", Qx))),
]
for n in (1, 2, 3):
    D = list(range(n))
    for Pp in all_subsets(D):
        for Qq in all_subsets(D):
            M = structure(D, pred={"P": Pp, "Q": Qq})
            for prem, concl in dist:
                if sat(prem, M, {"x": D[0]}):
                    assert sat(concl, M, {"x": D[0]})
M = structure(["a", "b"], pred={"P": {("a",)}, "Q": {("b",)}})
assert sat(ALL("x", OR(Px, Qx)), M, {}) and not sat(OR(ALL("x", Px), ALL("x", Qx)), M, {})
assert sat(AND(EX("x", Px), EX("x", Qx)), M, {}) and not sat(EX("x", AND(Px, Qx)), M, {})
# x free in psi: over a window of Z, P = even, x read as 1
Z = list(range(-6, 7))
even = lambda k: k % 2 == 0
assert all((not even(k)) or even(k) for k in Z)            # forall x (P(x) -> P(x))
x = QUOTED["x read as"]
assert any(even(k) for k in Z) and not even(x)              # exists x P(x) true, P(1) false
print("prp-quantifier-passage: all quoted values check")
