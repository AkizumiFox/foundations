"""exr-terms-formulas-substitution-b2 (Ch 4, Section 4.2): FV of two formulas."""
from _s0102_fol import *

QUOTED = {"second formula": "\\{z\\}"}

x, y, z = V('x'), V('y'), V('z')
assert fv(And(All('x', At('<', x, y)), Ex('y', At('<', y, x)))) == {'x', 'y'}
s = All('x', Ex('y', Eq(F('+', x, y), z)))
assert fv(Ex('y', Eq(F('+', x, y), z))) == {'x', 'z'} and fv(s) == {'z'}
from fractions import Fraction as Fr
R = [Fr(p, 3) for p in range(-20, 21)]
assert all(any(xx + yy == zz for yy in [zz - xx]) for xx in R for zz in R)
print("exr-terms-formulas-substitution-b2: all quoted values check")
