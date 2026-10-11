"""exm-computing-substitutions and the capture examples of Section 4.2 (Ch 4)."""
from _s0102_fol import *

QUOTED = {"(b) result": "y + 1 < y \\ \\wedge \\ \\forall x\\, (x \\ge 0)",
          "safe substitution": "\\forall z\\, (y + 1 < z)",
          "capture": "\\exists y\\, (y > y + 1)"}

x, y, z, c = V('x'), V('y'), V('z'), C('c')
two = C('2')
yp1 = F('+', y, C('1'))
# (a)
assert sub(Imp(At('P', x), At('S', x)), two, 'x') == Imp(At('P', two), At('S', two))
# (b)
phi = And(At('<', x, y), All('x', At('>=', x, C('0'))))
assert sub(phi, yp1, 'x') == And(At('<', yp1, y), All('x', At('>=', x, C('0'))))
assert free_for(yp1, 'x', phi)
# (c)
fz = F('f', z)
assert sub(All('y', At('R', x, y)), fz, 'x') == All('y', At('R', fz, y))
# (d)
assert sub(All('x', At('P', x)), c, 'x') == All('x', At('P', x))
# capture: exists y (y != x) with y for x
cap = Ex('y', Not(Eq(y, x)))
assert sub(cap, y, 'x') == Ex('y', Not(Eq(y, y))) and not free_for(y, 'x', cap)
# exists y (y > x) with y + 1
cap2 = Ex('y', At('>', y, x))
assert sub(cap2, yp1, 'x') == Ex('y', At('>', y, yp1)) and not free_for(yp1, 'x', cap2)
assert fv(cap2) == {'x'} and fv(sub(cap2, yp1, 'x')) == set()
# safe: forall z (x < z)
safe = All('z', At('<', x, z))
assert free_for(yp1, 'x', safe) and sub(safe, yp1, 'x') == All('z', At('<', yp1, z))
# not free for in forall y (x < y)
assert not free_for(yp1, 'x', All('y', At('<', x, y)))
# the recipe: rename then substitute
r = rename_top(cap, 'z')
assert r == Ex('z', Not(Eq(z, x))) and free_for(y, 'x', r) and sub(r, y, 'x') == Ex('z', Not(Eq(z, y)))
r2 = rename_top(cap2, 'z')
assert sub(r2, yp1, 'x') == Ex('z', At('>', z, yp1))
# y free for x in P(x) and exists y Q(y)
q = And(At('P', x), Ex('y', At('Q', y)))
assert free_for(y, 'x', q) and sub(q, y, 'x') == And(At('P', y), Ex('y', At('Q', y)))
# renaming without the condition changes meaning: forall y (y >= z) -> forall z (z >= z)
assert occurs('z', At('>=', y, z))
# over N: forall y (y >= z) true iff z = 0 (checked on a finite initial segment)
Nn = range(0, 50)
assert [zz for zz in range(0, 10) if all(yy >= zz for yy in Nn)] == [0]
# phi[x/x] = phi and the claim "x not free => phi[t/x] = phi" on random formulas
import random
random.seed(1)
vs = ['x', 'y', 'z']
def rt(d):
    if d == 0 or random.random() < .4:
        return V(random.choice(vs)) if random.random() < .7 else C('c')
    return F('f', rt(d - 1), rt(d - 1))
def rf(d):
    r = random.random()
    if d == 0 or r < .25:
        return At('R', rt(1), rt(1))
    if r < .4: return Not(rf(d - 1))
    if r < .6: return And(rf(d - 1), rf(d - 1))
    if r < .7: return Imp(rf(d - 1), rf(d - 1))
    return (random.choice(['all', 'ex']), random.choice(vs), rf(d - 1))
for _ in range(3000):
    p = rf(4); t = rt(2); v = random.choice(vs)
    assert sub(p, V(v), v) == p
    if v not in fv(p):
        assert sub(p, t, v) == p
    assert free_for(t, v, p) == free_for_rec(t, v, p)      # the recursive description
    if free_for(t, v, p) and v in fv(p):                     # exr C1 equation
        assert fv(sub(p, t, v)) == (fv(p) - {v}) | tvars(t)
print("exm-computing-substitutions: all quoted values check")
