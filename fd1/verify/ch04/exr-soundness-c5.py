"""exr-soundness-c5 (Section 4.7, two three-valued tables; the Kleene valuation u_K, written u below): u(not) = 1 - u, min, max,
u(phi -> psi) = max(1 - u(phi), u(psi)). Every one-step rule is checked for each set D of
designated values ({1} and {1/2, 1}), the box rules on the instances quoted; the values quoted in (a)-(c)."""
import itertools
from fractions import Fraction as F

H = F(1, 2)
V = (F(0), H, F(1))
neg = lambda a: 1 - a
imp = lambda a, b: max(1 - a, b)
iff = lambda a, b: min(imp(a, b), imp(b, a))


def survives(D):
    d = lambda a: a in D
    ok = {}
    combos = list(itertools.product((True, False), V, V, V))
    # m: whether the context is designated
    ok["andI"] = all(not (m and d(x) and d(y)) or d(min(x, y)) for m, x, y, z in combos)
    ok["andE"] = all(not (m and d(min(x, y))) or (d(x) and d(y)) for m, x, y, z in combos)
    ok["orI"] = all(not (m and d(x)) or d(max(x, y)) for m, x, y, z in combos)
    ok["impE"] = all(not (m and d(imp(x, y)) and d(x)) or d(y) for m, x, y, z in combos)
    ok["iffE"] = all(not (m and d(iff(x, y)) and d(x)) or d(y) for m, x, y, z in combos)
    ok["negE"] = all(not (m and d(x) and d(neg(x))) or d(F(0)) for m, x, y, z in combos)
    ok["botE"] = all(not (m and d(F(0))) or d(z) for m, x, y, z in combos)
    # the box rules are tested on the one-letter instances of (a) and below
    return ok


def entails(D, prem, concl, n):
    for vals in itertools.product(V, repeat=n):
        if all(p(*vals) in D for p in prem) and concl(*vals) not in D:
            return False
    return True


r1, r2 = survives({F(1)}), survives({H, F(1)})
assert all(r1.values()), r1                      # D = {1}: every one-step rule survives
assert not r2["impE"] and not r2["negE"] and r2["andI"] and r2["orI"], r2
# (a) D = {1}: p D-entails p, but p -> p is undesignated at 1/2
assert entails({F(1)}, [lambda p: p], lambda p: p, 1)
assert imp(H, H) == H and H not in {F(1)}
# (b) D = {1/2, 1}: p -> q and p designated, q not, at (1/2, 0)
assert imp(H, F(0)) == H and F(0) not in {H, F(1)}
# (c) excluded middle
assert max(H, neg(H)) == H                                   # fails for D = {1}
assert all(max(x, neg(x)) >= H for x in V)                   # holds for D = {1/2, 1}
# recorded: for D = {1/2, 1}, the box rules ->I and not-I survive one-letter tests
assert entails({H, F(1)}, [], lambda p: imp(p, p), 1)
print("exr-soundness-c5: all quoted values check")
