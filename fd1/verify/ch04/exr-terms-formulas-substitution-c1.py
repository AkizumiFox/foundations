"""exr-terms-formulas-substitution-c1 (Ch 4, Section 4.2): the FV equation and its two counterexamples.
The general equation is also checked on random formulas in exm-computing-substitutions.py."""
from _s0102_fol import *

QUOTED = {"counterexample (b), second": "\\{y, z\\}"}

x, y, z = V('x'), V('y'), V('z')
yp1 = F('+', y, C('1'))
p = Ex('y', At('>', y, x))
assert fv(p) == {'x'} and fv(sub(p, yp1, 'x')) == set() and (fv(p) - {'x'}) | tvars(yp1) == {'y'}
q = At('P', z)
assert 'x' not in fv(q) and free_for(y, 'x', q)
assert fv(sub(q, y, 'x')) == {'z'} and (fv(q) - {'x'}) | tvars(y) == {'y', 'z'}
print("exr-terms-formulas-substitution-c1: all quoted values check")
