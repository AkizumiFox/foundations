"""thm-cancellation (F2.6 §02), the fold "Part (a) by cancellation", exm-method-cancel,
and exr-functions-c1/-c2 (b) and prp-composite-partial-converse:
brute force over all functions between sets of sizes 0..3."""
import sys
sys.path.insert(0, "verify/ch01")
from _sets import functions, injective, surjective

QUOTED = {"W in the proof": {0}, "Z in the proof": {0, 1}}


def comp(g, f):
    return {x: g[f[x]] for x in f}


sets = [frozenset(range(n)) for n in range(4)]
for X in sets:
    for Y in sets:
        for f in functions(X, Y):
            # (a): injective iff left-cancellable against all W of size <= 3
            leftc = all(comp(f, g) != comp(f, h) or g == h
                        for W in sets for g in functions(W, X) for h in functions(W, X))
            assert injective(f) == leftc
            # the proof only needs W = {0}
            W = QUOTED["W in the proof"]
            leftc0 = all(comp(f, g) != comp(f, h) or g == h
                         for g in functions(W, X) for h in functions(W, X))
            assert injective(f) == leftc0
            # (b): surjective iff right-cancellable against all Z of size <= 3
            rightc = all(comp(g, f) != comp(h, f) or g == h
                         for Z in sets for g in functions(Y, Z) for h in functions(Y, Z))
            assert surjective(f, Y) == rightc
            Z = QUOTED["Z in the proof"]
            rightc01 = all(comp(g, f) != comp(h, f) or g == h
                           for g in functions(Y, Z) for h in functions(Y, Z))
            assert surjective(f, Y) == rightc01
            # the proof's witnesses: constant 0 and the indicator of a missed point
            missed = [y for y in Y if y not in f.values()]
            for y0 in missed:
                g = {y: 0 for y in Y}
                h = {y: (1 if y == y0 else 0) for y in Y}
                assert comp(g, f) == comp(h, f) and g != h
            for Zs in sets:
                for g in functions(Y, Zs):
                    gf = comp(g, f)
                    if injective(gf):
                        assert injective(f)                     # partial converse (a)
                    if surjective(gf, Zs):
                        assert surjective(g, Zs)                # partial converse (b)
                    if injective(gf) and surjective(f, Y):
                        assert injective(g)                     # C1 (a)
                    if surjective(gf, Zs) and injective(g):
                        assert surjective(f, Y)                 # B2's claim
                    if injective(gf) and surjective(gf, Zs) and surjective(f, Y):
                        assert injective(f) and injective(g) and surjective(g, Zs)  # C2 (b)

# exm-method-cancel: an injection does not cancel on the right
f = {0: 0}
g = {0: 0, 1: 1}
h = {0: 0, 1: 0}
assert injective(f) and comp(g, f) == comp(h, f) and g != h
# the lead's example before prp-composite-partial-converse
f = {1: 1}
g = {1: 1, 2: 1}
gf = comp(g, f)
assert gf == {1: 1} and not injective(g) and not surjective(f, {1, 2})
print("thm-cancellation: all statements check")
