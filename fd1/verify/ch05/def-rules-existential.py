"""def-rules-existential (Ch 4, Section 4.6) and the prose of that section: the hook
n + 2 = 2(k + 1); the readings of the three illegal derivations after the definition and of the
warnings (witness generalized; two witnesses one name: n = 2, m = 4); the front renaming fact
(phi[z/y])[t/z] = phi[t/y] for z not appearing in phi; the bounded-sequence arithmetic (now in a fold); the 5.6 deepening: the n + 2 box, the RIGHT
half of the clause-3 pair, the worlds of Figures C6a and C6b, the gallery
exm-existential-elimination-instances."""
import random
import sys
sys.path.insert(0, "verify/ch05")
from _s0102_fol import V, C, F, At, Eq, Not, And, Imp, All, Ex, sub, free_for, occurs
from _fo_models import structure, sat, is_counter_model, P, ALL, EX

QUOTED = {"two witnesses n": 2, "two witnesses m": 4, "sum": 6}

W = range(-100, 101)
N = range(0, 200)
# hook: n = 2k gives n + 2 = 2(k + 1)
assert all(2 * k + 2 == 2 * (k + 1) for k in W)
# clause 3: over N, exists x (x > 5) true, forall x (x > 5) false at 0
assert any(d > 5 for d in N) and not (0 > 5)
# clause 4: over N, P even, x_0 = 1: exists x P(x) true, not P(1) true
assert any(d % 2 == 0 for d in N) and 1 % 2 != 0
# clause 5: over Z with <: every integer has a smaller one; none is less than itself
assert all(any(e < d for e in [d - 1]) for d in W) and not any(d < d for d in W)
# the same on a finite check: the sequent forall y exists x R(x,y) |- exists z R(z,z) has a
# counter-model, so the illegal step can lose truth (structure on {0,1}: R = {(1,0),(0,1)})
M = structure([0, 1], pred={"R": {(1, 0), (0, 1)}})
assert is_counter_model([ALL("y", EX("x", P("R", "x", "y")))], EX("z", P("R", "z", "z")), M)
# warning 1: some integer even, not every integer even
assert any(d % 2 == 0 for d in W) and not all(d % 2 == 0 for d in W)
# warning 2: n = 2, m = 4 are even, n + m = 6 is not divisible by 4
n, m = QUOTED["two witnesses n"], QUOTED["two witnesses m"]
assert n % 2 == 0 and m % 2 == 0 and n + m == QUOTED["sum"] and (n + m) % 4 != 0
assert all(2 * k + 2 * k == 4 * k for k in W)          # the illegal arith line itself is right

# front renaming: (phi[z/y])[t/z] == phi[t/y] for z not appearing in phi; y0 free for z
y, z, x, y0 = V('y'), V('z'), V('x'), V('y_0')
samples = [Eq(y, x), And(At('P', y), All('x', At('R', x, y))),
           Imp(Ex('w', At('R', V('w'), y)), All('y', At('Q', y))), Not(Eq(y, F('f', y, x)))]
for phi in samples:
    assert not occurs('z', phi) and not occurs('y_0', phi)
    for t in [y0, C('c'), F('g', x)]:
        assert sub(sub(phi, z, 'y'), t, 'z') == sub(phi, t, 'y')
    assert free_for(y0, 'z', sub(phi, z, 'y'))
# bounded sequence: |a| <= M gives |2a| = 2|a| <= 2M
rng = random.Random(4)
for _ in range(2000):
    a = rng.uniform(-50, 50)
    Mb = abs(a) + rng.uniform(0, 10)
    assert abs(2 * a) == 2 * abs(a) <= 2 * Mb

# Section 5.6 deepening: A first witness, the RIGHT half, Figures C6a/C6b, the gallery
# RIGHT half: x_0 > 5 gives x_0 + 1 > 6; over N some number exceeds 6
assert all(k + 1 > 6 for k in N if k > 5) and any(k > 6 for k in N)
# Figure C6a: dots {0, 6}, the predicate "> 5", x_0 names 0
C6a = structure([0, 6], pred={"G": {(6,)}})
assert sat(EX("x", P("G", "x")), C6a, {}) and not sat(P("G", "x0"), C6a, {"x0": 0})
assert not sat(ALL("x", P("G", "x")), C6a, {})
# Figure C6b, clause 4: dots {1, 2}, P (even) at 2, x_0 names 1: both premises true
C6b4 = structure([1, 2], pred={"P": {(2,)}})
assert sat(EX("x", P("P", "x")), C6b4, {}) and sat(("not", P("P", "x0")), C6b4, {"x0": 1})
# Figure C6b, clause 5: triangle a -> b -> c -> a: premise true, exists z R(z, z) false
C6b5 = structure("abc", pred={"R": {("a", "b"), ("b", "c"), ("c", "a")}})
assert is_counter_model([ALL("y", EX("x", P("R", "x", "y")))], EX("z", P("R", "z", "z")), C6b5)
# gallery: row 1 m = 2k_0 + 1 gives m + 1 = 2(k_0 + 1); row 3 0 < d < e gives e > 0
assert all((2 * k + 1) + 1 == 2 * (k + 1) for k in W)
from fractions import Fraction as Fr
for e in [Fr(1, 3), Fr(2), Fr(5, 7)]:
    for d in [e / 2, e / 3, e * Fr(9, 10)]:
        assert 0 < d < e and e > 0
# gallery substitutions: each assumption is phi[name/var]; the look-alike is not
x_, c_ = V('x'), C('c')
assert sub(At('R', x_, c_), V('x_0'), 'x') == At('R', V('x_0'), c_) != At('R', c_, V('x_0'))
yv, u0, z_ = V('y'), V('u_0'), V('z')
phi2 = And(At('R', F('f', c_), yv), All('z', At('R', yv, z_)))
assert sub(phi2, u0, 'y') == And(At('R', F('f', c_), u0), All('z', At('R', u0, z_)))
assert free_for(u0, 'y', phi2)
print("def-rules-existential: all quoted values check")
