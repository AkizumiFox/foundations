"""exr-terms-formulas-substitution-b1 (Ch 4, Section 4.2): five substitutions, two with renaming."""
from _s0102_fol import *

QUOTED = {"(c)": "\\forall z\\, (y + 1 < z)", "(d)": "\\exists z\\, (z = 2 \\cdot x)",
          "(e)": "\\exists y\\, (y > x) \\wedge Q(x + 1)"}

x, y, z, c = V('x'), V('y'), V('z'), C('c')
fy = F('f', y)
a = And(At('P', x), At('R', x, y))
assert free_for(fy, 'x', a) and sub(a, fy, 'x') == And(At('P', fy), At('R', fy, y))
b = Imp(All('x', At('R', x, y)), At('P', x))
assert free_for(c, 'x', b) and sub(b, c, 'x') == Imp(All('x', At('R', x, y)), At('P', c))
yp1 = F('+', y, C('1'))
cc = All('y', At('<', x, y))
assert not free_for(yp1, 'x', cc)
cr = rename_top(cc, 'z')
assert free_for(yp1, 'x', cr) and sub(cr, yp1, 'x') == All('z', At('<', yp1, z))
assert sub(cc, yp1, 'x') == All('y', At('<', yp1, y))              # the captured version
two_y = F('*', C('2'), y)
dd = Ex('x', Eq(x, two_y))
assert not free_for(x, 'y', dd)
dr = rename_top(dd, 'z')
assert sub(dr, x, 'y') == Ex('z', Eq(z, F('*', C('2'), x)))
assert sub(dd, x, 'y') == Ex('x', Eq(x, F('*', C('2'), x)))        # the captured version
xp1 = F('+', x, C('1'))
ee = And(Ex('y', At('>', y, x)), At('Q', y))
assert free_for(xp1, 'y', ee) and sub(ee, xp1, 'y') == And(Ex('y', At('>', y, x)), At('Q', xp1))
print("exr-terms-formulas-substitution-b1: all quoted values check")
