"""exr-existential-introduction-c1 (Ch 4, Section 4.5): the substitutions of the 4-line
'derivation', and its readings over N: forall x (x <= x) true, no largest natural number."""
from _s0102_fol import V, At, All, sub, free_for

QUOTED = {"lines": 4}

x, y, y0 = V('x'), V('y'), V('y_0')
assert sub(At('<=', x, x), y0, 'x') == At('<=', y0, y0)            # line 2, forall-E at y_0
assert sub(At('<=', x, y0), y0, 'x') == At('<=', y0, y0)           # line 3's phi[y_0/x]
phi = All('x', At('<=', x, y))
assert sub(phi, y0, 'y') == All('x', At('<=', x, y0)) and free_for(y0, 'y', phi)   # line 4
N = range(0, 500)
assert all(d <= d for d in N)
assert all(any(not (e <= d) for e in [d + 1]) for d in N)          # y + 1 beats every y
print("exr-existential-introduction-c1: all quoted values check")
