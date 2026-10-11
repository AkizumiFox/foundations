"""exr-sets-from-axioms-b2 (Section 9.1): the intersection of S = {X, Y} with
X = {0, {0}}, Y = {{0}, {{0}}} (0 = emptyset), computed from A_0 = X and from A_0 = Y."""
E = frozenset()
one = frozenset({E})
X = frozenset({E, one})
Y = frozenset({one, frozenset({one})})
F = [X, Y]

QUOTED = {"intersection": frozenset({one})}


def inter(A0):
    return frozenset(x for x in A0 if all(x in S for S in F))


assert E not in Y and frozenset({one}) not in X
assert inter(X) == QUOTED["intersection"]
assert inter(Y) == QUOTED["intersection"]
print("exr-sets-from-axioms-b2: all quoted values check")
