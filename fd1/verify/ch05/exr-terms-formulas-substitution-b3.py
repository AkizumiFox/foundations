"""exr-terms-formulas-substitution-b3 (Section 5.2): swapping two letters in
phi = exists z (R(x, z) & R(z, y))."""
from _s0102_fol import *
from _fo_models import structure, sat, P, EX, AND

QUOTED = {"(a) is the swap": False, "reading: swap true": True, "reading: computed true": False,
          "reading witness z": 1, "(c) z free for x": False}
x, y, z, u = V('x'), V('y'), V('z'), V('u')
phi = Ex('z', And(At('R', x, z), At('R', z, y)))
swap = Ex('z', And(At('R', y, z), At('R', z, x)))
a1 = sub(phi, y, 'x')
assert a1 == Ex('z', And(At('R', y, z), At('R', z, y)))
computed = sub(a1, x, 'y')
assert computed == Ex('z', And(At('R', x, z), At('R', z, x)))
assert (computed == swap) == QUOTED["(a) is the swap"]
# (b): through u, free for at each step
s1 = sub(phi, u, 'x'); assert free_for(u, 'x', phi)
assert s1 == Ex('z', And(At('R', u, z), At('R', z, y)))
s2 = sub(s1, x, 'y'); assert free_for(x, 'y', s1)
assert s2 == Ex('z', And(At('R', u, z), At('R', z, x)))
s3 = sub(s2, y, 'u'); assert free_for(y, 'u', s2)
assert s3 == swap
# (c)
assert free_for(z, 'x', phi) == QUOTED["(c) z free for x"]
assert sub(phi, z, 'x') == Ex('z', And(At('R', z, z), At('R', z, y)))
# the reading over N with R as <, x = 2, y = 0 (checked on {0, 1, 2})
M = structure([0, 1, 2], pred={"R": {(i, j) for i in range(3) for j in range(3) if i < j}})
l = {"x": 2, "y": 0}
swapM = EX("z", AND(P("R", "y", "z"), P("R", "z", "x")))
compM = EX("z", AND(P("R", "x", "z"), P("R", "z", "x")))
assert sat(swapM, M, l) == QUOTED["reading: swap true"]
assert sat(compM, M, l) == QUOTED["reading: computed true"]
assert sat(AND(P("R", "y", "z"), P("R", "z", "x")), M, {**l, "z": QUOTED["reading witness z"]})
# over a larger initial segment of N the computed formula stays false (no z with 2 < z < 2)
assert not any(2 < k < 2 for k in range(100))
print("exr-terms-formulas-substitution-b3: all quoted values check")
