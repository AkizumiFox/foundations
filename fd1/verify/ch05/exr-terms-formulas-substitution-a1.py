"""exr-terms-formulas-substitution-a1 (Ch 4, Section 4.2): free variables and a substitution."""
from _s0102_fol import *

QUOTED = {"(a) free variables": True}

x, y, c = V('x'), V('y'), C('c')
e, d = V('eps'), V('delta')
assert fv(All('x', Imp(At('P', x), At('Q', y)))) == {'y'}
assert fv(Ex('x', All('y', At('R', x, y)))) == set()
assert fv(And(All('x', At('<', x, y)), Ex('y', At('<', y, x)))) == {'x', 'y'}
assert fv(All('eps', Imp(At('>', e, C('0')), Ex('delta', And(At('>', d, C('0')), At('<', d, e)))))) == set()
# (c) a variable need not be free for x
assert not free_for(y, 'x', Ex('y', Not(Eq(y, x))))
# (d)
assert sub(And(All('x', At('P', x)), At('Q', x)), c, 'x') == And(All('x', At('P', x)), At('Q', c))
print("exr-terms-formulas-substitution-a1: all quoted values check")
