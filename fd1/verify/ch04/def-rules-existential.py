"""def-rules-existential (Ch 4, Section 4.6) and the prose of that section: the hook
n + 2 = 2(k + 1); the readings of the three illegal derivations after the definition and of the
warnings (witness generalized; two witnesses one name: n = 2, m = 4); the front renaming fact
(phi[z/y])[t/z] = phi[t/y] for z not appearing in phi; the bounded-sequence arithmetic."""
import random
import sys
sys.path.insert(0, "verify/ch04")
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
print("def-rules-existential: all quoted values check")
