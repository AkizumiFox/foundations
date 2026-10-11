"""exr-terms-formulas-substitution-c2 (Ch 4, Section 4.2): renaming vs swapping."""
from _s0102_fol import *

QUOTED = {"renaming chain": True}

x, y, z = V('x'), V('y'), V('z')
s1 = All('x', Ex('y', At('<', x, y)))
s2 = All('y', Ex('x', At('<', y, x)))
# step 1: rename x to z at the root
t1 = rename_top(s1, 'z')
assert t1 == All('z', Ex('y', At('<', z, y)))
# step 2: rename the inner y to x (x no longer occurs)
assert not occurs('x', t1)
t2 = ('all', 'z', rename_top(t1[2], 'x'))
assert t2 == All('z', Ex('x', At('<', z, x)))
# step 3: rename z to y
assert not occurs('y', t2)
t3 = rename_top(t2, 'y')
assert t3 == s2 and shape(s1) == shape(s2)
swap = Ex('y', All('x', At('<', x, y)))
assert shape(swap) != shape(s1)
# over N (initial segment), the first true with y = x + 1, the swap false with x = y
assert all(xx < xx + 1 for xx in range(0, 100)) and all(not (yy < yy) for yy in range(0, 100))
print("exr-terms-formulas-substitution-c2: all quoted values check")
